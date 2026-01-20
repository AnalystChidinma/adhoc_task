from adhoc_fetch_raw_json import json
import pandas as pd

with open("champion.json", "r") as json_file:
    champion = json.load(json_file)

result = []

for champ in champion["data"].values():
    if champ["info"]["attack"] > 5 and champ["info"]["defense"] > 5:
        result.append({
            "name": champ["name"],
            "title": champ["title"],
            "attack": champ["info"]["attack"],
            "defense": champ["info"]["defense"]
        })
    with open("champion_result.json", "w") as result_file:
        json.dump(result, result_file, indent=4)

    df = pd.json_normalize(result)

    print(df)
    print("saved as both dataframe and JSON" )