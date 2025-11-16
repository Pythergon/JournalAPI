# Import the browser module and the ajax submodule
from browser import document, alert, ajax
import json

book = "john"
chapter = "3"

# API Details
BASE_URL = "https://api.rebuildingfaith.org"
ENDPOINT = f"/bible/text/{book}/{chapter}"
VERSION = "nkjv"
URL = f"{BASE_URL}{ENDPOINT}?ver={VERSION}"

# Authentication
access_token = "..." # Your token

headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json"
}

# 1. Define the function to handle a successful response
def on_complete(req):
    if req.status == 200 or req.status == 0:
        # Request was successful, req.text contains the response body
        try:
            data = json.loads(req.text)
            verses_list = data.get('verses')
            # For demonstration, you can see the data in the browser console
            print("Successfully retrieved data:")
            print(data)
            # You would update an element on the HTML page here
            # document['my_output_div'].text = data['verses'][0]['text']
        except json.JSONDecodeError:
            print("Error: Could not decode JSON response.")
    else:
        # Request failed (e.g., 401, 404, 500)
        print(f"HTTP Error: Status code {req.status}")
        print(req.text) # Print the error message from the server

# 2. Define the function to start the request
def get_bible_text():
    # Make the asynchronous GET request
    # 'complete' is the event handler for when the request finishes
    req = ajax.ajax()
    req.bind('complete', on_complete)
    try:
        req.open('GET', URL, False) # The 'False' means the request is SYNCHRONOUS
        # NOTE: For proper browser practice, you should use True (asynchronous)
        # and handle the response in the 'on_complete' function.
        # However, Brython sometimes defaults to synchronous for simplicity.
        for header, value in headers.items():
            req.set_header(header, value)
        req.send()

    except Exception as e:
        print(f"An unexpected error occurred during request setup: {e}")

# 3. Execute the function (e.g., when the script loads)
get_bible_text()
