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
import abc
from http.client import HTTPConnection
# import urllib
# import urllib3
import urllib.request
from flask import request
import requests
# from httplib2 import HTTPConnectionWithTimeout
host = 'localhost'
data_payload = 16384

def echo_server(port):
  """ A simple echo server """
  # Create a UDP socket
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  # Bind the socket to the port
  server_address = (host, port)
  print ("Starting up echo server on %s port %s" % server_address)
  sock.bind(server_address)

  print("Servidor incializando\nIniciando modelagem de dados..." )

  while True:
    print ("Waiting to receive message from client")
    data, address = sock.recvfrom(data_payload) #recebe os dados processados pelo socket UDP
    print ("received %s bytes from %s" % (len(data), address))
    device_data = data.decode() # decodifica a mensagem recebida como JSON
    print(device_data)
    # conn = HTTPConnection("localhost", 3000)
    # conn.putheader("content-length","512")
    # conn.endheaders()
    print(type(device_data))
    # params = urllib.parse.urlencode({'oxigenacao': device_data},doseq=True)
    # headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    
    url = 'http://127.0.0.1:3000/pacientes'
    data = device_data
    r = requests.post(url, verify=False, json=data)
    print(r.status_code)

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
  echo_server(port)
  