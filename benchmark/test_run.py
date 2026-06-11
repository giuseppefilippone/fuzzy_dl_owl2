import subprocess
import time

if __name__ == "__main__":
    # Run the test script and capture output
    try:
        t0 = time.perf_counter()
        result = subprocess.run(
            [
                "python",
                "run_queries.py",
                "gurobi",
                # "./data/mygrid-moby-service.txt",
                # "./data/FuzzyWine.txt",
                "./data/mosquito_insecticide_resistance.obo.txt",
            ],
            text=True,
            check=True,
            capture_output=True,
        )
        t1 = time.perf_counter()
        print("Test script output:")
        print(result.stdout.strip())
        if result.stderr:
            print("Test script errors:")
            print(result.stderr.strip())
        print(f"Test script completed in {t1 - t0:.2f} seconds.")
    except subprocess.CalledProcessError as e:
        print(f"Test script failed with return code {e.returncode}")
        print("Output:")
        print(e.stdout.strip())
        if e.stderr:
            print("Errors:")
            print(e.stderr.strip())
