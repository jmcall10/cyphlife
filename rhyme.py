import json
import os
import webbrowser
import time

import requests




def use_requests(api_url):

    response = requests.get(api_url)
    json_response = json.loads(response.text)

    for data in (json_response):
        print("" + (data['word'].upper()) + " / score: " + str(data['score']))
        api_url = 'https://api.datamuse.com/words?ml=' + data['word'] + '&max=4'
        response = requests.get(api_url)
        json_response = json.loads(response.text)
        for data in json_response:
            print("     related word: " + data['word'].upper())


        #time.sleep(1)
        #print(json_response)
    #for count, data in enumerate(json_response):
    #    while count < 10:
    #        print(count, data['word'] + '....' )
    #        count=count+1
        
    #print(a = json_response[1])
    #print(b = json_response[2])
    #print(c = json_response[3])
    #print(d = json_response[4])
    #webbrowser.open_new_tab(photo_url)

    return json_response

topic = input("Enter topic: ")
print("Topic is: " + topic)
api_url = 'https://api.datamuse.com/words?rel_rhy=' + topic + '&max=10'

use_requests(api_url)
time.sleep(1)
#api_url = 'https://api.datamuse.com/words?ml=' + topic + '&max=10'
#use_requests(api_url)
#use_requests(api_url)

#poem from a picture

#shuffle prompts? cyph life

#poem app where daily u have a prompt to make a poem
