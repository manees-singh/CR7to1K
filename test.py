import requests
import tweepy
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import random

load_dotenv()

#Fetching data from web
"------------------------------------------------------------------------"

# previous goal count
GOAL_COUNT_FILE = "previous_goals.txt"

url = "https://www.messivsronaldo.app/"

# Variables to store current total goals and increment
current_total_goals = 0
goal_increment = 0

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # total goal count
    ronaldo=soup.find('div', class_='StatsBlock-module--statsBlock--4b2a6 StatsBlock-module--RonaldoStatsBlock--f266e relative text-center w-1/2')
    goal_counter = ronaldo.find('li', class_='StatsBlock-module--goals--df119')

    if goal_counter:
        current_goal=goal_counter.find('span', class_ ='StatsBlock-module--statNum--f90f1')
        current_total_goals = int(current_goal.get_text(strip=True))
        
    
    # previous goal count
    previous_goals = 0
    if os.path.exists(GOAL_COUNT_FILE):
        with open(GOAL_COUNT_FILE, 'r') as f:
            previous_goals = int(f.read().strip())
    
    print(current_total_goals)
    goals = current_total_goals - previous_goals
    
    

    with open(GOAL_COUNT_FILE, 'w') as f:
        f.write(str(current_total_goals))

except Exception as e:
    print(f" Error parsing data: {e}")