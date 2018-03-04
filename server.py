import socket
import sys
from encrypt import encrypt
from decrypt import decrypt
from collections import deque
import datetime

if len(sys.argv) != 2:
    print("[ERROR] " + str(sys.argv[0]) + " Incorrect command line arguments.")
    exit(1)

que = deque(maxlen=5)
key_dic = {"127.0.0.1":"aeiouaei","10.10.4.1":"abcdefgh","10.10.2.2":"bcdefghi","10.10.3.2":"cdefghij","10.10.4.2":"defghijk","10.10.5.2":"efghijkl","10.10.6.2":"fghijklm"}

udp_port = int(sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', udp_port))

try:
    while True:
        print("[LOG] Waiting to receive.")
        data, address = sock.recvfrom(4096)
        print("[LOG] Message Received.")
        quedata = bytearray(datetime.datetime.now().strftime("%H:%M:%S.%f") + " " + str(address[0]) + " ", "utf-8")
        key = bytes(key_dic[str(address[0])], "utf-8")
        quedata += decrypt(key, data)
        print(str(quedata)[12:-2])
        que.append(encrypt(key, quedata))
        print("[LOG] Replying:")
        for i in range(0, len(que)):
            sock.sendto(que[i], address)
            print(str(que[i])[12:-2])
finally:
    sock.close()
