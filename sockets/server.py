import socket
import sys
import logging


logging.basicConfig(filename='example.log',level=logging.DEBUG)

HOST = 'localhost'
PORT = 2222

def bind_safely(socket):
  try:
    socket.bind((HOST, PORT))
  except:
    print 'Unable to bind a socket on host [{}] and port [{}]: {}'.format(HOST, PORT, sys.exc_info()[0])
    socket.close()
    raise 

def close_safely(socket):
  try:
    socket.close()
  except:
    print 'Unable to close socket for host [{}] and port [{}]: {}'.format(HOST, PORT, sys.exec_info()[0])
    raise

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bind_safely(socket)
close_safely(socket)
