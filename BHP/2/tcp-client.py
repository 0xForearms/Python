#!/usr/bin/env python3

#just a simple TCP client

import socket

target_host = "127.0.0.1"
target_port = 9999

#Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host, target_port))

#Send some data
client.send(b"ABCDEF")

#receive some data
response = client.recv(4096)

client.close()

print(response)
