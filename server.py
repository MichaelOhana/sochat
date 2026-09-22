import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 3000))
peers = {}

# def userExists(user):
#     return input in peers

while True:
    data, addr = server_socket.recvfrom(1024)
    msg = data.decode().split(":")
    requestHeader = msg[0]
    requestBody = msg[1]
    print(f"Request header: '{requestHeader}' \nRequest body: '{requestBody}'")
    if(requestHeader == "Register"):
        peers[requestBody] = str(addr)
        print(f"{requestBody}: {peers[requestBody]}")
    elif(requestHeader == "Send"):
        print("DEBUG: " + peers[requestBody])
        server_socket.sendto((peers[requestBody][0] + ":" + peers[requestBody][1]).encode(), addr)
        server_socket.sendto(addr[0].encode() ,peers[requestBody].encode())


