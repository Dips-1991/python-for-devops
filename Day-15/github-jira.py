# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://patildipak0791.atlassian.net/rest/api/3/issue"

    API_TOKEN="ATATT3xFfGF0IxIFYK2DnBxDgEmApPkCwgjc8ETlKGNGp3IFDucez4H44sEkqHkb4AyJDTAKV1HCLvyvh9XxhbYDOcZyngBiwHenaQd0IHGnF2FwQBrj3PkqEIHyvQ_a1QKiECeq9mTfKM0AbPlTDCjLApqU42Q0DSHCQRWi9veDdPmJJZqdN_w=51F413BB"

    auth = HTTPBasicAuth("", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "AB"
        },
        "issuetype": {
            "id": "10006"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
