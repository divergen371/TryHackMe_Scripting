import base64
import sys


encdata = open(sys.argv[1], 'r').read().replace('\n', '')

count = 0
while count < 5:
    encdata = base64.b16decode(encdata)
    count += 1

count = 0
while count < 5:
    encdata = base64.b32decode(encdata)
    count += 1

count = 0
while count < 5:
    encdata = base64.b64decode(encdata)
    count += 1


print(encdata)