import socket
import datetime


def server_program():
    host = ''
    port = 1305
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(6)
    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        conn.send(datetime.datetime.now().strftime("%d.%m.%y %H:%M").encode())
        conn.close()


if __name__ == '__main__':
    try:
        server_program()
    except KeyboardInterrupt:
        pass
