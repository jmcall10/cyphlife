import json
import os
import webbrowser
import time

import requests


topic = input("Enter topic: ")
print("Topic is: " + topic)
api_url = 'https://api.datamuse.com/words?rel_rhy=' + topic + '&max=10'

def use_requests(api_url):

    response = requests.get(api_url)
    json_response = json.loads(response.text)


    for data in (json_response):
        print(data['word'])
    #for count, data in enumerate(json_response):
    #    while count < 10:
    #        print(count, data['word'] + '....' )
    #        count=count+1
        
    #print(a = json_response[1])
    #print(b = json_response[2])
    #print(c = json_response[3])
    #print(d = json_response[4])
    #webbrowser.open_new_tab(photo_url)

    return

use_requests(api_url)
time.sleep(5)
api_url = 'https://api.datamuse.com/words?ml=' + topic
#use_requests(api_url)
use_requests(api_url)
