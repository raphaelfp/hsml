""" Imports """
import json
import requests

SUBSCRIPTION_KEY = '58af56a3ae604019a01ebe3dbd5a330e'
URI_BASE = 'https://southcentralus.api.cognitive.microsoft.com'

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
