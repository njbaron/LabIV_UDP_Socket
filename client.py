from encrypt import encrypt
from decrypt import decrypt
from helpers import read_file
import sys
import socket

if len(sys.argv) != 5:
    print("[ERROR] " + str(sys.argv[0]) + " Incorrect command line arguments")
    exit(1)

udp_ip = sys.argv[1]
udp_port = int(sys.argv[2])
keys = bytearray(sys.argv[3], "utf-8")
message = encrypt(keys, read_file(sys.argv[4]))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)

try:
    print("[LOG] Sending infromation.")
    sock.sendto(message, (udp_ip, udp_port))
    while True:
        print("[LOG] Waiting for response.")
        try:
            data, address = sock.recvfrom(4096)
        except:
            print("[LOG] Reciever Timed Out")
            exit(0)
        print("[LOG] Response Timed Out")
        print(str(decrypt(keys, data))[12:-2])
finally:
    sock.close()
