ECE 456 UDP Socket Server/ Client Lab4
by Nick Baron 830278807

You need to have python3!

Note: You must have the server running before the client will be able to send information. This read me will describe how to run the client before setting up
the server because the server need infromation about the client before it will run properly.

How to run the Client:
	-Once the zip file has been extracted move client.py and a copy of encrypt.py, decrypt.py, and helpers.py onto the client machine.
	-Using ifconfig or ipconfig get the ipv4 ip of the client machine and save it for later.

	-Move onto reading about how to run the server for now. We will come back to this point later.

	-create a file in the same directory as client.py named keys.txt in it add the key string that you added to the dictionary in the server.
	-Using cd change a terminal window to be pointing at the directory houseing client.py
	-Run the client using "python3 client.py {server_ip} {server_port} {key_file} {input_file}"
	-The server port much be the same port that the server was initialized with.

How to run the Server:
	-Once the zip file is extracted move the server.py and a copy of encrypt.py, decrypt.py, and helpers.py onto the server machine.
	-Make sure that all of the .py file are in the same directory.
	-open server.py
	-Edit the dictionary key_dic to include the ip address of the client pointing to a string containing 8 characters acting as keys.
	-Using cd change a terminal window to be pointing at the directory houseing server.py
	-Run the command: "python3 server.py {port_numer}"
	-The server will now be running and will wait unitl it receives a packet from a client.
	-Return to reading about the client.

	