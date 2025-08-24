import oauthlib
from requests_oauthlib import OAuth2Session
import requests
import pandas
import json
import os
from dotenv import load_dotenv
import base64


load_dotenv()
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

oauth_client_id = os.getenv("OAUTH_CLIENT_ID")
oauth_client_secret = os.getenv("OAUTH_CLIENT_SECRET")
redirect_url = os.getenv("OAUTH_REDIRECT_ID")


def  oauth_auth():
    oauth = OAuth2Session(oauth_client_id, redirect_uri=redirect_url)

    authorization_url, state = oauth.authorization_url(
        'https://service.com/auth',
        access_type="offline", prompt="select_account"
    )

    print('Please visit %s and authroize acess.' % authorization_url)


def  get_access_token():
    auth_str = spotify_client_id + ':' + spotify_client_secret
    auth_bytes = auth_str.encode("utf-8")
    auth_base64  = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers =  {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "grant_type": "client_credentials",
    }

    result =  requests.post(url, headers=headers, data=data)

    json_result = json.loads(result.content)

    token = json_result["access_token"]

    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_artist(token, artist_name):
    url =  "https://api.spotify.com/v1/search"
    headers =  get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query

    result = requests.get(query_url, headers=headers)

    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exist...")
        return None

    return json_result[0]


def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)

    json_result = json.loads(result.content)["tracks"]

    return json_result


# def get_access_token() -> str:
#     url = "https://accounts.spotify.com/api/token"
#
#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
#
#     payload = {
#         "grant_type": "client_credentials",
#         "client_id": spotify_client_id,
#         "client_secret": spotify_client_secret
#     }
#
#     try:
#
#         response = requests.post(url, headers=headers, data=payload)
#
#         response.raise_for_status() 
#
#         return response.json()['access_token']
#
#     except requests.exceptions.HTTPError as errh:
#         print(f"Http Error: {errh}")
#         return ""
#     except requests.exceptions.ConnectionError as errc:
#         print(f"Error Connecting: {errc}")
#         return ""
#     except requests.exceptions.Timeout as errt:
#         print(f"Timeout Error: {errt}")
#         return ""
#     except requests.exceptions.RequestException as err:
#         print(f"Something went wrong: {err}")
#         return ""


def play_pause(access_token: str):
    try:
        url = "https://api.spotify.com/v1/me/player"

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
