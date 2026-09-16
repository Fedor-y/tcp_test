import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target_port = 1234
target_host = '127.0.0.1'

client.connect((target_host,target_port))

client.send(b'hi serv!')

response = client.recv(1024)
print(response.decode())
client.close()
