import socket


def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 4000))  # Подключаемся к нашему серверу.
    print("Создано соединение между клиентом и сервером")

    while True:
        client_command = input()
        s.sendall(client_command.encode('utf-8'))
        if client_command == "-1":
            print("Получен запрос на уничтожение связи")
            break
        input_string = s.recv(1024).decode('utf-8')
        if input_string:
            print("Получены данные: ")
            print(input_string)
    s.close()
    print("Связь уничтожена")


if __name__ == '__main__':
    client()
