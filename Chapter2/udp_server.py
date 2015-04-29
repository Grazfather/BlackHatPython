import socket

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((bind_ip, bind_port))

print "[*] Ready for data at %s:%d" % (bind_ip, bind_port)

while True:
    data, addr = server.recvfrom(1024)

    print "[*] Got data from %s:%d: %s" % (addr[0], addr[1], data)

    server.sendto("ACK!", addr)
