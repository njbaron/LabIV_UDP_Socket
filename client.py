from encrypt import encrypt
from decrypt import decrypt
from helpers import read_file
from helpers import get_keys
import sys
import socket

print("Welcome to the UDP ECHO client!")

if len(sys.argv) != 5:
    print("[ERROR] " + str(sys.argv[0]) + " Incorrect command line arguments")
    exit(1)

udp_ip = sys.argv[1]
udp_port = int(sys.argv[2])
keys = get_keys(sys.argv[3])
message = encrypt(keys, read_file(sys.argv[4]))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (udp_ip, udp_port)
sock.settimeout(1)

try:
    print("[LOG] Sending information to", server_address[0], server_address[1])
    sock.sendto(message, server_address)
    while True:
        print("[LOG] Waiting for response.")
        data, address = sock.recvfrom(4096)
        print("[LOG] Response received from", address[0], address[1])
        print(str(decrypt(keys, data))[12:-2])
except:
    print("[WARNING] Receiver Timed Out.")
finally:
    sock.close()
