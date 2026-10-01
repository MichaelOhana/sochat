import socket
import threading
rendezvous_server =  ("165.245.214.71", 3000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(("0.0.0.0", 2000))

# Connect to rendezvous server
print("Registering")
client_socket.sendto(b"0", rendezvous_server)

# Check for confirmation from the server
while True:
    data = client_socket.recv(1024)

    if data == b"ready":
        print("Server confirmd registeration. Waiting for other peer...")
        break

# Reciving other peer connection infro from server
data = client_socket.recv(1024).decode()
ip, port = data.split(" ")
port = int(port)

print(f"Recived peer infro: {ip} {port}")

# Punching a hole
client_socket.sendto(b"0", (ip, port))
print("Punched a hole. Waiting for other peer...")


# Listen for msgs from peer
def listen():
    while True:
        msg = client_socket.recv(1024).decode()
        print(f"peer said: {msg}")

listener = threading.Thread(target=listen, daemon=True);
listener.start()


# send msgs to peer
while True:
    msg = input("> ")
    client_socket.sendto(msg.encode(), (ip, port))