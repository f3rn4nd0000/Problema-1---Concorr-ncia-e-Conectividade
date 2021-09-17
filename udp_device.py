import socket
import sys
import argparse
import json
import random
import time
from faker import Faker
import patient

class UDPClient:
  ''' A simple UDP Client '''
  def __init__(self, host, port):
    self.host = host    # Host address
    self.port = port    # Host port
    self.sock = None    # Socket

  def configure_client(self):
    ''' Configure the client to use UDP protocol with IPv4 addressing '''
    # create UDP socket with IPv4 addressing
    print('Criando socket UDP/IPv4...')
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket criado')

  def interact_with_server(self):
    ''' Envia requisição ao servidor UDP... '''
    try:
        print("Conectando-se a %s porta %s" % (self.host, self.port))
        #instancia e atribui dados gerados na classe Patient a variável device_data
        device_data = patient.Patient()
        # envia dados ao servidor UDP
        while True:
          self.sock.sendto(device_data.get_json().encode(), (self.host, self.port))
          print(device_data.get_json())
          device_data.update_json()
          time.sleep(5)
        # resp, server_address = self.sock.recvfrom(1024)
    except OSError as err:
      print(err)
    finally:
      # close socket
      print('Fechando conexão com servidor UDP...')
      self.sock.close()

def main():
  ''' Create a UDP Client, send message to a UDP Server and receive reply. '''
  udp_client = UDPClient('127.0.0.1', 8000)
  udp_client.configure_client()
  udp_client.interact_with_server()

if __name__ == '__main__':
    main()