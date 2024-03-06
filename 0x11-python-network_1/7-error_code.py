import requests
import sys

def display_response_body(url):
    try:
        response = requests.get(url)
        # Check if response status code is >= 400
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if URL is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    display_response_body(url)

