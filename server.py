import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0',1234)) #привязываем к порту 1234
server.listen()
print('сервер запущен \n\n')
while True:
 #принимаем данные
    client_sock , client_inf = server.accept()
    data = (client_sock.recv(1024)).decode()

    #сохраняем данные отправителя чтобы потом отправить ответ
    client_ip, client_port =client_inf[0], client_inf[1]
    print(f'соединяю с пользователем {client_ip, client_port}')
    print(f'[*] получено новое сообщение: {data}')

    client_sock.send(b'hello')
    client_sock.close()
