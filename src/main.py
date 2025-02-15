import requests


def main():
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("All good!")
    else:
        print("Something went wrong")


if __name__ == "__main__":
    main()