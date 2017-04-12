import nexmo
import urllib
from appConfig import NEXMO_KEY, NEXMO_SECRET, nexmoNumber

#send SMS message to contact   
# *need to use http1.1 in order to send batch SMS   
def sendSMS(contact):
        params = {
            'api_key': NEXMO_KEY,
            'api_secret': NEXMO_SECRET,
            'to': contact,
            'from': nexmoNumber,
            'text': 'Random facts are not all that random.'
        }

        url = 'https://rest.nexmo.com/sms/json?' + urllib.parse.urlencode(params)

        request = urllib.request.Request(url)
        request.add_header('Accept', 'application/json')
        response = urllib.request.urlopen(request)
        print(response)

        response = None

def main():

    contacts = []
    
    #store numbers in list from contactBook.txt
    contacts = open("contactBook.txt", 'r').read().splitlines()

    for contact in contacts:
         sendSMS(contact)

if __name__ == '__main__':
    main()
