#===================================================================
import json
import requests

inference_url = 'https://api.wikimedia.org/service/lw/inference/v1/models/enwiki-articlequality:predict'
headers = {
    'Content-Type': 'application/json',
}
data = {"lang": "en", "rev_id":  123456789}
response = requests.post(inference_url, headers=headers, data=json.dumps(data))
print(response.text)
#===================================================================
