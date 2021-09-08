#!/usr/bin/env python
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
import socket
import sys
import argparse
import json
host = 'localhost'
data_payload = 16384

# data_set = {"key1": [1, 2, 3], "key2": [4, 5, 6]}
# json_dump = json.dumps(data_set)
# jsonResult = {"first":"You're", "second":"Awsome!"}
# jsonResult = json.dumps(jsonResult)

def echo_client(port):
  """ A simple echo client """
  # Create a UDP socket
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  server_address = (host, port)
  print ("Connecting to %s port %s" % server_address)
  message = 'This is the message. It will be repeated.'

  try:
    # Send data
    # data_set = {"key1": [1, 2, 3], "key2": [4, 5, 6]}
    # json_dump = json.dumps(data_set)
    with open("MOCK_DATA.json") as jsonFile:
      data = json.load(jsonFile)
      # data_to_send = json.loads(data)
      # data_to_send = ''.join(data)
      user_encode_data = json.dumps(data, indent=2).encode('utf-8')
      jsonFile.close()
    print(type(data))
    # message = "Test message. This will be echoed"
    # print(type(jsonObject))  
    print ("Sending MOCK_DATA.json")
    sent = sock.sendto(user_encode_data, server_address)
    # print(data)
    # sent = sock.sendto(data,server_address)
    # Receive response
    # data, server = sock.recvfrom(data_payload)
    # print ("received %s" % data)
  finally:
    print ("Closing connection to the server")
    sock.close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Socket Server Example')
  parser.add_argument('--port', action="store", dest="port", type=int, required=True)
  given_args = parser.parse_args()
  port = given_args.port
  echo_client(port)