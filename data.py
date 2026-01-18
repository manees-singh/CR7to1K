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
goals = 0

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

"""                                 Twitter setup                                    """
"-----------------------------------------------------------------------------------------"
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')



client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

filled_char = '\u2588'  # full block '█'
unfilled_char = '░'
ball='\u26BD'
thousand=1000
bar_length=22
tags=["#Ronaldo #CR7 #Siuuu", "#Ronaldo #GOAT", "#CR7 #Ronaldo", "#Ronaldo #CR7",
      "#CR7 #VivaRonaldo" , "#Ronaldo #GOAT #CR7"]
chant=["SIIIIIIIIIIUUUUUUUUUU! 🐐", "Another goal for Cristiano Ronaldo! 👑",
       "THE GOAL MACHINE HAS BEEN ACTIVATED. 🤖","He scores when he wants!", 
       "GOAL RONALDO! 🔥","👑 Cristiano Ronaldo puts it in the back of the net",
         "GOAL RONALDO! 💥", "EL BICHO GETS ANOTHER ONE "+ ball  ]


filled_length=int((previous_goals/thousand)*bar_length)
solid_blocks_length = filled_length - goals
unfilled_length = bar_length - filled_length
bar = (filled_char * solid_blocks_length) + (ball * goals) + (unfilled_char * unfilled_length)




# tweet_content=f"\r{bar}  {current_total_goals}/1000\n"

tweet_content= random.choice(chant) + "\n"
tweet_content=f"{1000-current_total_goals} more to go\n"
tweet_content += random.choice(tags) 
tweet_content += f"\r{bar}  {current_total_goals}/1000\n"

if goals>0:

    client.create_tweet(text=tweet_content)





