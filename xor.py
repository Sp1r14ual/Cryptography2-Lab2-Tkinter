from itertools import cycle
from random import randint
def random_key(length):
 result = str()
 for i in range(length):
  result += str(randint(0, 1))
 return str(int(result, base=2))

def xor(message, key):
 return "".join([chr(ord(c) ^ ord(k)) for (c, k) in zip(message, cycle(key))])

