import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("Hostname: ", hostname)
print("IP Address: ", ip_address)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip_address, 5000))
s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print('Received from client: ', data)
        data = input('Enter data to send to client: ')
        print('Sending to client: ', data)
        c.send(data.encode())
    c.close()
