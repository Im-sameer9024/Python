import requests

api_url = "https://api.freeapi.app/api/v1/public/randomusers"


def fetch_api_data(url):
    try:
        response = requests.get(url=url,timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    data = fetch_api_data(api_url)
    if data:
        print(data["data"]["data"])