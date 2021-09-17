#!/usr/bin/env python
# This program is optimized for Python 2.7.12
# and Python 3.5.2.
# It may run on any other version with/without modifications.
import socket
import sys
import argparse
import json
from multiprocessing import Pool
import os
from http.client import HTTPConnection
import threading
import requests
host = 'localhost'
data_payload = 16384

def configure_server():
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  # sock.setblocking(0)
  # sock.settimeout(0.5)
  # Bind the socket to the port
  server_address = (host, 8000)
  print ("Starting up echo server on %s port %s" % server_address)
  sock.bind(server_address)
  return sock

def send_requests():
  
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  # sock.setblocking(0)
  # sock.settimeout(0.5)
  # Bind the socket to the port
  server_address = (host, 8000)
  print ("Starting up echo server on %s port %s" % server_address)
  sock.bind(server_address)
  
  while True:
    print ("Waiting to receive message from client")
    data, address = sock.recvfrom(data_payload)
    device_data = data.decode()
    data_dict = json.loads(device_data)
    print ("received %s bytes from %s" % (len(data), address))    
    url = 'http://127.0.0.1:3000/pacientes'
    post_r = requests.post(url, verify=False, json=device_data)
    print("post status code = ")
    print(post_r.status_code)  

def echo_server(port):
  """ A simple echo server """
  # Create a UDP socket
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  # sock.setblocking(0)
  # sock.settimeout(0.5)
  # Bind the socket to the port
  server_address = (host, port)
  print ("Starting up echo server on %s port %s" % server_address)
  sock.bind(server_address)

  print("Servidor incializando\nIniciando modelagem de dados..." )

  while True:
    print ("Waiting to receive message from client")
    data, address = sock.recvfrom(data_payload)
    device_data1 = data.decode()
    print ("received %s bytes from %s" % (len(data), address))
    
    data, address = sock.recvfrom(data_payload) #recebe os dados processados pelo socket UDP
    device_data2 = data.decode()
    print ("received %s bytes from %s" % (len(data), address))
    
    data_dict1 = json.loads(device_data1)
    data_dict2 = json.loads(device_data2)
    print("device_data1", data_dict1['nome'])
    print("device_data2", data_dict2['nome'])
    print(type(data_dict1['nome']))

    url = 'http://127.0.0.1:3000/pacientes'
    
    if(data_dict2['nome'] != data_dict1['nome']):
      print('nao iguais')
      post = requests.post(url, verify=False, json=device_data2)
      print("post status code = ")
      print(post.status_code)
    elif(data_dict2['nome'] == data_dict1['nome']):
      print('iguais')
      put = requests.put(url, verify=False, json=device_data1) #tanto faz json=device_data1 ou 2 pois é o mesmo pacote
      print("put status code = ",put.status_code)
    print("asdoaisdoa\n")

if __name__ == '__main__':
  # parser = argparse.ArgumentParser(description='Socket Server Example')
  # parser.add_argument('--port', action="store", dest="port", type=int, required=True)
  # given_args = parser.parse_args()
  # port = given_args.port
  # echo_server(port)
  # threaded_server = threading.Thread(target=configure_server())
  # threaded_server.start()

  threaded_request = threading.Thread(target=send_requests())
  threaded_server.start()