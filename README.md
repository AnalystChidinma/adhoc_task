# Adhoc Python Task – Data Quality check & JSON processing

## Overview

This task demonstrates working with Python lists and JSON data.
It covers:

- Checking data types

- Filtering data based on conditions

- Handling JSON files


### Task Description
1. List Data Type Check

  - Check the data type of elements in a list.

  - Filter elements that are:

      - Strings

      - Start with "Republic"

      - End with "Nigeria"

  2. Save JSON Data

  - Fetch champion data from this link:
  `https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/champion.json`

  - Save it locally as a JSON file for processing.

3. Extract and Filter JSON

Extract the following fields from the JSON:
  - name,
  - title,
  - attack,  and
  - defense

  ### *Keep only champions where attack > 5 or defense > 5* ###

  - Save the filtered data both as:

      - JSON file and

      - Pandas DataFrame
  
4. String Handling Scripts

  - One script ignores strings in a list gracefully.

  - Another script fails intentionally if a string is found.
This shows safe handling vs strict rules.

## Requirements

1. Python 3.13

2. Pandas

3. Requests

  - Install packages with:

`pip install pandas requests`
    
