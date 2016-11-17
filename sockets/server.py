import sys
import logging
import logging.config
import socket
import threading

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(sys.argv[0])

HOST = '0.0.0.0'
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

class CommunicatorThread(threading.Thread):
  def __init__(self, threadId, threadName, communicator):
    threading.Thread.__init__(self)
    self.threadId = threadId
    self.threadName = threadName
    self.communicator = communicator
    self.logger = logging.getLogger("CommunicatorThread") 
    self.logger.debug('Initialized CommunicatorThread(threadId={}, threadName={})'.format(threadId, threadName))

  def __receive(self):
    """
    Receives messages via communicator. This is the blocking call
    Returns (data, should_stop) 
    """
    try:
      data, is_last_msg = self.communicator.receive()
      if is_last_msg:
        self.logger.debug('Received the last message, closing communicator and ending the thread')
        self.communicator.close()
      return (data, is_last_msg)
    except:
      self.logger.error('Unable to read from the communicator, closing it and accepting another connection')
      self.communicator.close()
      return (None, True)

  def __send(self, data):
    """
    Sends data via communicator
    Returns true if the interaction should continue, false otherwise
    """
    try:
      self.communicator.send(data)
    except:
      self.logger.error('Unable to send data [{}], closing connection', data)
      self.communication.close

  def run(self):
    self.logger.debug('Starting the CommunicatorThread(threadId={}, threadName={})'.format(self.threadId, self.threadName))
    while True:
      data, should_stop = self.__receive()
      if should_stop:
        break
      should_stop = self.__send(data)
      if should_stop:
        break

    self.logger.debug('Finished the CommunicatorThread(threadId={}, threadName={})'.format(self.threadId, self.threadName))

def accept_connections_and_interact(socket):
  thread_count = 0
  while True:
    thread_count = thread_count + 1
    communicator = Communicator(accept_and_get_msg_socket(socket))
    thread = CommunicatorThread(thread_count, 'CommnicatorThread-{}'.format(thread_count), communicator)
    thread.start()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bind_safely(socket)
listen_safely(socket)
accept_connections_and_interact(socket)
close_safely(socket)
