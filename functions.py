import requests
import pandas
import json
import os
from dotenv import load_dotenv
from urllib3 import request


load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_access_token() -> str:
    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    try:

        response = requests.post(url, headers=headers, data=payload)

        response.raise_for_status() 

        return response.json()['access_token']

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
        return ""
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        return ""
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return ""
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
        return ""


def play_pause(access_token: str):
    try:
        url = "https://api.spotify.com/v1/me/player?market=US"

        header = {
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.get(url, headers=header)

        print(response)
        # if response.json()["is_playing"]:
        #     print("song is playing")
        # else:
        #     print("nothing is playing")

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")


def search():
    pass


def skip_for():
    pass


def skip_bac():
    pass
