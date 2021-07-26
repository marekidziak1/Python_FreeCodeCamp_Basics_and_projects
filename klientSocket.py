######################### strona klienta:
import socket as s     #wpisujesz nazwe HOSTA SERWERA na sztywno
HOST = s.gethostname() #ALBO poprzez gethostname() (swojego komputera)
PORT = 33000
BUFFER =1024
client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT))
#STRONA WYSYŁAJĄCA
name=input("Twoje imie: ").encode("utf8")
client_socket.send(name)
#STRONA ODBIERAJĄCA
print(client_socket.recv(BUFFER).decode("utf8"))
#STRONA WYSYŁAJĄCA
HEADER=8
surname=input("Twoje nazwisko: ").encode()
surname_header= f"{len(surname):<{HEADER}}".encode()
client_socket.send(surname_header + surname)
#STRONA ODBIERAJĄCA:
HEADER=8
msg2_header=client_socket.recv(HEADER).decode()
msg2=client_socket.recv(int(msg2_header)).decode()
print(msg2)
