"""
Author: Nick Baron 830278807
Description: This is a set of helper methods that can be used for a variety of purposes.
"""

def get_keys(keyFileName, numberKeys = 8):
    """
    This functions retrieves key_file from a file.
    :param keyFileName: This is the filename that is supposed to contain the key_file.
    :param numberKeys: This is the number of key_file that are being requested for encryption.
    :return: This is a bytes array that contains the key_file.
    """
    keys = read_file(keyFileName)

    if len(keys) > numberKeys:
        print("[WARNING] Found more than " + str(numberKeys) + " key_file.")
        print("[NOTICE] Using " + str(numberKeys) + " key_file.")
    elif len(keys) < numberKeys:
        print("[WARNING] Found less than " + str(numberKeys) + " key_file.")
        print("[NOTICE] Using " + str(len(keys)) + " key_file.")
    elif len(keys) == 0:
        print("[ERROR] Key file found to be empty. Cannot continue.")
        exit(1)

    return keys[:numberKeys]


def read_file(file, debug=False):
    """
    This functions reads bytes arrays from the fiven file.
    :param file: This is the file that is to be read from.
    :return: This is the bytes array containing all the information from the file.
    """
    if debug:
        print("[LOG] Reading file: " + file)

    try:
        f = open(file, "rb") #read bytes
        retStr = f.read()
        f.close()
    except:
        print("[ERROR] Cannot open file: " + file)
        exit(1)

    return retStr


def write_file(file, string, debug=False):
    """
    This functions writes bytes array back to a file.
    :param file: This is the file name that is to be written to.
    :param string: This is the information that is to be written to the file.
    :return: Nothing useful.
    """
    if debug:
        print("[LOG] Writing file: " + file)

    try:
        f = open(file, "wb") #write bytes
        f.write(string)
        f.close()
    except:
        print("[ERROR] Cannot write file: " + file)
        exit(1)

def big_endian_ip(ip_string):
    """
    This function calculates a big endian form IP address from a string.
    :param ip_string: This is an input string that contains an IP address in the form of: "192.168.1.104"
    :return: This returns a bytearray of the big endian information.
    """
    ip_string_arr = ip_string.split(".")
    if not len(ip_string_arr) == 4:
        print("[ERROR] Invalid IP: " + str(ip_string))
        exit(1)
    big_endian = bytearray()
    for i in range(3, -1, -1):
        big_endian.append(int(ip_string_arr[i]))

    return big_endian

def ones_add(a, b):
    """
    This function adds two 16 bit numbers and returns a 16 bit number that has any overflow added back in.
    :param a: This is an int.
    :param b: This is a bytearray of length 2.
    :return: This is a 16 bit integer.
    """
    b = (b[0] << 8) + b[1]
    ret_int = a + b
    while ret_int > 0xffff:
        remainder = ret_int >> 16
        ret_int = (ret_int & 0xffff) + remainder
    return ret_int

def check_sum(packet, compliment = True):
    """
    This function calulates a check sum of a passed packet.
    :param packet: This is a bytearray of even length.
    :param compliment: This is parameter that if TRUE will make the output the compliment of its self.
    :return: This is the final checksum of the packet.
    """
    checksum = 0
    for i in range(0, len(packet), 2):
        checksum = ones_add(checksum, packet[i:i + 2])
    if compliment:
        checksum = checksum ^ 0xffff
    return checksum