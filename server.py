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
# import urllib
# import urllib3
# import urllib.request
# from flask import request
# from httplib2 import HTTPConnectionWithTimeout
host = 'localhost'
data_payload = 16384

# def send_to_flask():

# def receive_from_socket():    
#   data, address = sock.recvfrom(data_payload) #recebe os dados processados pelo socket UDP
#   device_data = data.decode()
#   print ("received %s bytes from %s" % (len(data), address))
#   data_dict1 = json.loads(device_data1)
#   return device_data

# def send_to_flask(device_data):



def echo_server(port):
  """ A simple echo server """
  # Create a UDP socket
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  sock.setblocking(0)
  # sock.settimeout(0.5)
  # Bind the socket to the port
  server_address = (host, port)
  print ("Starting up echo server on %s port %s" % server_address)
  sock.bind(server_address)

  print("Servidor incializando\nIniciando modelagem de dados..." )

  # data, address = sock.recvfrom(data_payload)
  # device_data1 = data.decode()
  # print ("first response, received %s bytes from %s" % (len(data), address))
  # url = 'http://127.0.0.1:3000/pacientes'
  # # data = device_data1
  # post = requests.post(url, verify=False, json=device_data1)
  # print(post.status_code)

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
    # palavra_1 = []
    # palavra_1.append(device_data1)
    # json.loa
    # palavra_2 = []
    # palavra_2.append(device_data2)
    # device_data = data.decode() # decodifica a mensagem recebida como JSON
    print("device_data1", data_dict1['nome'])
    print("device_data2", data_dict2['nome'])
    print(type(data_dict1['nome']))
    # conn = HTTPConnection("localhost", 3000)
    # conn.putheader("content-length","512")
    # conn.endheaders()
    # print(type(device_data))
    # params = urllib.parse.urlencode({'oxigenacao': device_data},doseq=True)
    # headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    # data, address = sock.recvfrom(data_payload)
    # device_data2 = data.decode()
    url = 'http://127.0.0.1:3000/pacientes'
    
    # data = device_data
      # post = requests.post(url, verify=False, json=device_data2)
      # print("post status code = ",post.status_code)
      
    # post = requests.post(url, verify=False, json=device_data1)
    # print("post status code = ",post.status_code)

    if(data_dict2['nome'] != data_dict1['nome']):
      print('nao iguais')
      post = requests.post(url, verify=False, json=device_data2)
      print("post status code = ")
      print(post.status_code)
    elif(data_dict2['nome'] == data_dict1['nome']):
      print('iguais')
      put = requests.put(url, verify=False, json=device_data1) #tanto faz json=device_data1 ou 2 pois é o mesmo pacote
      print("put status code = ",put.status_code)
    # post = requests.post(url, verify=False, json=device_data)
    # print(post.status_code)

    # url = 'http://127.0.0.1:3000/pacientes'
    # data = device_data

    # url = 'http://127.0.0.1:3000/pacientes'
    # data = device_data
    # post = requests.post(url, verify=False, json=data)
    # print(post.status_code)

    # body = {'minha': device_data}
    # req = urllib.request.Request('http://127.0.0.1:3000/pacientes', headers={'User-Agent': 'Mozilla/5.0'})
    # req.add_header('Content type','application/json; charset=utf-8')
    # jsondata = json.dumps(body)
    # jsondataasbytes = jsondata.encode('utf-8')
    # req.add_header('Content-Length',len(jsondataasbytes))
    # response = urllib.request.urlopen(req,jsondataasbytes)

    # r =requests.get('https://127.0.0.1:3000/pacientes')
    # pload = {'username':'Olivia','password':'123'}
    # r = request.post('https://127.0.0.1:3000/pacientes',data = pload)
    # print(r.text)
    
    # response = urllib3.url
    # conn = HTTPConnection("localhost",3000)
    # conn.request("POST", "/pacientes", params, headers)
    # response = conn.getresponse()

    # conn.request("GET","/pacientes")
    # response = conn.getresponse()
    # conn.send(device_data.encode())
    
    # conn.putheader(
    # conn.send(device_data.encode())
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as httpsock:
      # httpsock.connect(("localhost", 5000))
      # httpsock.sendall(bytes("Hello" + "\n", "utf-8"))
      # httpsock.sendall(bytes(data))
    print("asdoaisdoa\n")
    # print(bytes(data))
    # print("Registrando os dados em um banco para comunicação com servidor HTTP...")
    # with open("./flask-api-2/BANCO_QUATRO.json",'w+') as file:
    #   # json.dump(device_data,file)
    #   file.write(data.decode())
    #   file.close()
    # HTTPConnection.putheader("Content-Length","512")
    # HTTPConnection.endheaders()
    # HTTPConnection.send(data)

    # with open("./node-api/BANCO_QUATRO.json",'w+') as file:
    #   file.write(data.decode())
    #   file.close()
      # with open("./express/BANCO_QUATRO.json",'w') as file:
      #   file.write(data.decode())
      # file.close()
    # separators=(',', ': ') isso aqui vai no json dump
    # print ("Data: %s" %data)  
    # if data:
    #   sent = sock.sendto(data, address)
    #   print ("sent %s bytes back to %s" % (sent, address))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Socket Server Example')
  parser.add_argument('--port', action="store", dest="port", type=int, required=True)
  given_args = parser.parse_args()
  port = given_args.port
  # echo_server(port)
  threaded_server = threading.Thread(target=echo_server)
  threaded_server.start()