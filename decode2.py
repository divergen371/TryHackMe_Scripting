from base64 import *
import sys

encdata = open(sys.argv[1], 'r').read().replace('\n', '')

for x in range(50):
    encdata = b64decode(encdata)

print(encdata)
