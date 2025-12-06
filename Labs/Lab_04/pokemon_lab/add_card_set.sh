#!/usr/bin/env bash

# use read to prompt user to tcg card set id and save response in SET_ID
read -r -p "Enter the TCG Card Set ID (eg. base1, base4):" SET_ID

# ensure error is thrown if setid is empty
if [ -z "$SET_ID" ]; then
    echo "Error: Set ID cannot be empty." >&2
    exit 1
fi

echo "The data from the ID $SET_ID is being fetched."

# API call - still does not work
# curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID&page=1&pageSize=250" > card_set_lookup/"$SET_ID".json

# manually using json
cp card_set_lookup/"$SET_ID".json .

echo "Successfully saved the data to card_set_loopup/$SET_ID.json"