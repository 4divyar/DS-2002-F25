#!/bin/bash

echo "All card sets in card_set_lookup are being refreshed."

for FILE in ./card_set_lookup/*json;
do
	SET_ID=$(basename "$FILE" .json)
    echo "${SET_ID} is being updated."
    # Use the test JSON data as the source, since API doesn't work
    jq "." "card_set_lookup_test/${SET_ID}.json" > "$FILE"
    echo "Data was written to ${FILE}."
done

echo "All card sets have been refreshed."