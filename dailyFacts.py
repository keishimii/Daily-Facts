import nexmo
import urllib
from appConfig import NEXMO_KEY, NEXMO_SECRET, testNumber1, contact1

params = {
    'api_key': NEXMO_KEY,
    'api_secret': NEXMO_SECRET,
    'to': contact1,
    'from': testNumber1,
    'text': 'Random facts are not all that random.'
}

url = 'https://rest.nexmo.com/sms/json?' + urllib.parse.urlencode(params)

request = urllib.request.Request(url)
request.add_header('Accept', 'application/json')
response = urllib.request.urlopen(request)