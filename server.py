import zmq
import requests

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print("Waiting to request...")

while True:
    socket.recv()
    print('Fetching a random word...\n')
    url = "https://wordsapiv1.p.rapidapi.com/words/"

    headers = {
        "X-RapidAPI-Key": "035af51e50msh68d685ccdc16360p1b9a49jsn767069945ef4",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }

    querystring = {"random": "true"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.json()
    print(result["word"])

    while "results" not in result:
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.json()
        print(result["word"])

    parse_word = result["word"]
    print(f'Random word is {parse_word}.')
    socket.send_string(parse_word)
    print('Random word sent to client...\n')