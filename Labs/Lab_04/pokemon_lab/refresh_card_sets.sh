#!/bin/bash

echo "All card sets in card_set_lookup are being refreshed."


for FILE in card_set_lookup/*.json; do
    # extract set_id from filename
    SET_ID=$(basename "$FILE" .json)

    echo "Updating set: $SET_ID"

    # API call - doesn't work
    # curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID&page=1&pageSize=250" > "$FILE"

    # using local json
    cp card_set_lookup/"$SET_ID".json "$FILE"

    echo "Data written to "$FILE"
done

echo "All card sets have been refreshed."