import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables first
load_dotenv()

# Player ID for the query
player_id = 874

# API endpoint for player statistics
url = "https://v3.football.api-sports.io/players"

# Parameters for the 2023 season (free plan limitation)
payload = {
    'id': player_id,
    'season': '2023'
}

headers = {
  'x-rapidapi-key': os.getenv('DATA_KEY'),
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.request("GET", url, headers=headers, params=payload)

# Parse the response
data = response.json()

# Pretty print the JSON response
print(json.dumps(data, indent=2))

# Extract and display goal statistics if available
if data['results'] > 0:
    player_data = data['response'][0]
    player = player_data['player']
    statistics = player_data['statistics']
    
    print(f"\n=== GOAL STATISTICS for {player['name']} (ID: {player['id']}) ===")
    print(f"Age: {player['age']}")
    print(f"Nationality: {player['nationality']}")
    print(f"Position: {player['position']}")
    
    for stat in statistics:
        team = stat['team']
        league = stat['league']
        goals = stat['goals']
        games = stat['games']
        
        print(f"\n--- {team['name']} ({league['name']}) ---")
        print(f"Games Played: {games['appearences']}")
        print(f"Goals Scored: {goals['total']}")
        print(f"Goals (Home): {goals['home']}")
        print(f"Goals (Away): {goals['away']}")
        print(f"Minutes Played: {games['minutes']}")
        
        if goals['total']:
            print(f"Goals per Game: {goals['total'] / games['appearences']:.2f}")
else:
    print("No data found for player ID 874")