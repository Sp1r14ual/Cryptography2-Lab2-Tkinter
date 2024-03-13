from itertools import cycle

def xor(message, key):
 return "".join([chr(ord(c) ^ ord(k)) for (c, k) in zip(message, cycle(key))])

