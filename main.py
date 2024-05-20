import os
import time
from instabot import Bot

# Initialize the bot
bot = Bot()

# Securely handle credentials using environment variables
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')

if not username or not password:
    print("Please set the INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD environment variables.")
    exit()

# Login to Instagram
bot.login(username=username, password=password)

# Get the list of your followers
followers = bot.get_user_followers(username)

# Get the list of users you are following
following = bot.get_user_following(username)

# Identify users who you follow but who don't follow you back
not_following_back = [user for user in following if user not in followers]

# Unfollow users who don't follow you back with rate limiting
for user_id in not_following_back:
    bot.unfollow(user_id)
    print(f"Unfollowed user ID: {user_id}")
    time.sleep(30)  # Wait 30 seconds between unfollows to avoid rate limiting

print(f"Unfollowed {len(not_following_back)} users who don't follow you back.")
