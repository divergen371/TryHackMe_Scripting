import socket
import hashlib
import sys

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)


def main():
    host = sys.argv[1]
    port = 4000
    server = (host, port)
    iv = b'secureiv1337'
    key = b'thisisaverysecretkey1337'

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.sendto(b'hello', server)
    print(recv(s))
    s.sendto(b'ready', server)
    data = recv(s)
    print(data)
    checksum = data[104:136].hex()

    while True:
        s.sendto(b'final', server)
        cText = bytes(recv(s))
        s.sendto(b'final', server)
        tag = bytes(recv(s))
        pText = decrypt(key, iv, cText, tag)
        if hashlib.sha256(pText).hexdigest() != checksum:
            continue
        else:
            print(f'The flag is: {pText}')
            break


def recv(s):
    try:
        data = s.recv(1024)
        return data
    except Exception as e:
        print(str(e))


def decrypt(key, iv, cText, tag):
    decryptor = Cipher(algorithms.AES(key), modes.GCM(iv, tag),
                       backend=default_backend()).decryptor()
    return decryptor.update(cText) + decryptor.finalize()


if __name__ == '__main__':
    main()


