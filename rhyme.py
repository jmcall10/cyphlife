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


def word_association(topic):
    response = requests.get('https://api.datamuse.com/words?rel_jja=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("jja")
    print("---")
    print(topic.upper())
    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_jjb=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("jjb")
    print("---")
    print(topic.upper())

    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_syn=' + topic + '&max=6')
    json_response = json.loads(response.text)
    print("syn")
    print("---")
    print(topic.upper())
    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_trg=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("trg")
    print("---")
    print(topic.upper())
    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_ant=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("ant")
    print("---")
    print(topic.upper())
    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_spc=' + topic + '&max=6')
    json_response = json.loads(response.text)
    print("spc")
    print("---")
    print(topic.upper())

    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_gen=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("gen")
    print("---")
    print(topic.upper())
    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_com=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("com")
    print("---")
    print(topic.upper())
    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_par=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("par")
    print("---")
    print(topic.upper())
    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_bga=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("bga")
    print("---")
    print(topic.upper())

    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_bgb=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("bgb")
    print("---")
    print(topic.upper())
    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_rhy=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("rhy")
    print("---")
    print(topic.upper())
    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_nry=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("nry")
    print("---")
    print(topic.upper())
    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_hom=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("hom")
    print("---")
    print(topic.upper())

    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])
    response = requests.get('https://api.datamuse.com/words?rel_cns=' + topic + '&max=3')
    json_response = json.loads(response.text)
    print("cns")
    print("---")
    print(topic.upper())
    for data in json_response:
        print("     " + data['word'])
        time.sleep(1)
        #practice_loop(data['word'])

        
    

print(" ")
#topic = input("Enter topic: ")
#print("Topic is: " + topic)
#api_url = 'https://api.datamuse.com/words?rel_rhy=' + topic + '&max=10'
word_association('plant')
#use_requests(api_url)
time.sleep(1)
#api_url = 'https://api.datamuse.com/words?ml=' + topic + '&max=10'
#use_requests(api_url)
#use_requests(api_url)

#poem from a picture

#shuffle prompts? cyph life

#poem app where daily u have a prompt to make a poem
