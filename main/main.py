# Handle the verse getting on the python side

import requests
import json

book = "romans"
chapter = "6"

# API Details
BASE_URL = "https://api.rebuildingfaith.org"
ENDPOINT = f"/bible/text/{book}/{chapter}"
VERSION = "nkjv"
URL = f"{BASE_URL}{ENDPOINT}?ver={VERSION}"

# Authentication
access_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6InNpZ25pbmcta2V5LTAxIiwidHlwIjoiSldUIn0.eyJzdWIiOiI2OGI3N2YyOTkzNWM4MDQyNmY0NTc2NmMiLCJzaWQiOiI2OTEzOTJiZDU3NjQ4YWYzODgwZTgwNzYiLCJkZXZpY2VfaWQiOiJhNzI5OTAxZC1lOWI3LTQxMGEtYWU4OS1lZjMzYzllYjA0MjciLCJ0aWQiOiI2N2E5MjAyYzMzMWNmNWU1MmM4ZDY1ZjIiLCJhenAiOiI2N2E5MjY3NzMzMWNmNWU1MmM4ZDY1ZjYiLCJqdGkiOiIwN2EzYWY4My0xZDhkLTRlMTgtOTNiNy05OWVlOWJmMTZhYjEiLCJpYXQiOiIxNzYyODkwNDgyIiwic2NvcGUiOlsib3BlbmlkIiwicHJvZmlsZSIsIm9mZmxpbmVfYWNjZXNzIl0sInRva2VuX3VzZSI6IkFUIiwiZXhwIjoxNzYyODk0MDgyLCJpc3MiOiJodHRwczovL2F1dGgucmVhbHNpbXBsZWF1dGguY29tIiwiYXVkIjoiaHR0cHM6Ly9yZWJ1aWxkaW5nZmFpdGgub3JnIn0.4YGR056pwsH-FVjZ-vxWlkf9VLpq0GgNHQ91o5wcyeGHnRCzhalCaWWp0H2ZN6BeJoLKNzFoZOk2bY1qou6eDFRpl7fswsru0VE5CzQtKvEgQ_L7uYf8v76ebsewAB94Z6EShXt4fPiKcQQsw35j4q-ue8vBDUU4dhhJEgK_WwFa7pEXrNL-IeqZK56aymI6r4CEn5h_Q2CR0adP5tk8CoenIjMH3TbdLy_vjU8lbEr9oEzWoBOmdtOyicE84O2X-C9XUKjB-gau3YwfXR64PP7QLGcYGzzz7-ojyYOKbSaxT0vtc6HzOBaqn2AlQMVTB3gRE3jGjF57COJcCTjRqg"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json"
}

# Clear the JSON file
with open('jsondata.json', 'w') as f:
    pass

try:

    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    data = response.json()

    verses_list = data['verses']

    userInput = input("Input your desired verse")

    for item in verses_list:
        if item['r'] == userInput:
            raw_verse_text = item['t']
            verse_text = raw_verse_text.replace('*r', '')
            break

    print(data)
    print(verse_text)

    with open('jsondata.json', 'w') as jsonFile:
        json.dump(data, jsonFile, indent=4)

except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"An unexpected error occurred: {err}")

