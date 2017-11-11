""" Imports """
import json
import requests

SUBSCRIPTION_KEY = '8c8a3081ded0455e81a3c0f3a471a57c'
URI_BASE = 'https://westcentralus.api.cognitive.microsoft.com'

HEADERS = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
}

PARAMS = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'gender',
}


def get_attributes(filename):
    file = open(filename, 'rb')
    data = file.read()
    try:
        response = requests.request(
            'POST', URI_BASE + '/face/v1.0/detect', data=data, headers=HEADERS, params=PARAMS)

        #print('Response:')
        parsed = json.loads(response.text)
        #print(json.dumps(parsed, sort_keys=True, indent=2))
        return parsed[0]

    except Exception as ex:
        print('Error:')
        print(ex)
        return ""
    file.close()
