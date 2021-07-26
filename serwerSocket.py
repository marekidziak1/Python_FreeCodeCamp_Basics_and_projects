######################### strona servera
#ODPALENIE SERWERA I KLIENTA POWININES ZROBIĆ W DWÓCH KONSOLACH
    # STWORZENIE OBIEKTU SOCKETA
    # socket.AF_INET - rodzina adresow IPV4 ;deklarujemy jakie IP bedzie obiekt przyjmował
    # socket.AF_INET6 -rodzina adresow IPV6 ;deklarujemy jakie IP bedzie obiekt przyjmował
    # socket.SOCK_STREAM - strumien przesyłu danych dla socketa
import socket as s
HOST = s.gethostname()
PORT = 33000
BUFFER =512    #ilosc Bitow z jaką rezerwujemy sobie na wiadomość
                #mozna tez zrobic to na mniejszym bufferze
server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    # otworzenie połączenia dla klienta (w argumencie podajesz krotke (HOST,PORT)
    # poprzez bind() wiążasz ze sobą HOST I PORT tworzac adres i
    # włączasz nasluchiwanie polączeń (w argumencie jest kolejka klientow ktorzychca sie polaczy)
    #i nawiązujesz połączenie z klientem
server_socket.bind((HOST, PORT))
server_socket.listen(2)
while True:
    client_socket, address = server_socket.accept()
    print(f"Uzyskano polaczenie od {address} | lub {address[0]}:{address[1]}")
    #STRONA ODBIERAJĄCA
    name = client_socket.recv(BUFFER).decode("utf8")
    print(f"[{address[0]}:{address[1]}], Nazwa uzytkownika: {name}")
    #STRONA WYSYŁAJĄCA
    msg = f"Witaj na serwerze, {name}!".encode("utf8")
    client_socket.send(msg)
    #STRONA ODBIERAJĄCA:
    HEADER=8
    surname_header =client_socket.recv(HEADER).decode()
    surname=client_socket.recv(int(surname_header)).decode()
    print(f"Nazwisko uzytkownika: {surname}")
    #STRONA WYSYŁAJĄCA:
    HEADER=8
    msg2= f"nazwisko ktore otrzymalismy to: {surname}".encode()
    msg2_header=f"{len(msg2):<{HEADER}}".encode()
    client_socket.send(msg2_header+msg2)

#METODY W SOCKETACH - niezależnie czy jestes w serwerze czy w kliencie
#zawsze uzywasz metod na obiekcie klienta (w kliencie na obiekcie
#klienta stworzonym przez konstruktor a w serwerze na obiekcie
#klienta zwróconym dzięki server_socket.accept()):
    #METODA send() - wysylasz jakies dane podane w argumencie ktore
                    #wczesniej musisz zakodować poprzez metodę encode("utf8")
    #METODE recv() - otrzymujesz jakies dane do ktorych musisz
                    #okreslic ilosc zarezerwowanego miejsca na te
                    #dane (argument BUFFER,ktory deklarujesz
                    #wcześniej) i ktore musisz takze zdekodowac
                    #poprzez metode decode("utf8")
        #Jeżeli masz bardzo duży plik to zamiast rezerwować miejsce (BUFFER)
        #na sztywno (czyli zarezerwowanego miejsca na plik) to czekasz na
        #wiadomość od drugiej strony ktora będac podzielona na 2 cześci:
        #daje nam (pierwsza cześć - NAGŁÓWEK:) rozmiar pliku oraz
        #(druga cześć:) dany plik. Dzięki temu strona odbierająca dokladnie
        #ile BUFFERA ma sobie przygotować na dany plik

        #PO STRONIE WYSYŁĄJĄCEJ musisz stworzyć:
            #zmienną - plik ktory zakodujesz
            #zmienna_header - czyli rozmiar wysyłanego pliku ktoremu
                  #przypiszesz poprzez HEADER miejsce w jakim te
                  #dane o rozmiarze będą musiały się zmieścić
                  #ZAPIS takiejgo rozmiaru: (+trzeba jeszcze zakodowac)
                  #  zmienna_header= f"{len(surname):<{HEADER}}"
                  #taki zapis stworzy nam iles-bajtowy odstep(HEADER)
                  #ktory musi byc taki sam po stornie otrzymujacej
            #poprzez metode send() wyslanie zmienna_header+zmienna
                  #czyli danych o rozmiarze pliku i sam plik

        #PO STRONIE OTRZYMUJĄCEJ musisz stworzyc:
            #HEADER - czyli ile miejsca rezerwujesz na wiadomosc o
                  #wielkosc pliku ktory zostanie nadesłany w
                  #metodzie receive
            #header_len - zmienna ktora przechowa wielkosc pliku ktory nadejdzie
            #zmienną - której przekazesz nadesłany plik za pomocą metody recv()
                  #ktorej w argumencie przekazesz header_len czyli wielkość
                  #nadesłanego pliku zamiast na sztywno ustalac BUFFER

        #HEADER - czyli zarezerwowany obszar miejsca na nagłówek (czyli
                  #wielkosc nadeslanego pliku musi byc taki sam zarowno po
                  #stronie odbierającej jak i po stronie wysyłającej
                  #gdyż np jezeli zarezerwuje 8 bajtow miejsca na dane o wielkosci
                  #pliku po stronie wysyłającej i dodam do tego sam plik
                  #to po stornie odbierajacej muszę najpierw odczytac te 8 bajtow
                  #a dopiero potem kolejny plik. Jeżeli odczytałbym np tylko2 bajty
                  #to pozostałe 6 bajtów już by program pobrał sobie z mojego pliku
                  #co spowodowałoby błąd krytyczny gdyż po stronie odbierającej wczytałyby
                  #błedne dane o wielkosci pliku (przez te 6 dodatkowych bajtów) jak
                  #i błedne dane o samym pliku (przez te 6 brakujących początkowych bajtów)
