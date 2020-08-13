#import
import requests
from pprint import pprint

#loop
def loop():
    while True:
        username = input('What is the username?: ')
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        status_code = response.status_code
        if status_code == 200:
            user_data = response.json()
            pprint(user_data)
            #question
            again = input('Do you want to continue? yes/no: ')
            if again == 'yes':
                continue
            elif again == 'no':
                break
        elif status_code >= 400:
            print('Try again')
loop()
