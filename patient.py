import socket
import sys
import argparse
import json
import random
import time
from faker import Faker

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
          sort_keys=True)

  #cria um json para ser enviado
  def get_json(self):
    json_content = {
      'nome': self.name,
      'oxigenacao': self.oxigenacao
    }
    return json.dumps(json_content)

  def get_name(self):
    json_content = {
      'nome': self.name,
    }
    return json.dumps(json_content)  

  #atualiza o JSON com valores de oxigenação diferentes
  def update_json(self):
    self.oxigenacao = random.uniform(90,100)
    json_content = {
      'oxigenacao': self.oxigenacao
    }
    # print(self.oxigenacao)
    return json.dumps(json_content)

  def get_oxigenacao(self):
    return json.dumps(self.oxigenacao)

def input_data(x):
  for i in range(0,x):
    patient = Patient()
    print(patient.get_json())
    # while True:
    patient.update_json()
    print(patient.get_json())
  return patient