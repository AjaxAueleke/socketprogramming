import socket
s = socket.socket()
s.connect(('localhost', 5000))
while True:
    data = input('Enter data to send to server: ')
    print('Sending to server: ', data)
    s.send(data.encode())
    data = s.recv(1024).decode()
    print('Received from server: ', data)
    if not data:
        break
s.close()
