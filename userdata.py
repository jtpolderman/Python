#import
import requests
from pprint import pprint

print("Hi, welcome to Github userinfo scraper!")
#loop
def loop():
    while True:
        username = input('What is the username?: ')
        url = f"https://api.github.com/users/{username}"
        user_data = requests.get(url).json()
        if len (username) < 3:
            print ('Username must be at least 3 characters')
            pass
        if len (username) > 3:
            pprint (user_data)
        question()

#continue
def question():
    import sys
    while True:
        again = input('Do you want to continue? yes/no: ')
        if again == 'yes':
            return loop()
        elif again == 'no':
            print("Bye!")
            sys.exit()
loop()
