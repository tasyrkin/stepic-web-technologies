import sys
import logging
import logging.config
import socket

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(sys.argv[0])

HOST = 'localhost'
PORT = 2222
LISTEN_QUEUE_SIZE = 10

def close_safely(socket):
  logger.debug('Closing the socket [{}]'.format(socket))
  try:
    socket.close()
  except:
    print 'Unable to close socket [{}]: {}'.format(socket, sys.exc_info()[0])
    raise
  logger.debug('Successfully closed the socket [{}]'.format(socket))

def bind_safely(socket):
  logger.debug('Trying to bind the socket on host [{}:{}]'.format(HOST, PORT))
  try:
    socket.bind((HOST, PORT))
  except:
    logger.error('Unable to bind a socket on host [{}:{}]: {}'.format(HOST, PORT, sys.exc_info()[0]))
    close_safely(socket)
    raise 
  logger.debug('Successfully bound the socket on host [{}:{}]'.format(HOST, PORT))

def listen_safely(socket):
  logger.debug('Trying to listen the socket on host [{}:{}]'.format(HOST, PORT))
  try:
    socket.listen(LISTEN_QUEUE_SIZE)
  except:
    logger.error('Unable to listen the socket on host [{}:{}]: {}'.format(HOST, PORT, sys.exc_info()[0]))
    close_safely(socket)
    raise 
  logger.debug('Successfully listening the socket on host [{}:{}]'.format(HOST, PORT))

def accept_and_get_msg_socket(socket):
  try:
    msg_socket = None
    msg_socket, address = socket.accept() 
  except:
    logger.error('Unable to accept socket on [{}:{}]: {}'.format(HOST, PORT, sys.exc_info()[0]))
    if msg_socket is not None:
      close_safely(msg_socket)
    close_safely(socket)
    raise
  return msg_socket

class Communicator:
  BUFFER_SIZE = 1024
  STOP_MSG = 'close'
  
  def __init__(self, msg_socket):
    self.msg_socket = msg_socket
    self.logger = logging.getLogger('Communicator')
    self.logger.debug('Created communicator with the socket [{}]'.format(self.msg_socket))

  def receive(self):
    """
    Receives data from the msg_socket.
    In case of error rethrows the original exception
    Returns (data, is_last_msg)
    """
    try:
      msg = self.msg_socket.recv(self.BUFFER_SIZE)
      self.logger.debug('Received msg of size [{}]: [{}]'.format(len(msg), msg))
    except:
      self.logger.error('Unable to read from msg_socket [{}]: {}'.format(self.msg_socket, sys.exc_info()[0]))
      raise
    return (msg, msg == self.STOP_MSG or len(msg) == 0)

  def send(self, msg):
    """
    Sends data to the msg_socket
    In case of error rethrows the original exception
    Returns number of sent bytes
    """
    sent_bytes = 0
    while len(msg) != sent_bytes:
      try:
        sent_bytes += self.msg_socket.send(msg[sent_bytes:])
      except:
        self.logger.error('Unable to send to msg_socket [{}], bytes sent [{}], total bytes [{}]: {}'.format(self.msg_socket, sent_bytes, len(msg), sys.exc_info()[0]))
        raise
    return sent_bytes

  def close(self):
    close_safely(self.msg_socket)

def accept_connections_and_interact(socket):
  while True:
    communicator = Communicator(accept_and_get_msg_socket(socket))
    while True:
      try:
        data, is_last_msg = communicator.receive()
        if is_last_msg:
          logger.debug('Received the last message, accepting another connection')
          communicator.close()
          break
      except:
        logger.error('Unable to read from the communicator, closing it and accepting another connection')
        communicator.close()
        break
      try:
        communicator.send(data)
      except:
        logger.error('Unable to send data [{}], closing connection', data)
        communication.close

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bind_safely(socket)
listen_safely(socket)
accept_connections_and_interact(socket)
close_safely(socket)
