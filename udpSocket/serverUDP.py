import socket
import time
HOST = '127.0.0.1'
PORTA = 8080
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
origem = (HOST, PORTA)
udp.bind(origem)
while(True):
    print("Esperando cliente...")
    # recebendo uma tupla contendo a mensagem do cliente
    array = udp.recvfrom(1024)
    # [0] = mensagem [1] = origem
    print(f"{array[0].decode()} recebida de {array[1]}") 