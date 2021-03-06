import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.7"
ADDR = (SERVER, PORT)
print("Hola mundo")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

mensajes = ["hola","chao","prueba"]
    
send(mensajes[0])
input()
send(mensajes[1])
input()
send(mensajes[2])

send(DISCONNECT_MESSAGE)