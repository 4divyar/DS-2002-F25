#!/bin/bash

# use read to prompt user to tcg card set id and save response in SET_ID
read -p "Enter the TCG Card Set ID (eg. base1, base4):" SET_ID

# ensure error is thrown if setid is empty
if [ -z "$SET_ID" ]; then
    echo "Error: Set ID cannot be empty." >&2
    exit 1
fi

echo "The data from the ID $SET_ID is being fetched."

# API didn't work, so manually added jsons
jq '.' "card_set_lookup_test/${SET_ID}.json" > "card_set_lookup/${SET_ID}.json"