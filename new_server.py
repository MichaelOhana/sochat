import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 3000))

peers = []

# Register peer
while len(peers) < 2:
    data, addr = server_socket.recvfrom(1024)
    peers.append(addr)

# Send infro about the each peer to the other peer
server_socket.sendto(f"{peers[1][0]} {peers[1][1]}", peers[0])
server_socket.sendto(f"{peers[0][0]} {peers[0][1]}", peers[1])