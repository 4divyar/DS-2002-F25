import sys
import update_portfolio
import generate_summary

def run_production_pipeline():
    print("Starting production pipeline.", file=sys.stderr)

    # etl
    print("Running ETL.")
    update_portfolio.main()

    # reporting
    print("Running generate_summary.")
    generate_summary.main()

    print("Production pipeline complete!", file=sys.stderr)
