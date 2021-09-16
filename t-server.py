import threading
import socket
import logging
import requests
import sys
import argparse
import json
import os
import requests
host = 'localhost'
data_payload = 16384

class MyThreadedServer():

  def __init__(self):
    logging.info('Inicializando servidor')
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, 8000)
    self.sock.bind(server_address)
    print("servidor ligado a %s na porta %s" % server_address)
    self.clients_list = []
    print("esperando por clientes")

  def talkToClient(self, ip):
    logging.info("Sending 'ok' to %s", ip)
    self.sock.sendto("ok", ip)

  # def talkToClient(self, ip):
  #   requests.post(url, verify=False, json=device_data)
  #   logging.info("Sending 'ok' to %s", ip)
  #   self.sock.sendto("ok", ip)

  def talkToFlask(self, client_address, data):
    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # data, client_address = client_socket.recvfrom(data_payload)
    # print("Foram recebidos %s dados de %s", (len(data), client_address))
    device_data = data.decode()
    url = 'http://127.0.0.1:3000/pacientes'
    print("enviando dados para o servidor Flask")
    post_r = requests.post(url, verify=False, json = device_data)
    print("POST req. status:", post_r.status_code)
    
  def listen_clients(self):
    while True:
      data, client_address = self.sock.recvfrom(data_payload)
      print("Foram recebidos %s dados de %s", (len(data), client_address))
      # msg, client = self.sock.recvfrom(data_payload)
      # logging.info('Received data from client %s: %s', client, msg)
      t = threading.Thread(target=self.talkToFlask, args=(client_address,data))
      # args=(client,)
      t.start()


if __name__ == '__main__':
  # Make sure all log messages show up
  logging.getLogger().setLevel(logging.DEBUG)
  t = MyThreadedServer()
  t.listen_clients()
