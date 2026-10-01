import socket
import threading
rendezvous_server =  ("165.245.214.71", 3000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind("0.0.0.0", 2000)

def menu():
    print("---MENU--- \n Send = s \n Register = r \n Wait = w")
    while True:
        selection = input("Input: ")
        if(selection in ["r", "s", "w"]):
            return selection

# def peer_exists(peer):
#     client_socket.send(("peer_exists:" + peer).encode(), rendezvous_server)
#     while True:
#         client_socket.recvfrom(1024)

def format_request(header, body):
    return f"{header}:{body}".encode()

def recive_from_peer(peer_addr):
    addr = ""
    while addr != peer_addr:
        data, addr = client_socket.recvfrom(1024)
    print(data.decode())

while True:
    selection = menu()
    if(selection == "r"):
        username = input("Username to Register: ")
        client_socket.sendto(format_request("Register", username), rendezvous_server)
        recive_peer_ip = threading.Thread(
                target=recive_from_peer,
                args=(rendezvous_server[0],))
        recive_peer_ip.start()
    elif(selection == "s"):
        peer_to_connect_with = input("Username for the peer you want to connect with: ")
        client_socket.sendto(format_request("Send", peer_to_connect_with), rendezvous_server)

        addr = ""
        while addr != rendezvous_server:
            data, addr = client_socket.recvfrom(1024)

        msg = data.decode().split(":")
        peer_ip = msg[0]
        peer_port = int(msg[1])
        print("ip: " + msg[0])
        print("port: " + msg[1])

        for i in range(100):
            recive_thread = threading.Thread(
                target=recive_from_peer,
                args=(peer_ip,))
            recive_thread.start()

            client_socket.sendto(f"hello #{i}".encode(), (peer_ip, peer_port))
            print(f"Sent: hello#{i} to {peer_ip}")
        recive_thread.join()
    elif(selection == "w"):
        recive_peer_ip.join()