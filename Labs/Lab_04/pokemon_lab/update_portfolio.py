import os
import sys
import json
import pandas as pd

# load lookup data function
def _load_lookup_data(lookup_dir):
    all_lookup_df = []

    for filename in os.listdir(lookup_dir):
        if not filename.endswith(".json"): # error handling
            continue

        # get and read json data
        filepath = os.path.join(lookup_dir, filename)
        with open(filepath, "r", encoding='utf-8') as f:
            data = json.load(f)

        df = pd.json_normalize(data['data'])

        df['card_market_value'] = (df.get("tcgplayer.prices.holofoil.market", pd.Series([None]*len(df)))
                                   .fillna(df.get("tcgplayer.prices.normal.market", 0.0))
                                   .fillna(0.0) )

        df = df.rename(columns = {
            "id": "card_id",
            "name": "card_name",
            "number": "card_number",
            "set.id": "set_id",
            "set.name": "set_name"
        })

        required_cols = [
            "card_id", "card_name", "card_number",
            "set_id", "set_name", "card_market_value"
        ]
        df = df[required_cols]
        all_lookup_df.append(df)

    # create final
    lookup_df = pd.concat(all_lookup_df, ignore_index=True)

    # only return what we want, subset
    return lookup_df.drop_duplicates(subset=["card_id"], keep="first").sort_values(by="card_id")


# load inventory data function
def _load_inventory_data(inventory_dir):
    inventory_data = []

    # error handling, makes sure its csv file
    for filename in os.listdir(inventory_dir): 
        if not filename.endswith(".csv"):
            continue

        # gets and reads data
        filepath = os.path.join(inventory_dir, filename)
        df = pd.read_csv(filepath)
        inventory_data.append(df)

        if inventory_data.empty:
            return pd.DataFrame()
    
        inventory_df = pd.concat(inventory_data, ignore_index=True)

        # return unified key column
        inventory_df["card_id"] = inventory_df["set_id"].astype(str) + "-" + inventory_df["card_number"].astype(str)
        return inventory_df


# update portfolio function
def update_portfolio(inventory_dir, lookup_dir, output_file):

    lookup_df = _load_lookup_data(lookup_dir)
    inventory_df = _load_inventory_data(inventory_dir)

    # error handling, empty inventory
    if inventory_df.empty:
        print("Error, the inventory dataframe is empty. Creating empty portfolio CSV.", file=sys.stderr)
        headers = ["card_id", "card_name", "card_number", "set_name", "set_id", "card_market_value"]
        empty_cols = [
            "index", "binder_name", "page_number", "slot_number",
            "card_id", "card_name", "set_id", "set_name", "card_market_value"
        ]
        empty_portfolio = pd.DataFrame(columns=headers)
        empty_portfolio.to_csv(output_file, index=False)
        return
    
    # data merge, on card_id
    merged_df = pd.merge(
        inventory_df,
        lookup_df[["card_id", "card_name", "set_name", "card_market_value"]],
        on="card_id",
        how="left"
    )

    # cleaning final - fill missing values
    merged_df["card_market_value"] = merged_df["card_market_value"].fillna(0.0)
    merged_df["set_name"] = merged_df["set_name"].fillna("NOT_FOUND")

    # index creation
    merged_df["index"] = (
        merged_df["binder_name"].astype(str) + "-" +
        merged_df["page_number"].astype(str) + "-" +
        merged_df["slot_number"].astype(str)
    )

    final_cols = [
        "index", "binder_name", "page_number", "slot_number",
        "card_id", "card_name", "set_id", "set_name", "card_market_value"
    ]

    merged_df[final_cols].to_csv(output_file, index=False)

    print("Portfolio successfully created!")


# main funciton
def main():
    update_portfolio(
        inventory_dir="./card_inventory/",
        lookup_dir="./card_set_lookup/",
        output_file="card_portfolio.csv"
    )


# test function
def test():
    update_portfolio(
        inventory_dir="./card_inventory_test/",
        lookup_dir="./card_set_lookup_test/",
        output_file="test_card_portfolio.csv"
    )


# main block
# if __name__ == "__main__":
#     print("Starting Pokémon Card portfolio ETL in test mode.", file=sys.stderr)
#     test()