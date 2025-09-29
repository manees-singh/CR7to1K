import requests
import tweepy
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import re

load_dotenv()

#Fetching data from web
"------------------------------------------------------------------------"

# File to store the previous goal count
GOAL_COUNT_FILE = "previous_goals.txt"

url = "https://www.roadto1000goals.com/"

# Variables to store current total goals and increment
current_total_goals = 0
goal_increment = 0

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get the total goal count
    goal_counter = soup.find('h1', class_='goal-counter')
    if goal_counter:
        current_total_goals = int(goal_counter.get_text(strip=True))
        print(f"Current total goals: {current_total_goals}")
    
    # Read previous goal count
    previous_goals = 0
    if os.path.exists(GOAL_COUNT_FILE):
        with open(GOAL_COUNT_FILE, 'r') as f:
            previous_goals = int(f.read().strip())
    
    
    goal_increment = current_total_goals - previous_goals
    

    print(f"Goal increment: {goal_increment}")
    if goal_increment > 0:
        inreased_goal=goal_increment
    
    # Save current total for next time
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

here=f"{goal_increment}"
client.create_tweet(text=here)

# auth =tweepy.OAuth1UserHandler(api_key, api_secret,access_token, access_token_secret)
# api=tweepy.API(auth)

# try:
#     # Test 1: Get your own user info
#     me = client.get_me()
#     print(f"✅ Twitter API working! Logged in as: {me.data.username}")
    
#     # Test 2: Check API limits
#     verify = api.verify_credentials()
#     if verify:
#         print(f"✅ API credentials verified! Account: @{verify.screen_name}")
    
# except Exception as e:
#     print(f"❌ Twitter API error: {e}")

# tweet_content = f"{current_total_goals}"

# response=client.create_tweet(text=tweet_content.strip())
