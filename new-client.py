#!/usr/bin/env python
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
import socket
import sys
import argparse
import json
import random
from faker import Faker
host = 'localhost'
data_payload = 16384

# A classe abaixo faz parte da simulação
class Patient:
  #Construtor
  def __init__(self):
    fake = Faker()
    self.first_name = fake.first_name()
    self.last_name = fake.last_name()
    self.oxigenacao = random.uniform(90,100)
    self.name = ""
    # self.name.append(self.first_name)
    # self.name.append(self.last_name)
    self.name = ''.join((self.first_name," ",self.last_name))

  def toJSON(self):
      return json.dumps(self, default=lambda o: o.__dict__, 
          sort_keys=True, indent=4)

  #cria um json para ser enviado
  def get_json(self):
    json_content = {
      'nome': self.name,
      'oxigenacao': self.oxigenacao
    }
    return json.dumps(json_content)

  #atualiza o JSON com valores de oxigenação diferentes
  def update_json(self):
    self.oxigenacao = random.uniform(90,100)
    json_content = {
      'oxigenacao': self.oxigenacao
    }
    return self.oxigenacao


def input_data(x):
  for i in range(0,x):
    patient = Patient()
    print(patient.get_json())
    # while True:
    patient.update_json()
    print(patient.get_json())
  return patient


def echo_client(port):
  """ A simple echo client """
  # Create a UDP socket
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  server_address = (host, port)
  print ("Connecting to %s port %s" % server_address)
  message = 'This is the message. It will be repeated.'

  try:
    # with open("client-data.json",'a') as jsonFile:
      # data = json.load(jsonFile)
    patient = Patient()
    data = patient.get_json()
    print(data)
  # user_encode_data = json.dumps(data, indent=2).encode('utf-8') # codifica o dictionary data em bytes para ser enviado
    # jsonFile.close()
    # print(type(data))
    print ("Sending encoded data")
    while True:
      patient.update_json()
      sent = sock.sendto(patient.toJSON().encode(), server_address)
  finally:
    print ("Closing connection to the server")
    sock.close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Socket Server Example')
  parser.add_argument('--port', action="store", dest="port", type=int, required=True)
  given_args = parser.parse_args()
  port = given_args.port
  echo_client(port)