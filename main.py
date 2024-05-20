
import instaloader
import requests
import time

INSTAGRAM_USERNAME = ""
INSTAGRAM_PASSWORD = ""

if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD:
    print("Please set the INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD environment variables.")
    exit()

L = instaloader.Instaloader()
L.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

profile = instaloader.Profile.from_username(L.context, INSTAGRAM_USERNAME)

followers = set(profile.get_followers())
followees = set(profile.get_followees())

not_following_back = followees - followers

session = L.context._session

def get_username(user_id):
    try:
        user = instaloader.Profile.from_id(L.context, user_id)
        return user.username
    except instaloader.ProfileNotExistsException:
        return "Unknown"

def unfollow(user_id):
    username = get_username(user_id)
    unfollow_url = f"https://www.instagram.com/web/friendships/{user_id}/unfollow/"
    response = session.post(unfollow_url)
    if response.status_code == 200:
        print(f"Unfollowed user: {username} (ID: {user_id})")
    else:
        print(f"Failed to unfollow user: {username} (ID: {user_id}), Status Code: {response.status_code}")

for user in not_following_back:
    unfollow(user.userid)
    time.sleep(30)

print(f"Unfollowed {len(not_following_back)} users who don't follow you back.")
