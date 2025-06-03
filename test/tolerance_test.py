import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple, Any
import mip
import highspy as highs
import time
import logging
from dataclasses import dataclass
from enum import Enum


class SolverResult(Enum):
    OPTIMAL = "optimal"
    INFEASIBLE = "infeasible"
    UNBOUNDED = "unbounded"
    ERROR = "error"
    TIME_LIMIT = "time_limit"


@dataclass
class SolverConfiguration:
    """Configuration for solver parameters"""

    name: str
    primal_feasibility_tolerance: float = 1e-7
    dual_feasibility_tolerance: float = 1e-7
    mip_feasibility_tolerance: float = 1e-6
    mip_gap_tolerance: float = 1e-4
    presolve: str = "on"  # "on", "off", "choose"
    time_limit: float = 300.0


class MILPSolverComparator:
    """
    A comprehensive tool for comparing MILP solvers with different tolerance settings.
    This class helps diagnose why problems are feasible in one solver but not another.
    """

    def __init__(self, problem_file_path: str = None):
        self.problem_file_path = problem_file_path
        self.results = []

        # Set up logging to track solver behavior
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger(__name__)

    def create_tolerance_configurations(self) -> List[SolverConfiguration]:
        """
        Create a range of tolerance configurations to test systematic sensitivity.
        We'll test from very strict to very relaxed tolerances.
        """
        configurations = []

        # Base configuration (HiGHS defaults)
        configurations.append(
            SolverConfiguration(
                name="HiGHS_Default",
                primal_feasibility_tolerance=1e-7,
                dual_feasibility_tolerance=1e-7,
                mip_feasibility_tolerance=1e-6,
            )
        )

        # Match python-MIP's tight tolerances
        configurations.append(
            SolverConfiguration(
                name="Match_PythonMIP_Tight",
                primal_feasibility_tolerance=1e-9,
                dual_feasibility_tolerance=1e-9,
                mip_feasibility_tolerance=1e-9,
            )
        )

        # Progressively relaxed tolerances
        tolerance_levels = [1e-6, 1e-5, 1e-4, 1e-3, 1e-2]

        for tol in tolerance_levels:
            configurations.append(
                SolverConfiguration(
                    name=f"Relaxed_{tol:.0e}",
                    primal_feasibility_tolerance=tol,
                    dual_feasibility_tolerance=tol,
                    mip_feasibility_tolerance=tol,
                )
            )

        # Test different presolve settings
        for presolve_setting in ["off", "choose"]:
            configurations.append(
                SolverConfiguration(
                    name=f"Presolve_{presolve_setting}",
                    primal_feasibility_tolerance=1e-6,
                    dual_feasibility_tolerance=1e-6,
                    mip_feasibility_tolerance=1e-6,
                    presolve=presolve_setting,
                )
            )

        return configurations

    def solve_with_highs(
        self, config: SolverConfiguration, problem_data: Dict[str, Any]
    ) -> Tuple[SolverResult, Dict[str, Any]]:
        """
        Solve the problem using HiGHS with specific configuration.
        Returns the result status and additional information.
        """
        try:
            # Create HiGHS model
            h = highs.Highs()
            h.silent()  # Suppress output initially

            # Set tolerances based on configuration
            h.setOptionValue(
                "primal_feasibility_tolerance", config.primal_feasibility_tolerance
            )
            h.setOptionValue(
                "dual_feasibility_tolerance", config.dual_feasibility_tolerance
            )
            h.setOptionValue(
                "mip_feasibility_tolerance", config.mip_feasibility_tolerance
            )
            h.setOptionValue("mip_gap_tolerance", config.mip_gap_tolerance)
            h.setOptionValue("presolve", config.presolve)
            h.setOptionValue("time_limit", config.time_limit)

            # Load problem from LP file if available
            if self.problem_file_path:
                status = h.readModel(self.problem_file_path)
                if status != highs.HighsStatus.kOk:
                    return SolverResult.ERROR, {"error": "Failed to read model"}
            else:
                # Build problem from problem_data
                self._build_highs_model_from_data(h, problem_data)

            # Solve the problem
            start_time = time.time()
            status = h.run()
            solve_time = time.time() - start_time

            # Get solution information
            info = h.getInfo()
            solution_info = {
                "solve_time": solve_time,
                "objective_value": None,
                "num_iterations": info.simplex_iteration_count,
                "primal_status": None,
                "dual_status": None,
            }

            # Interpret the result
            if status == highs.HighsStatus.kOk:
                model_status = h.getModelStatus()

                if model_status == highs.HighsModelStatus.kOptimal:
                    solution = h.getSolution()
                    solution_info["objective_value"] = info.objective_function_value
                    solution_info["primal_status"] = "feasible"
                    solution_info["dual_status"] = "feasible"
                    return SolverResult.OPTIMAL, solution_info

                elif model_status == highs.HighsModelStatus.kInfeasible:
                    solution_info["primal_status"] = "infeasible"
                    return SolverResult.INFEASIBLE, solution_info

                elif model_status == highs.HighsModelStatus.kUnbounded:
                    return SolverResult.UNBOUNDED, solution_info

                elif model_status == highs.HighsModelStatus.kTimeLimit:
                    return SolverResult.TIME_LIMIT, solution_info

            return SolverResult.ERROR, solution_info

        except Exception as e:
            self.logger.error(f"Error solving with HiGHS: {str(e)}")
            return SolverResult.ERROR, {"error": str(e)}

    def solve_with_python_mip(
        self, problem_data: Dict[str, Any] = None
    ) -> Tuple[SolverResult, Dict[str, Any]]:
        """
        Solve using python-MIP with configuration matching your original setup.
        This serves as our baseline for comparison.
        """
        try:
            # Create model with CBC backend (matching your configuration)
            model = mip.Model(
                name="Comparison", sense=mip.MINIMIZE, solver_name=mip.CBC
            )
            model.verbose = 0
            model.infeas_tol = 1e-9  # Matching your configuration
            model.integer_tol = 1e-9  # Matching your configuration
            model.max_mip_gap = 1e-6  # Assuming a small epsilon value
            model.emphasis = mip.SearchEmphasis.OPTIMALITY
            model.opt_tol = 0
            model.preprocess = 1

            # Load from LP file if available
            if self.problem_file_path:
                model.read(self.problem_file_path)
            else:
                raise ValueError

            start_time = time.time()
            status = model.optimize()
            solve_time = time.time() - start_time

            solution_info = {
                "solve_time": solve_time,
                "objective_value": (
                    model.objective_value if model.objective_value else None
                ),
                "num_vars": len(model.vars),
                "num_constraints": model.num_rows,
                "gap": model.gap if hasattr(model, "gap") else None,
            }

            if status == mip.OptimizationStatus.OPTIMAL:
                return SolverResult.OPTIMAL, solution_info
            elif status == mip.OptimizationStatus.INFEASIBLE:
                return SolverResult.INFEASIBLE, solution_info
            elif status == mip.OptimizationStatus.UNBOUNDED:
                return SolverResult.UNBOUNDED, solution_info
            else:
                return SolverResult.ERROR, solution_info

        except Exception as e:
            self.logger.error(f"Error solving with python-MIP: {str(e)}")
            return SolverResult.ERROR, {"error": str(e)}

    def run_comprehensive_comparison(self, lp_file_path: str) -> pd.DataFrame:
        """
        Run a comprehensive comparison across all tolerance configurations.
        This is the main method you'll use to diagnose solver differences.
        """
        self.problem_file_path = lp_file_path
        self.logger.info(f"Starting comprehensive comparison for {lp_file_path}")

        results = []

        # First, test with python-MIP as baseline
        self.logger.info("Testing with python-MIP (baseline)...")
        pymip_result, pymip_info = self.solve_with_python_mip()

        baseline_entry = {
            "Solver": "python-MIP (CBC)",
            "Configuration": "Your_Original_Settings",
            "Result": pymip_result.value,
            "Solve_Time": pymip_info.get("solve_time", 0),
            "Objective_Value": pymip_info.get("objective_value"),
            "Primal_Tol": 1e-9,
            "Dual_Tol": 1e-9,
            "MIP_Tol": 1e-9,
            "Presolve": "on",
            "Notes": "Baseline configuration",
        }
        results.append(baseline_entry)

        # Test all HiGHS configurations
        configurations = self.create_tolerance_configurations()

        for i, config in enumerate(configurations):
            self.logger.info(
                f"Testing HiGHS configuration {i+1}/{len(configurations)}: {config.name}"
            )

            highs_result, highs_info = self.solve_with_highs(config, {})

            entry = {
                "Solver": "HiGHS",
                "Configuration": config.name,
                "Result": highs_result.value,
                "Solve_Time": highs_info.get("solve_time", 0),
                "Objective_Value": highs_info.get("objective_value"),
                "Primal_Tol": config.primal_feasibility_tolerance,
                "Dual_Tol": config.dual_feasibility_tolerance,
                "MIP_Tol": config.mip_feasibility_tolerance,
                "Presolve": config.presolve,
                "Notes": self._generate_analysis_notes(
                    highs_result, highs_info, pymip_result
                ),
            }
            results.append(entry)

            # Log significant findings
            if highs_result != pymip_result:
                self.logger.warning(
                    f"Difference detected: {config.name} -> {highs_result.value} vs python-MIP -> {pymip_result.value}"
                )
            elif (
                highs_result == SolverResult.OPTIMAL
                and pymip_result == SolverResult.OPTIMAL
            ):
                self.logger.info(f"SUCCESS: {config.name} matches python-MIP result!")

        # Create comprehensive results DataFrame
        df = pd.DataFrame(results)

        # Add summary statistics
        self._add_summary_analysis(df)

        return df

    def _generate_analysis_notes(
        self,
        highs_result: SolverResult,
        highs_info: Dict[str, Any],
        pymip_result: SolverResult,
    ) -> str:
        """Generate analytical notes about the comparison"""
        notes = []

        if highs_result == pymip_result:
            notes.append(
                f"✓ Matches python-MIP result ({highs_result.value}, {pymip_result.value})"
            )
        else:
            notes.append(f"✗ Differs from python-MIP ({highs_result.value}, {pymip_result.value})")

        if highs_result == SolverResult.INFEASIBLE and "error" not in highs_info:
            notes.append("Detected infeasibility during solve")
        elif highs_result == SolverResult.ERROR:
            notes.append(f"Error: {highs_info.get('error', 'Unknown error')}")

        solve_time = highs_info.get("solve_time", 0)
        if solve_time > 10:
            notes.append("Slow convergence")
        elif solve_time < 0.1:
            notes.append("Fast solve")

        return "; ".join(notes)

    def _add_summary_analysis(self, df: pd.DataFrame):
        """Add summary analysis to help interpret results"""
        print("\n" + "=" * 80)
        print("COMPREHENSIVE SOLVER COMPARISON ANALYSIS")
        print("=" * 80)

        # Count results by type
        result_counts = df["Result"].value_counts()
        print(f"\nResult Distribution:")
        for result, count in result_counts.items():
            print(f"  {result}: {count} configurations")

        # Identify successful HiGHS configurations
        successful_highs = df[(df["Solver"] == "HiGHS") & (df["Result"] == "optimal")]
        if len(successful_highs) > 0:
            print(
                f"\n✓ SUCCESS: Found {len(successful_highs)} HiGHS configurations that work!"
            )
            print("Successful configurations:")
            for _, row in successful_highs.iterrows():
                print(
                    f"  - {row['Configuration']}: Primal={row['Primal_Tol']:.0e}, Dual={row['Dual_Tol']:.0e}"
                )
        else:
            print("\n✗ No HiGHS configurations succeeded")

        # Analyze tolerance sensitivity
        failed_highs = df[(df["Solver"] == "HiGHS") & (df["Result"] == "infeasible")]
        if len(failed_highs) > 0:
            min_failing_tol = failed_highs["Primal_Tol"].min()
            max_failing_tol = failed_highs["Primal_Tol"].max()
            print(f"\nTolerance Analysis:")
            print(
                f"  Failing tolerance range: {min_failing_tol:.0e} to {max_failing_tol:.0e}"
            )

        print("\nRecommendations:")
        if len(successful_highs) > 0:
            best_config = successful_highs.iloc[0]
            print(f"  1. Use configuration: {best_config['Configuration']}")
            print(
                f"     - Set primal_feasibility_tolerance = {best_config['Primal_Tol']:.0e}"
            )
            print(
                f"     - Set dual_feasibility_tolerance = {best_config['Dual_Tol']:.0e}"
            )
            print(
                f"     - Set mip_feasibility_tolerance = {best_config['MIP_Tol']:.0e}"
            )
        else:
            print("  1. Consider problem reformulation")
            print("  2. Try alternative solver backends")
            print("  3. Check for numerical scaling issues")


