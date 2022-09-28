import socket

print("введите ip")
HOST = input()
PORT = 1303

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    s.close()
print(f"{data!r}")
