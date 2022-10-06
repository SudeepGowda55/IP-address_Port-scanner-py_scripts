# !/bin/python3
import sys, socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Target gives the host address using host name (domain name)

else :
    print("Invalid arguments : Please enter a valid arguments")
    print("syntax: python3 filename hostname")
    sys.exit()

print("-" * 50)
print("Scanning Target " + target )
print("Target Scanning Started at" + str(datetime.now()))
print("-" * 50)

try:
    for port in range(0, 65535):
        sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockets.settimeout(0.5) # To close the connection request if not accepted. Then after 0.5 sec or any sec connection will close  --> Time in float (sec)
        result = sockets.connect_ex((str(target), port))  # returns 0 if connection is established or returns int which indicates err no
        if result == 0:
            print(f"Port {port} is open")
            sockets.close()
        else :
            print(f"port {port} closed")
            sockets.close()

except KeyboardInterrupt:
    print("\n Exiting Program")
    sys.exit()

except socket.gaierror:    # Use socket not sockets (variable). gai --> get add info
    print("Hostname is not resolved. Please enter a valid hostname")
    sys.exit()

except socket.error:       # Use socket not sockets (variable)
    print("Couldn't connect to server")
    sys.exit()