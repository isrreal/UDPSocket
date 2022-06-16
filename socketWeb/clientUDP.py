import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # For UDP
udp_host = '127.0.0.1'		# IP do host
udp_port = 8080			    # porta pra se conectar
while(True):
    msg = input("sua mensagem\n")
    code = str.encode(msg)
    print(f"IP do alvo: {str(udp_host)}") 
    print(f"Porta alvo: {str(udp_port)}")
    sock.sendto(code,(udp_host,udp_port))	