import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.112"
ADDR = (SERVER, PORT)
print("Hola mundo")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)