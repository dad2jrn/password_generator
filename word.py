import requests as req
from requests.exceptions import HTTPError

# class Words:
def getword():
    for url in ["https://random-word-api.herokuapp.com/word"]:
        try:
            response = req.get(url)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Some other error occurred: {err}")
        else:
            json_response = response.json()
            for myword in list(json_response):
                # print(myword)
                return myword


