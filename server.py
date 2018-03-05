import socket
import sys
from encrypt import encrypt
from decrypt import decrypt
from collections import deque
import datetime

print("Welcome to the UDP ECHO server!")

if len(sys.argv) != 2:
    print("[ERROR] " + str(sys.argv[0]) + " Incorrect command line arguments.")
    exit(1)

que = deque(maxlen=5)
key_dic = {"127.0.0.1":"aeiouaei","10.10.4.1":"abcdefgh","10.10.6.1":"bcdefghi","10.10.5.1":"cdefghij","10.10.3.1":"defghijk","10.10.2.1":"fghijklm"}

udp_port = int(sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', udp_port))

try:
    while True:
        print("[LOG] Waiting to receive.")
        data, address = sock.recvfrom(4096)
        print("[LOG] Message Received from", address[0], address[1])
        try:
            quedata = bytearray(datetime.datetime.now().strftime("%H:%M:%S.%f") + " " + str(address[0]) + " ", "utf-8")
            key = bytes(key_dic[str(address[0])], "utf-8")
            quedata += decrypt(key, data)
            print(str(quedata)[12:-2])
            que.append(quedata)
            print("[LOG] Replying to", address[0], address[1])
            for i in range(0, len(que)):
                sock.sendto(encrypt(key, que[i]), address)
                print(str(que[i])[12:-2])
        except:
            print("[ERROR] Received information from", address[0], address[1], "with no key!")
finally:
    sock.close()
