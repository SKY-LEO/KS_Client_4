import pickle
import socket

menu = "Для просмотра всех векторов напишите \"view\"\n" \
       + "Чтобы добавить вектор напишите \"add число число\"\n" \
       + "Чтобы изменить вектор напишите \"edit номер_вектора новое_значение\"\n" \
       + "Чтобы удалить товар напишите \"delete номер_вектора\"\n" \
       + "Чтобы умножить векторы на скаляр напишите \"* коэффициент\"\n" \
       + "Чтобы поделить векторы на скаляр напишите \"/ коэффициент\"\n" \
       + "Чтобы просмотреть минимальные элементы векторов напишите \"min\"\n" \
       + "Чтобы просмотреть максимальные элементы векторов напишите \"max\"\n" \
       + "Чтобы отсортировать элементы векторов по возрастанию напишите \"asc\"\n" \
       + "Чтобы отсортировать элементы векторов по убыванию напишите \"desc\"\n" \
       + "Чтобы сложить вектор_1 с вектор_2 напишите \"sum вектор_1 вектор_2\"\n" \
       + "Чтобы отнять от вектор_1 вектор_2 напишите \"dif вектор_1 вектор_2\"\n" \
       + "Чтобы просмотреть список команд напишите \"help\"\n" \
       + "Чтобы завершить работу напишите \"-1\"\n"


def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 6000))
    print("Создано соединение между клиентом и сервером")
    help_dialog()

    while True:
        client_command = input("Введите сообщение: ")
        if client_command == "-1":
            break
        elif client_command == "help":
            help_dialog()
        else:
            client_socket.sendall(pickle.dumps(client_command))
            input_string = pickle.loads(client_socket.recv(4096))
            print("Получены данные:", input_string, "\n")
    client_socket.close()
    print("Связь уничтожена")


def help_dialog():
    print("\033[36m{}".format(menu))
    print("\033[0m")


if __name__ == '__main__':
    client()
