import requests
import json

url = "https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/champion.json"

response = requests.get(url)
result = response.json()

with open("champion.json", "w") as file:
        json.dump(result, file, indent=4)
        
        print("json file saved successfully")