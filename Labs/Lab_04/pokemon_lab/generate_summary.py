#!/usr/bin/env python3

import os
import sys
import pandas as pd

def generate_summary(portfolio_file):
    """Reads the portfolio CSV and prints a simplified summary to the console."""

    # check if file exists
    if not os.path.exists(portfolio_file):
        print("Error: The file '{portfolio_file}' is not found.", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(portfolio_file)

    # check if df empty
    if df.empty:
        print("The portfolio file dataframe is empty.")
        return
    
    # calculate total portfolio value
    total_port_value = df['card_market_value'].sum()

    # find most valuable card
    most_val_card = df.loc[df['card_market_value'].idxmax()]

    # print report
    print(f"Total Portfolio Value: ${total_port_value:,.2f}")
    print(f"Most Valuable Card Name: {most_val_card['card_name']}, Card ID: {most_val_card['card_id']}, Value: {most_val_card['card_market_value']:,.2f}")


# main function
def main():
    generate_summary('card_portfolio.csv')

# test function
def test():
    generate_summary('test_card_portfolio.csv')

if __name__ == "__main__":
    test()