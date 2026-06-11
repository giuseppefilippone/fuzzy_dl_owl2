import json
import os

import numpy as np


def load_json_file(file_path):
    """Load JSON data from file."""
    with open(file_path, "r") as f:
        return json.load(f)


def generate_latex_table(python_results, java_results):
    """Generate LaTeX table from benchmark results."""
    # Get all KB names (keys from both results)
    all_kb_names = set(python_results.keys()) | set(java_results.keys())
    kb_names: list[str] = sorted(all_kb_names, key=lambda x: x.lower())

    # Start LaTeX table
    latex_lines = []

    total_cases = 0
    python_speedup_counter = 0
    outperformance_cases = []
    times_differences = []

    # Process each KB
    for kb_name in kb_names:
        escape_kb_name = kb_name  #  re.escape(kb_name).replace("_", "\\_")

        # Get Python results
        py_data = python_results.get(kb_name, {})

        # Get Java results
        java_data = java_results.get(kb_name, {})
        java_avg = java_data.get("avg", 0) if java_data else 0

        # Skip if missing data (no Java data or no Python solver data)
        if len(java_data) == 0 and all(len(v) == 0 for v in py_data.values()):
            continue

        # Get solver results
        gurobi_data = py_data.get("Gurobi", {})
        gurobi_avg = gurobi_data.get("avg", 0) if gurobi_data else 0

        cbc_data = py_data.get("CBC", {})
        cbc_avg = cbc_data.get("avg", 0) if cbc_data else 0

        highs_data = py_data.get("HiGHS", {})
        highs_avg = highs_data.get("avg", 0) if highs_data else 0

        total_cases += 1

        # Format Java results
        java_std = java_data.get("std", 0) if java_data else 0
        java_str = f"{java_avg:.2f} \\pm {java_std:.2f}" if java_avg > 0 else "\\textbf{N/A}"

        # Format Gurobi results
        if gurobi_data and gurobi_avg > 0:
            gurobi_std = gurobi_data.get("std", 0)
            gurobi_str = f"{gurobi_avg:.2f} \\pm {gurobi_std:.2f}"
        else:
            gurobi_str = "\\textbf{N/A}"

        # Format CBC results
        if cbc_data and cbc_avg > 0:
            cbc_std = cbc_data.get("std", 0)
            cbc_str = f"{cbc_avg:.2f} \\pm {cbc_std:.2f}"
        else:
            cbc_str = "\\textbf{N/A}"

        # Format HiGHS results
        if highs_data and highs_avg > 0:
            highs_std = highs_data.get("std", 0)
            highs_str = f"{highs_avg:.2f} \\pm {highs_std:.2f}"
        else:
            highs_str = "\\textbf{N/A}"

        # Calculate speedup (ratio of Java to best solver)
        solver_avgs = []
        if gurobi_avg > 0:
            solver_avgs.append(gurobi_avg)
        if cbc_avg > 0:
            solver_avgs.append(cbc_avg)
        if highs_avg > 0:
            solver_avgs.append(highs_avg)

        speedup = 0.0
        if java_avg > 0 and solver_avgs:
            best_solver_avg = min(solver_avgs)  # Lower is better (time)
            speedup = java_avg / best_solver_avg
            speedup_str = f"${speedup:.3f}$"
        else:
            speedup_str = "$0$"
            speedup = float("inf") if java_avg > 0 else 0.0

        if java_avg == 0:
            speedup_str = "\\textbf{N/A}"
            speedup = float("inf") if solver_avgs else 0.0

        if speedup > 1:
            python_speedup_counter += 1

        times = [java_avg if java_avg > 0 else float("inf")] + solver_avgs
        best_time = np.argmin(times)

        if best_time == 0:
            java_str = f"\\mathbf{{{java_str}}}"
        elif best_time == 1:
            gurobi_str = f"\\mathbf{{{gurobi_str}}}"
        elif best_time == 2:
            cbc_str = f"\\mathbf{{{cbc_str}}}"
        elif best_time == 3:
            highs_str = f"\\mathbf{{{highs_str}}}"

        if java_str != "\\textbf{N/A}":
            java_str = f"${java_str}$"

        gurobi_str = f"${gurobi_str}$"
        cbc_str = f"${cbc_str}$"
        highs_str = f"${highs_str}$"

        # Add row to table
        latex_lines.append(
            ((speedup, times[best_time]), f"\\path{{{escape_kb_name}}} & {java_str} & {gurobi_str} & {cbc_str} & {highs_str} & {speedup_str} \\\\")
        )

        if speedup > 1 or java_avg == 0:
            outperformance_cases.append(f"\\path{{{escape_kb_name}}}")
        if java_avg > 0:
            times_differences.append(
                max(0, abs(java_avg - min(solver_avgs)) if solver_avgs else 0)
            )

    print(
        f"Python solvers were faster than Java in {python_speedup_counter} out of {total_cases} cases."
    )
    if outperformance_cases:
        print("Cases where Python outperformed Java or Java data was missing:")
        print(", ".join(outperformance_cases))

    if times_differences:
        print(
            "Maximum time difference between Java and best Python solver:",
            max(times_differences),
        )
        print(
            "Minimum time difference between Java and best Python solver:",
            min(times_differences),
        )

    # Sort rows by speedup (descending)
    latex_lines.sort(key=lambda x: x[0], reverse=True)
    return "\n".join([line[1] for line in latex_lines])


def main():
    # Define file paths
    python_results_path = os.path.join("results", "benchmark_results.json")
    java_results_path = os.path.join("results", "java_benchmark_results.json")

    # Load benchmark results
    python_results = load_json_file(python_results_path)
    java_results = load_json_file(java_results_path)

    # Generate LaTeX table
    latex_table = generate_latex_table(python_results, java_results)

    # Write to file
    output_file = "benchmark_table.tex"
    with open(output_file, "w") as f:
        f.write(latex_table)

    print(f"LaTeX table generated and saved to {output_file}")


if __name__ == "__main__":
    main()
