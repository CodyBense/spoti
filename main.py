import functions


def main():
    # access_token = functions.get_access_token()
    # print(f"{access_token}")
    # print(f"is playing: {functions.play_pause(access_token)}")
    # functions.oauth_auth()
    
    token = functions.get_access_token()
    artist_result = functions.search_for_artist(token, "Mac Miller")
    artist_id = artist_result["id"]

    songs = functions.get_songs_by_artist(token, artist_id)

    for idx, song in enumerate(songs):
        print(f"{idx + 1}. {song['name']}")


if __name__ == "__main__":
    main()
