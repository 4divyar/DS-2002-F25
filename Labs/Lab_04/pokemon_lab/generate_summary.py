import os
import sys
import pandas as pd

def generate_summary(portfolio_file):

    # check if file exists
    if not os.path.exists(portfolio_file):
        print("The file '{portfolio_file}' is not found, error.", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(portfolio_file)

    # check if df empty
    if df.empty:
        print("The portfolio file dataframe is empty.")
        return
    
    # calculate total portfolio value
    total_port_value = df['card_market_value'].sum()

    # find most valuable card
    most_val_index = df['card_market_value'].idmax()
    most_val_card = df.loc[most_val_index]

    # print report
    print("The total portfolio market value is ${total_port_value}.")
    print(f"The most valuable card is {most_val_card['card_name']}. Its ID is {most_val_card['card_id']} and its market value is {most_val_card['card_market_value']}.")


# main function
def main():
    generate_summary('card_portfolio.csv')

# test function
def test():
    generate_summary('test_card_portfolio.csv')

# if __name__ == "__main__":
#     test()