import sys
import logging
import logging.config

class MyClass:
  VAR = 10
  def __init__(self):
    self.id = 100

  def __str__(self):
    return 'MyClass(id={})'.format(self.id)

def funct():
  return MyClass()

try:
  my_class = funct()
except:
  print 'Exception!'
  raise

print 'my_class.VAR = {}'.format(my_class.VAR)
print 'my_class={}'.format(my_class)
print 'VAR = {}'.format(VAR)
