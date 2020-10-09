import socket
import time
import sys
import re

def Main():
    serverIP   = sys.argv[1]
    serverPort = 1337
    startNum = 0

    while serverPort != 9765:
        try:
            if serverPort == 1337:
                print(f"Connecting to {serverIP} waiting for port {serverPort} to become available.")

