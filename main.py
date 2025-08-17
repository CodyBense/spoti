import functions


def main():
    access_token = functions.get_access_token()
    print(f"is playing: {functions.play_pause(access_token)}")


if __name__ == "__main__":
    main()