def demonstrate_usage():
    """
    Demonstrate how to use the solver comparison tool with your LP file.
    """
    print("MILP Solver Comparison Tool")
    print("=" * 50)

    # Initialize the comparator
    comparator = MILPSolverComparator()

    # For demonstration, let's assume you have saved your LP file
    lp_file_path = "./results/highs_model.lp"  # Replace with actual path

    print(f"Analyzing problem from: {lp_file_path}")
    print("This will test multiple tolerance configurations with HiGHS")
    print("to find settings that match your python-MIP results.\n")

    try:
        # Run comprehensive comparison
        results_df = comparator.run_comprehensive_comparison(lp_file_path)

        # Save results for further analysis
        results_df.to_csv("solver_comparison_results.csv", index=False)
        print(f"\nDetailed results saved to: solver_comparison_results.csv")

        # Display summary table
        print("\nSUMMARY TABLE:")
        print("-" * 100)
        display_cols = [
            "Solver",
            "Configuration",
            "Result",
            "Solve_Time",
            "Primal_Tol",
            "Notes",
        ]
        print(results_df[display_cols].to_string(index=False, max_colwidth=30))

    except Exception as e:
        print(f"Error during analysis: {e}")
        print("Make sure your LP file path is correct and accessible.")


if __name__ == "__main__":
    demonstrate_usage()
