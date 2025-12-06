#!/usr/bin/env python3

import sys
import update_portfolio
import generate_summary

def run_production_pipeline():
    print("Starting production pipeline.", file=sys.stderr)

    # etl
    print("Running ETL...", file=sys.stderr)
    update_portfolio.main()

    # reporting
    print("Running portfolio summary report...", file=sys.stderr)
    generate_summary.main()

    print("Production pipeline complete!", file=sys.stderr)

if __name__ == "__main__":
    run_production_pipeline()