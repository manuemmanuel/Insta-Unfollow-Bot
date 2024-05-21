# Instagram Unfollow Bot

This Python script identifies users who don't follow you back on Instagram and automatically unfollows them. It uses the `instaloader` module to interact with Instagram.

## Prerequisites

- Python 3.x
- `instaloader` module
- `requests` module

## Installation

1. Clone the repository or download the script.
2. Install the required Python modules:
   ```sh
   pip install instaloader requests```
   
## Usage

1. Set your Instagram username and password in the script:
```bash
INSTAGRAM_USERNAME = "your_username"
INSTAGRAM_PASSWORD = "your_password"
```
2. Run the script:
```bash
python main.py
```

3. The script will:

- Log in to Instagram.
- Retrieve the list of followers and followees.
- Identify users who don't follow you back.
- Unfollow users who don't follow you back, with a 30-second delay between each unfollow action to avoid rate limiting.
