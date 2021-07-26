#SPIS TREŚCI:
    #lesson3 - IF; TRY,EXCEPT:
        #IfTry_1
        #IfTry_2
    #lesson4 - FUNCTION:
    #lesson5 - WHILE; FOR:
    #lesson6 - STRING:
    #lesson7 - FILES:
        #zad1i3 - otwieranie pliku
        #zad2 - zliczanie SPAMU
    #lesson8 - LIST:
        #zad1 - praca na orginałach listy we funkcjach
        #zad2 - max i min wartość w liscie
        #zad4_1 - lista unikalnych slow w tekscie
        #zad4_2 - lista unikalnych slow w tekscie
        #zad5 - wyciaganie adresow email z teksu
    #lesson9 - DICTIONARY:
        #przypisanie listy do istniejacej wczesniej kolekcji Dictionary
        #zliczanie slow w teksie poprzez kolekcje Dictionary
        #znajdowanienajczestszego slowa w tekscie
        #zad9_2 - zliczanie słow w tekscie
        #zad9_3i4 - najczestsze slowo w tekscie
        #zad9_5 - najczesciej wystepujacy email
    #lesson10 - TUPLE:
        #przypisanie zmiennych w krotce
        #sortowanie listy Krotek - funkcja sorted
        #sortowanie w kolekcji Dictionary
        #sortowanie w kolekcji Dictionary - KROTSZE (1linia)
        #metoda sorted i reversed
        #zad10_2 - sortowanie emaili wg godziny
        #zad10_1_1 - znajdowanie najczesciej wystepujacego maila
        #zad10_1_2 - znajdowanie najczesciej wystepujacego maila
        #zad10_3 - Znajdowanie Najczesciej Wystepujacej Litery
    #lesson11 - REGEX:
        #REGEX - wszystkie Maile W Pliku
        #REGEX - maile Zaczynajace Sie Od Slowa From
        #REGEX - wyszukiwanie Domeny W Mailu
        #REGEX - wyszukiwanie po aliasie - spam Confidence
        #zad1 Imitacja Funkcji Grep
        #zad2_1_Wszystkie Liczby w pliku
        #zad2_2_Wszystkie Liczby Zwykle i Z przecinkiem
    #lesson12- BEAUTIFUL SOUP:
        #polaczenieHTTP_Przegladarka_internetowa()
        #polaczenieHTTP_Przegladarka_Internetowa_URLLIB()
        #polaczenieHTTP_Przegladarka_Internetowa_REQUESTS_MODULE()
        #polaczenieSocketow_WYMIANA_PLIKOW()
        #polaczenieHTTP_Przegladarka_internetowa()
        #zad1_przegladarka_internetowa_z_obsluga_bledow()
        #zad2_ilosc_znakow_przegladarka_internetowa()
        #zad3_ilosc_znakow_przegladarka_internetowa_URLLIB()
        #zad4_BeautifulSoup()
        #zad5_1_BeautifulSoup_sum_of_content()
        #zad5_2_BeautifulSoup_chodzenie_po_linkach()
    #lesson13 - XML and JSON and API:
        #wyszukiwanieDanych_XML()
        #wyszukiwanieDanych_XML_2()
        #pobieranieDanych_JSON()
        #pobieranieDanych_JSON_2()
        #JSONgeocodeAPI_google_maps_bez_API_KEY()
        #JSONgeocodeAPI_google_maps_WRAZ_Z_API_KEY()
        #XML_zad1_findall_data_API()
        #JSON_zad2_API()
        #JSON_zad3_geocode_google_map_API()
def lesson3IfTry():
    def lesson3_1ifTry():
        try: hours =float(input('Enter hours: '))
        except:
            print('Hours are floats not str, try one more time')
            lesson3_1ifTry()
        try: rate = float(input('Enter rates: '))
        except:
            print('Rate is float not str, try one more time')
            lesson3_1ifTry()
        grossPay = hours *rate
        if hours>40: grossPay=40*rate + (hours-40)*rate*1.5
        print("Pay: "+str(grossPay))
    #lesson3_1ifTry()
    def lesson3_2IfTry():
        grade=input("Enter the grade: ")
        #if type(grade)==str: raise TypeError
                #jezeli wyjatek przy słowku raise nie
                #zostanie obsluzony to wyskoczy blad
        try:
            #grade = float(input("Enter the grade: "))
            #if type(grade)==str: raise TypeError
            if grade > 1.0 or grade < 0.0: raise ValueError
                #jednakże jeżeli wywołanie wyjatku zostanie
                #obsluzone to program zostanie przerwany
                #wykona sie blok except i nastpai kontynuacja
                #programu
            print("continuation try block")
        except TypeError:
            print("Bad Score TypeError")
            #lesson4_2IfTry()
        except ValueError:
            print("Bad Score ValueError")
            #lesson4_2IfTry()
            #quit(0)       #tej funkcji trzebaby było uzyc gdyby
                           #pozostale instrukcje nie zostały
                           #obsluzone w bloku else
        else:
            if grade>=0.9: print('A')
            elif grade>=0.8: print('B')
            elif grade>=0.7: print('C')
            elif grade>=0.6: print('D')
            else: print('F')
        print("end")
    lesson3_2IfTry()
def lesson4Function():
    class MYTypeError(Exception):pass
    class MYValueError(Exception):pass
    def computepay(h, r):
        gross=float()
        try:
            if type(float(h))!=float: raise TypeError
            else: h=float(h)
            if type(float(r))!=float: raise MYTypeError
            else: r=float(r)
            if h<0 or r<0: raise ValueError
        except TypeError: h=0
        except MYTypeError: r=0
        except ValueError:h=0
        except MYValueError:r=0
        else:
            gross=h*r
            if h>40: gross=40*r +(h-40)*r*1.5
        return gross
    hrs = input("Enter Hours:")
    rts = input("Enter Rates:")
    p = computepay(hrs, rts)
    print("Pay", p)
def lesson5WhileFor():
    largest = None
    smallest = None
    sum=None
    count=None
    average=None
    while True:
        num = input("Enter a number: ")
        if num == "done":
            if sum is not None and count is not None:
                average=sum/count
            break
        try:
            num=float(num)
            if smallest is None: smallest=num
            elif smallest>num: 	 smallest=num
            if largest is None:	largest=num
            elif largest<num: 	largest=num
            if sum is None: sum=num
            elif type(num)==float: sum=sum+num
            if count is None: count=1
            else: count+=1
        except ValueError:
            print("Invalid input")
    print("Maximum is ", largest)
    print("Minimum is ", smallest)
    print("Average is ", average)
def lesson6String():
    word="banana"
    if word  == "banana": print("jest rowne słowu \"banana\"")
    elif word < "banana": print("przed słowem \"banana\"")
    elif word > "banana": print("za słowem \"banana\"")

    str = 'X-DSPAM-Confidence:0.8475'
    colpos=str.find(":")
    substr=str[colpos+1:]
    substr.strip()
    number=float(substr)
    print(number)
def lesson7Files():
    def zad1i3():
        try:
            count=0
            namefile = input("Enter a file name: ")
            if namefile == "na na boo boo":
                print("NA NA BOO BOO TO YOU - You have been punk'd!")
                quit(0)
            else:
                file = open(namefile)
                for line in file:
                    print(line.upper().rstrip())
                    count=count+1
        except FileNotFoundError:
            print("nie znaleziono pliku, sprobuj jeszcze raz")
            zad1i3()
            quit(0)
        else:
            print("There were ",str(count)," lines in ",namefile," file")
    #zad1i3()
    def zad2():
        try:
            fname=input("Enter file name: ")
            fh=open(fname)
            total=0.0
            count=0.0
            lista=list()
            for line in fh:
                if not line.startswith("X-DSPAM-Confidence:"): continue
                else:
                    total=total+(float(line.split()[-1]))
                    count=count+1
            average=total/count
            print("Average spam confidence: ", average)
        except FileNotFoundError: print("File don't exist")
    #zad2()
def lesson8List():
    def zad8_1():
        list1 = [3,4,5,6]
        def chop(list1):
            if len(list1)<3:
                return list1
            else:
                list1.pop(0)
                list1.pop()
                return list1
        print(list1)    #przekazujac argumenty do funkcji
                        #pracujesz na orginałach nie na kopiach
        chop(list1)
        print(list1)
    zad8_1()
    def zad8_2MinMaxList():
        number=int()
        list1=list()
        while number!="done":
            number=input("Enter your number or exit by writing \"done\": ")
            if(number.isnumeric()): list1.append(number)
            else: print("you can only writes integers!!!")
        try: return "Maxximum: "+str(max(list1))+", Minimum: "+str(min(list1))
        except ValueError: return "Maxximum: None, Minimum: None"
        except: return "Maxximum: None, Minimum: None"
    print(zad8_2MinMaxList())
    def zad8_4_1ListaUnikalnychSlowWTekscie():
        listOfWords=list()
        try:
            file = open("romeo.txt","r")
            for line in file:
                words=line.split();
                count=0
                for word in words:
                    for globalWord in listOfWords:
                        if word == globalWord:
                            count += 1
                    if count ==0:
                        listOfWords.append(word)
                    count=0
            file.close()
        except FileNotFoundError: print("There is no File with that name in function zad9_4_1")
        except: print("Another bug in function zad9_4_1")
        finally: return listOfWords
    def zad8_4_2ListaUnikalnychSlowWTekscie():
        listOfWords=list()
        try:
            file = open("romeo.txt","r")
            for line in file:
                words=line.split();
                for word in words:
                    if any(word==globalWord for globalWord in listOfWords):continue
                    else: listOfWords.append(word)
            file.close()
        except FileNotFoundError: print("There is no File with that name in function zad9_4_2")
        except: print("Another bug in function zad9_4_2")
        finally: return listOfWords
    print(zad8_4_1ListaUnikalnychSlowWTekscie())
    print(zad8_4_2ListaUnikalnychSlowWTekscie())
    def zad8_5WyciaganieAdresowEmail():
        try:
            fh = open("text8.txt","r")
            count = 0
            for line in fh:
                if not line.startswith("From:") and line.startswith("From "):
                    words=line.split()
                    print(words[1])
                    count+=1
            print("There were", count, "lines in the file with From as the first word")
            fh.close()
        except FileNotFoundError: "There is no such file"
        except: "another bug "
    zad8_5WyciaganieAdresowEmail()
def lesson9Dictionaries():
    def przypisanieListyDoistniejacejWczesniejDictionary():
        dictionary = {"marek": 1, "arek":2}
        dictionary2= {"zdzsiek":2}
        for nameDict1 in dictionary:
            dictionary2[nameDict1] = dictionary2.get(nameDict1,0)+1
        print(dictionary2)
    #przypisanieListyDoistniejacejWczesniejDictionary()
    def zliczanieSlowWTeksciePrzezSlownik():
        words =list()
        dictionary = dict()
        try:
            fname = input("Enter the file name: ")
            file = open(fname,"r")
            for line in file:
                words.extend(line.split())
            for word in words:
                dictionary[word]=dictionary.get(word,0)+1
        except ValueError: print("No such file try again")
        except: print("other bug")
        print(dictionary)
    #zliczanieSlowWTeksciePrzezSlownik()
    def znajdowanieNajczestszegoSlwoaWTekscie():
        fname=input("Enter a file name")
        file = open(fname, "r")
        words=list()
        dictionary=dict()
        for line in file:
            words=line.split()
            for word in words:
                dictionary[word]=dictionary.get(word,0)+1
        bigWord=None
        bigValue=None
        for word,value in dictionary.items():
            if bigValue == None or bigValue <value:
                bigWord=word
                bigValue=value
        print((bigWord,dictionary[bigWord]))
    #znajdowanieNajczestszegoSlwoaWTekscie()
    def zad9_2():
        words=list()
        dictionary=dict()
        fname=input("Enter File Name: ")
        file = open(fname, "r")
        for line in file:
            if line.startswith("From") and not line.startswith("From:"):
                words=line.split()
                dictionary[words[2]]=dictionary.get(words[2],0)+1
        print(dictionary)
    #zad9_2()
    def zad9_3i4():
        dictionary = dict()
        words=list()
        fname = input("Enter file name: ")
        file= open(fname, "r")
        for line in file:
            if line.startswith("From") and not line.startswith("From:"):
                words = line.split()
                dictionary[words[1]]=dictionary.get(words[1],0)+1
        print(dictionary)
        bigkey=None
        bigValue=None
        for key,value in dictionary.items():
            if bigValue==None or value>bigValue:
                bigValue=value
                bigkey=key
        print((bigkey,bigValue))
    #zad9_3i4()
    def zad9_5():
        dictionary=dict()
        fname=input("Enter file name")
        file = open(fname,"r")
        for line in file:
            if line .startswith("From") and not line.startswith("From:"):
                words=line.split()
                word=words[1][words[1].find('@')+1:]
                dictionary[word]=dictionary.get(word,0)+1
        print(dictionary)
        bigKey=None
        bigValue=None
        for key,value in dictionary.items():
            if bigValue==None or value>bigValue:
                bigValue=value
                bigKey=key
        print((bigKey,bigValue))
    #zad9_5()
def lesson10Tuple():
    def przypisanieZmiennychwKrotce():
        (x,y) = [5,4]
        print(x)
        print(y)
    #przypisanieZmiennychwKrotce()
    def sortowanieListyKrotekFunkcjaSorted():
        #Przykład 1:
        slownik={'c':10, 'a':1, 'b':22}
        for key, value in slownik.items():
            print(key, value)
        print(slownik.items())
        print(sorted(slownik.items()))
        #Przykład 2:
        b=('r',10,22)
        c=('g',33,21)
        d=('r',9,55)
        e=('r',9,56)
        f=('z',1,1)
        list_of_tuples=[b,c,d,e,f]
        print(sorted(list_of_tuples))
        for m1,m2,m3 in sorted(list_of_tuples):
            print(m1,m2,m3)
    #sortowanieListyKrotekFunkcjaSorted()
    def sortowanieWSlowniku():
        #Przykład 1:
        slownik={'d':33,'c':10, 'a':1, 'b':22}
        tmp =list()
        for key, value in slownik.items():
            newTuple=(value, key)
            tmp.append(newTuple)
        tmp=sorted(tmp,reverse=True)
        #tmp.sort(reverse=True)
        tmp2=list()
        for value, key in tmp:
            newTuple=(key,value)
            tmp2.append(newTuple)
        print(tmp2)
    #sortowanieWSlowniku()
    def sortowanieWSlownikuKROTSZE():
        slownik = {'d': 33, 'c': 10, 'a': 1, 'b': 22}
        print(sorted([(v,k) for k,v in slownik.items()]))
    #sortowanieWSlownikuKROTSZE()
    def metodaSortedIReversed():
        slownik={'d':33,'c':10, 'a':1, 'b':22}
        tuple=(('t',3),('x',44),('r',33))
        lista=['t',3,'x',44,'r',33]
        zmienna = sorted(tuple, key= lambda x: x[1], reverse=True)
        print(sorted(tuple))
        print(list(reversed(tuple)))
        print(list(reversed(zmienna)))
        print(reversed(zmienna))
    #metodaSortedIReversed()
    def zad10_2_SortowanieEMailiWgGodziny():
        name = input("Enter file:")
        if len(name) < 1:
            name = "text8.txt"
        handle = open(name)
        dictionary = dict()
        for line in handle:
            if line.startswith("From") and not line.startswith("From:"):
                words = line.split()
                time = words[-2].split(":")
                hour = time[0]
                dictionary[hour] = dictionary.get(hour, 0) + 1
        for key, value in sorted(dictionary.items()):
            print(str(key) + " " + str(value))
    #zad10_2_SortowanieEMailiWgGodziny()
    def zad10_1_1_ZnajdowanieNajczesciejWystepujacegoMaila():
        fname="text8LONG.txt"
        file=open(fname,"r")
        dictionary=dict()
        for line in file:
            if line.find("@")>0:
                words = line.split("@")
                words1 = words[0].split()
                words2 = words[1].split()
                email=str(words1[-1])+"@"+str(words2[0])
                dictionary[email]=dictionary.get(email,0)+1
        bigKey=None
        bigValue=None
        for key,value in dictionary.items():
            if bigValue==None or value>bigValue:
                bigValue=value
                bigKey=key
        print(bigKey, bigValue)
        for key,value in sorted(dictionary.items(), key=lambda x: x[1], reverse=True):
            print(key,value)
    #zad10_1_1_ZnajdowanieNajczesciejWystepujacegoMaila()
    def zad10_1_2_ZnajdowanieNajczesciejWystepujacegoMaila():
        fname="text8LONG.txt"
        file=open(fname,"r")
        dictionary=dict()
        for line in file:
            if line.startswith("From") and not line.startswith("From:"):
                words=line.split()
                dictionary[words[1]]=dictionary.get(words[1],0)+1
        mails=sorted([(v,k) for k,v in dictionary.items()],reverse=True)
        print(mails[0][1],mails[0][0])
        for v,k in mails:
            print(k,v)
    #zad10_1_2_ZnajdowanieNajczesciejWystepujacegoMaila()
    def zad10_3_ZnajdowanieNajczesciejWystepujacejLitery():
        fname="text8.txt"
        file = open(fname, "r")
        dictionary=dict()
        for line in file:
            import string
            line=line.translate(line.maketrans('','',string.punctuation))
            line=line.lower()
            line=line.strip()
            words=line.split()
            for word in words:
                for i in range(len(word)):
                    if not word[i].isdigit():
                        dictionary[word[i]]=dictionary.get(word[i],0)+1
        chars= sorted(dictionary.items(), key=lambda x: x[1],reverse=True)
        print("Najczesieciej wystepujaca litera to: ",chars[0][0],chars[0][1])
        for k,v in chars:
            print(k,v)
    #zad10_3_ZnajdowanieNajczesciejWystepujacejLitery()
def lesson11REGEX():
    def REGEXwszystkieMaileWPliku():
        file = open("text8.txt","r")
        print("Wszystkie emaile:")
        for line in file:
            import re
            zmienna=re.findall("\s(\S+@\S+)\s",line)
            if zmienna != []:
                print(zmienna)
    #REGEXwszystkieMaileWPliku()
    def REGEXmaileZaczynajaceSieOdSlowaFrom():
        print("Emaile z lini zaczyanje sie od \"From:\"")
        file = open("text8.txt", "r")
        for line in file:
            if (line.startswith("From")):
                import re
                zmienna=re.findall("^From:(\s\S+@\S+)",line)
                if zmienna!=[]:
                    print(zmienna)
    #REGEXmaileZaczynajaceSieOdSlowaFrom()
    def wyszukiwanieDomenyWMailu():
        file = open("text8.txt","r")
        for line in file:
            import re
            zmienna=re.findall("\s.*@(\S+)\s",line) #   "@([^ ]*)"
            if zmienna != []:
                print(zmienna)
    #wyszukiwanieDomenyWMailu()
    def spamConfidence():
        globalList=list()
        file =open("text8.txt","r")
        for line in file:
            import re
            lst=re.findall("^X-DSPAM-Confidence: ([0-9.]+)",line)
            if len(lst) ==0:continue
            globalList.append(float(lst[0]))
        print(max(globalList))
    #spamConfidence()
    def zad1ImitacjaGrep():
        pattern = input("Enter a regular expresion: ")
        #pattern="\S+@\S+"
        #pattern="^Author"
        #pattern="^X-"
        #pattern="java$"
        file=open("text8LONG.txt")
        counter=0
        for line in file:
            import re
            match=re.findall(pattern, line)
            if len(match)==0:continue
            #print(match, len(match))
            counter+=len(match)
        print(counter)
    def zad2_1_WszystkieLiczby():
        #fname=input("Enter file name: ")
        #file=open(fname,"r")
        file=open("text11.txt","r")
        counter=0
        counter2=0
        globalNumber=0
        for line in file:
            counter+=1
            import re
            matched=re.findall("(\d+)",line)
            for i in matched:
                print(i)
                counter2+=1
                globalNumber+=float(i)
        print("Sum: "+str(globalNumber))
        print("Average: "+str(globalNumber/counter))
        print("126616799863095.0")
    zad2_1_WszystkieLiczby()
    def zad2_2_WszystkieLiczbyZwykleiZprzecinkiem():
        #fname=input("Enter file name: ")
        #file=open(fname,"r")
        file=open("text8LONG.txt","r")
        counter=0
        counter2=0
        globalNumber=0
        for line in file:
            counter+=1
            import re
            matched=re.findall("(\d+[.]?\d*\s)",line)
            for i in matched:
                print(i)
                counter2+=1
                globalNumber+=float(i)
        print("Sum: "+str(globalNumber))
        print("Average: " + str(globalNumber / counter))
        print("126616799863095.0")
    #zad2_2_WszystkieLiczbyZwykleiZprzecinkiem()
def lesson12Networking():
    def polaczenieHTTP_Przegladarka_internetowa():
        import socket
        HOST='data.pr4e.org'
        PORT=80
        client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect((HOST,PORT))
        rzadanieGet='GET http://data.pr4e.org.romeo.txt HTTP/1.0\r\n\r\n'.encode()
        #rzadanieGet='GET http://www.dr-chuck.com/page1.htm HTTP/1.0\r\n\r\n'.encode()
        client_socket.send(rzadanieGet)
        BUFFER=512
        while True:
            data = client_socket.recv(BUFFER)
            if len(data) <1:
                break
            print(data.decode(),end='')
        client_socket.close()
    #polaczenieHTTP_Przegladarka_internetowa()
    def polaczenieHTTP_Przegladarka_Internetowa_URLLIB():
        import urllib.request, urllib.parse, urllib.error
        file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
        file = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
        for line in file:
            print(line.decode().strip())
    #polaczenieHTTP_Przegladarka_Internetowa_URLLIB()
    def polaczenieHTTP_Przegladarka_Internetowa_REQUESTS_MODULE():
        import requests
        x = requests.get('http://data.pr4e.org/romeo.txt')
        x = requests.get('http://www.dr-chuck.com/page1.htm')
        print(x.text)
    #polaczenieHTTP_Przegladarka_Internetowa_REQUESTS_MODULE()
    def polaczenieSocketow_WYMIANA_PLIKOW():
        #WSZYSTKO DOKŁADNIE I LEPIEJ MASZ OPISANE W PLIKACH:
        #serwerSocket.py oraz klientSocket.py

        def serwerSocket():
            #strona servera
            import socket as s
            HOST=s.gethostname()
            PORT = 33000
            #STWORZENIE SOCKETA
            #socket.AF_INET - rodzina adresow IPV4 ;deklarujemy jakie IP bedzie obiekt przyjmował
            #socket.AF_INET6 -rodzina adresow IPV6 ;deklarujemy jakie IP bedzie obiekt przyjmował
            #socket.SOCK_STREAM - strumien przesyłu danych dla socketa
            server_socket = s.socket(s.AF_INET,s.SOCK_STREAM)
            #otworzenie połączenia dla klienta (w argumencie podajesz krotke (HOST,PORT)
            #wiążaesz ze sobą HOST I PORT tworzac adres i
            #włączasz nasluchiwanie polączeń
            server_socket.bind((HOST,PORT))
            server_socket.listen(2) #w argumencie kolejka klientow ktorzychca sie polaczyc
            while True:
                client_socket, address = server_socket.accept()
                print(f"Uzyskano polaczenie od {address} lub {address[0]}:{address[1]}")
        def klientSocket():
            # strona klienta:
            # TutaJ podajesz dane serwera ,nie klienta!!!
            import socket as s
            HOST = 'DESKTOP-J2DTD5J'
            PORT = 33000
            client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
            client_socket.connect((HOST, PORT))
        serwerSocket()
        #klientSocket()
        #zeby móc nawiązać połączenie to musisz klienta i serwera miec
        #w oddzielnych plikach uruchomionych w osobnych konsolach
    #polaczenieSocketow_WYMIANA_PLIKOW()
    def pobieranieLinkowBeautifulSoup():
        import urllib.request, urllib.parse, urllib.error
        from bs4 import BeautifulSoup
        #url = input("Enter a site address: ")
        url ='http://www.dr-chuck.com/page1.htm'
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags =soup('a')
        for tag in tags:
            print(tag.get('href',None))
    #pobieranieLinkowBeautifulSoup()

    #POTRZEBNE PLIKI:
    #https://www.py4e.com/code3/socket1.py
    #https://www.py4e.com/code3/urllinks.py
    #https://www.py4e.com/code3/urllink2.py?PHPSESSID=d163255a18b681c23d5f6c01094fc6a0

    def zad1_przegladarka_internetowa_z_obsluga_bledow():
        import socket
        import validators
        #url ="http://data.pr4e.org/romeo.txt"   #url = input("Enter your url: ")
        url ="http://data.pr4e.org/intro-short.txt"   #url = input("Enter your url: ")
        valid=validators.url(url)
        try:
            if valid !=True: raise Exception("URL is not valid")
        except : print("validation Url bug")
        else:
            HOST = url.split("/")[2]
            PORT = 80
            try:
                mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                mysock.connect((HOST, PORT))
            except socket.error("connection error"): quit(0)
            except: print("other connection bug")
            else:
                cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
                try:
                    mysock.send(cmd)
                except socket.error("Sending error"): quit(0)
                except:
                    print("other sending bug")
                else:
                    while True:
                        data = mysock.recv(512)
                        if len(data) < 1:
                            break
                        print(data.decode(),end='')
                mysock.close()
    #zad1_przegladarka_internetowa_z_obsluga_bledow()
    def zad2_ilosc_znakow_przegladarka_internetowa():
        import socket
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect(('data.pr4e.org', 80))
        cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)
        counter=0
        print("")
        while True:
            data = mysock.recv(100)
            if len(data) < 1:
                break
            for lit in data.decode():
                counter += 1
                if counter<3000:
                    print(lit,end='')
            #print(data.decode(),end='')
        print(counter)
        mysock.close()
    #zad2_ilosc_znakow_przegladarka_internetowa()
    def zad3_ilosc_znakow_przegladarka_internetowa_URLLIB():
        import urllib.request, urllib.parse, urllib.error
        file=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
        counter=0
        for line in file:
            counter+=len(line)
            if counter<=3000: [print(i,end='') for i in line.decode()]
            '''for i in line.decode():
                counter+=1
                if counter<=3000:
                    print(i,end='')'''
        print(counter)
    #zad3_ilosc_znakow_przegladarka_internetowa_URLLIB()
    def zad4_BeautifulSoup():
        import urllib.request, urllib.parse, urllib.error
        from bs4 import BeautifulSoup
        import ssl
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        #przyklad URL: https://www.w3.org/Protocols/HTTP/Performance/microscape/
        url = input('Enter - ')
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        counter=0
        for tag in tags:
            counter+=1
            print(tag.get('href', None))
        print(counter)
    #zad4_BeautifulSoup()
    def zad5_1_BeautifulSoup_sum_of_content():
        from bs4 import BeautifulSoup
        import urllib.request, urllib.parse, urllib.error
        url='http://py4e-data.dr-chuck.net/comments_1286488.html'
        html=urllib.request.urlopen(url).read()
        soup=BeautifulSoup(html, 'html.parser')
        tags=soup('span')
        sum=0
        for tag in tags:
            sum+=float(tag.contents[0])
        print(sum)
    #zad5_1_BeautifulSoup_sum_of_content()
    def zad5_2_BeautifulSoup_chodzenie_po_linkach():
        def zad5_2_Dane_Wejsciowe():
            #url = input('Enter the url: ')
            url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
            url = 'http://py4e-data.dr-chuck.net/known_by_Fruin.html'
            #count = input('Enter the count: ')
            count = 4
            count = 7
            #position = input('Enter position: ')
            position = 3
            position = 18
            zad5_2_rekursja(url,count,position)

        def zad5_2_rekursja(url, count, position):
            if count>0:
                from bs4 import BeautifulSoup
                import urllib.request, urllib.parse, urllib.error
                html = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(html, 'html.parser')
                tags = soup('a')
                posCounter = 0
                for tag in tags:
                    posCounter += 1
                    if posCounter > position: break
                    elif posCounter==position and count>0:
                        urlNow=tag.get('href',None)
                        print(tag.contents[0], urlNow)
                        zad5_2_rekursja(urlNow,count-1,position)
        zad5_2_Dane_Wejsciowe()
    #zad5_2_BeautifulSoup_chodzenie_po_linkach()
def lesson13_XML_JSON_API():
    def wyszukiwanieDanych_XML():
        import xml.etree.ElementTree as ET
        data='''<person>
                 <name>Chuck</name>
                  <phone type="init1">
                   +1 734 303 4456
                  </phone>
                  <email hide="yes" />
                </person>'''
        tree = ET.fromstring(data)
        print('Name:',tree.find('name').text)
        print('Attr:',tree.find('email').get('hide'))
    #wyszukiwanieDanych_XML()
    def wyszukiwanieDanych_XML_2():
        import xml.etree.ElementTree as ET
        data ='''<stuff>
                  <users>
                   <user x="2"> 
                     <id>001</id>
                     <name>Chuck</name>                
                   </user>
                   <user x="7">
                     <id>009</id>
                     <name>Brent</name>
                   </user>
                  </users>  
                 </stuff>'''
        tree = ET.fromstring(data)
        lst = tree.findall('users/user')
        print('User counts:',len(lst))
        for item in lst:
            print(item) #zwroci referencje do miejsca obiektu w RAMie
            print('Atribute:',item.get("x"))
            print('Id:',item.find('id').text)
            print('Name:', item.find('name').text)
    #wyszukiwanieDanych_XML_2()
    def pobieranieDanych_JSON():
        import json
        data='''{
            "name" : "Chuck",
            "phone" : {
                        "type" : "init1",
                        "number" : "+1 734 303 4456" 
                       },
            "email" : {
                        "hide" : "yes"
                       }
            }'''
        zmienna = json.loads(data)
        print('Name:',zmienna["name"])
        print('Phone:',zmienna["phone"])
        print('Email:',zmienna["email"])
        print('Hide:',zmienna["email"]["hide"])
    #pobieranieDanych_JSON()
    def pobieranieDanych_JSON_2():
        import json
        data='''[
            {"id" : "001",
             "x" : "2",
             "name" : "Chuck"
            },
            {"id" : "009",
             "x" : "7",
             "name" : "Buck"
            }
                ]'''
        zmienna= json.loads(data)
        print('User counts:',len(zmienna))
        for i in zmienna:
            print("Id",i['id'])
            print("Name",i['name'])
            print("Attribute",i['x'])
    #pobieranieDanych_JSON_2()
    def JSONgeocodeAPI_google_maps_bez_API_KEY():
        import urllib.request, urllib.parse, urllib.error
        import json
        # na koncu URL trzeba jeszcze dodać API KEY
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
        while True:
            location = input('Enter location, if you wanna quit enter \"quit\" ')
            if location=="":location = "Ann Arbor, MI"
            elif location=="quit":quit(0)
            if len(location)<1: break
            #na koncu URL trzeba jeszcze dodać API KEY
            url = serviceurl + urllib.parse.urlencode({'address': location})
            print('Uzyskano url =: ',url)

            html = urllib.request.urlopen(url)
            jsonData=html.read().decode()
            print('JSONdata length:',len(jsonData),'characters')
            print(jsonData)

            try:
                jsonPython= json.loads(jsonData)
                print('JSONloads:', jsonPython)
            except:
                jsonPython=None

            if not jsonPython or jsonPython['status'] !='OK' or 'status' not in jsonPython :
                print("=============FAILURE TO RETRIVE============")
                print(jsonData)
                continue

            lat = jsonPython["results"][0]["geometry"]["location"]["lat"]
            lng = jsonPython["results"][0]["geometry"]["location"]["lng"]
            loc = jsonPython["results"][0]["formatted_address"]
            print('lat:',lat,'lng:',lng)
            print('EnterLocation:',location,', GoogleLocalization:',loc)
    #JSONgeocodeAPI_google_maps_bez_API_KEY()
    def JSONgeocodeAPI_google_maps_WRAZ_Z_API_KEY():
        import urllib.request, urllib.parse, urllib.error
        import json
        import ssl

        api_key = False
        # If you have a Google Places API key, enter it here
        # api_key = 'AIzaSy___IDByT70'
        # https://developers.google.com/maps/documentation/geocoding/intro

        if api_key == False:
            api_key = 42
            serviceurl = 'http://py4e-data.dr-chuck.net/json?'
        else:
            serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
        print(serviceurl)
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        while True:
            location = input('Enter location, if you wanna quit enter \"quit\" ')
            if location=="":location = "Ann Arbor, MI"
            elif location=="quit":quit(0)
            if len(location) < 1: break

            parameters = dict()
            parameters['address'] = location
            parameters['key'] = api_key
            url = serviceurl + urllib.parse.urlencode({'address': parameters['address'], 'key': parameters['key']})
            print('Uzyskano url =: ', url)

            html = urllib.request.urlopen(url)
            jsonData = html.read().decode()
            print('JSONdata length:', len(jsonData), 'characters')
            print(jsonData)

            try:
                jsonPython = json.loads(jsonData)
                print('JSONloads:', jsonPython)
            except:
                jsonPython = None
            if not jsonPython or jsonPython['status'] != 'OK' or 'status' not in jsonPython:
                print("=============FAILURE TO RETRIVE============")
                print(jsonData)
                continue

            lat = jsonPython["results"][0]["geometry"]["location"]["lat"]
            lng = jsonPython["results"][0]["geometry"]["location"]["lng"]
            loc = jsonPython["results"][0]["formatted_address"]
            types = len(jsonPython["results"][0]["types"][0])
            [print(x["short_name"]) if x["types"][0] == "country" else None for x in jsonPython["results"][0]["address_components"]]
            print('lat:', lat, 'lng:', lng)
            print('EnteredLocation:', location, ', GoogleLocalization:', loc)
    #JSONgeocodeAPI_google_maps_WRAZ_Z_API_KEY()
    def XMLgeocode_API_google_maps_WRAZ_API_KEY():
        import urllib.request, urllib.parse, urllib.error
        import xml.etree.ElementTree as ET
        import ssl

        api_key = False
        # If you have a Google Places API key, enter it here
        # api_key = 'AIzaSy___IDByT70'
        # https://developers.google.com/maps/documentation/geocoding/intro

        if api_key is False:
            api_key = 42
            serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
        else :
            serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        while True:
            address = input('Enter location: ')
            if len(address) < 1: break

            parms = dict()
            parms['address'] = address
            if api_key is not False: parms['key'] = api_key
            url = serviceurl + urllib.parse.urlencode(parms)
            print('Retrieving', url)
            uh = urllib.request.urlopen(url, context=ctx)

            data = uh.read()
            print('Retrieved', len(data), 'characters')
            print(data.decode())

        #DOPIERO ODTĄD ZMIANA W SOTSUNKU DO JSONA:
            tree = ET.fromstring(data)

            lat = tree.find('result').find('geometry').find('location').find('lat').text
            lng = tree.find('result').find('geometry').find('location').find('lng').text
            location = tree.find('result').find('formatted_address').text

            lst= tree.find('result').findall('address_component')
            [print(x.find('short_name').text) if x.findall('type')[0].text=='country' else None for x in lst]

            print('lat', lat, 'lng', lng)
            print(location)
    #XMLgeocode_API_google_maps_WRAZ_API_KEY()
    def XML_zad1_findall_data_API():
        import urllib.request, urllib.parse, urllib.error
        import xml.etree.ElementTree as ET
        url='http://py4e-data.dr-chuck.net/comments_42.xml'
        url='http://py4e-data.dr-chuck.net/comments_1286490.xml'
        html =urllib.request.urlopen(url)
        xmlData= html.read().decode()
        xmlTree= ET.fromstring(xmlData)
        print(sum(map(int,[x.text for x in xmlTree.findall('.//count')])))
    #XML_zad1_findall_data_API()
    def JSON_zad2_API():
        import urllib.request, urllib.parse, urllib.error
        import json
        url='http://py4e-data.dr-chuck.net/comments_42.json'
        url='http://py4e-data.dr-chuck.net/comments_1286491.json'
        html=urllib.request.urlopen(url)
        jsonData=html.read().decode()
        jsonPython=json.loads(jsonData)
        print(sum([x["count"] for x in jsonPython["comments"]]))
    #JSON_zad2_API()
    def JSON_zad3_geocode_google_map_API():
        import urllib.request, urllib.parse, urllib.error
        import json
        #address= input("Enter location: ")
        address= 'Kent State University'
        api_key=False
        if api_key==False:
            api_key=42
            serviceurl='http://py4e-data.dr-chuck.net/json?'
        else:
            serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
        url=serviceurl+urllib.parse.urlencode({'address': address,'key':api_key})
        html=urllib.request.urlopen(url)
        jsonData=html.read().decode()
        jsonPython=json.loads(jsonData)
        print(jsonPython['results'][0]['place_id'])
    #JSON_zad3_geocode_google_map_API()
################################################################
def project1_column_calculator():
    #https://replit.com/@marekidziak1/boilerplate-arithmetic-formatter?v=1
    def README():
        '''### Assignment

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
```
  235
+  52
-----
```

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to `True`, the answers should be displayed.

### For example

Function Call:
```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:
```py
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

### Rules

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will **return** a **string** that describes an error that is meaningful to the user.


* Situations that will return an error:
  * If there are **too many problems** supplied to the function. The limit is **five**, anything more will return:
    `Error: Too many problems.`
  * The appropriate operators the function will accept are **addition** and **subtraction**. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
    `Error: Operator must be '+' or '-'.`
  * Each number (operand) should only contain digits. Otherwise, the function will return:
    `Error: Numbers must only contain digits.`
  * Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
    `Error: Numbers cannot be more than four digits.`
*  If the user supplied the correct format of problems, the conversion you return will follow these rules:
    * There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
    * Numbers should be right-aligned.
    * There should be four spaces between each problem.
    * There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

### Development

Write your code in `arithmetic_arranger.py`. For development, you can use `main.py` to test your `arithmetic_arranger()` function. Click the "run" button and `main.py` will run.

### Testing

The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.'''
    problems1 = ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]
    expected1 = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
    problems2 = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]
    expected2 = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"
    def arithmetic_arranger(problems, arg=False):
        if len(problems) > 5:
            return 'Error: Too many problems.'
        else:
            lst = list(zip(*[x.split() for x in problems]))
            arranged_problems = ""
            for x in lst[1]:
                if x == '*' or x == '/':
                    return 'Error: Operator must be \'+\' or \'-\'.'
            for i in range(len(problems)):
                if not lst[0][i].isdigit() or not lst[2][i].isdigit():
                    return 'Error: Numbers must only contain digits.'
                if len(lst[0][i]) > 4 or len(lst[2][i]) > 4:
                    return 'Error: Numbers cannot be more than four digits.'

            len_max_lst = [max(len(lst[0][i]), len(lst[2][i])) for i in range(len(problems))]

            ###############1st line
            for i in range(len(problems)):
                arranged_problems += lst[0][i].rjust(len_max_lst[i] + 2)
                if i < (len(problems) - 1):
                    arranged_problems += " " * 4
            arranged_problems += '\n'
            ###############2nd line
            for i in range(len(problems)):
                arranged_problems += lst[1][i] + " " + lst[2][i].rjust(len_max_lst[i])
                if i < (len(problems) - 1):
                    arranged_problems += " " * 4
            arranged_problems += '\n'
            ###############3rd line
            for i in range(len(problems)):
                arranged_problems += (len_max_lst[i] + 2) * "-"
                if i < (len(problems) - 1):
                    arranged_problems += " " * 4
            ###############4th line
            if arg == True:
                arranged_problems += '\n'
                for i in range(len(problems)):
                    if lst[1][i] == '+':
                        arranged_problems += str(int(lst[0][i]) + int(lst[2][i])).rjust(len_max_lst[i] + 2)
                    elif lst[1][i] == '-':
                        number = str(int(lst[0][i]) - int(lst[2][i]))
                        arranged_problems += number.rjust(len_max_lst[i] + 2)
                    else:
                        arranged_problems += (len_max_lst[i] + 2) * " "
                    if i < (len(problems) - 1):
                        arranged_problems += " " * 4
            return arranged_problems
    print(arithmetic_arranger(problems1),'\n')
    print(expected1,'\n')
    print()
    print(arithmetic_arranger(problems2,True),'\n')
    print(expected2,'\n')
#project1_column_calculator()
def project2_time_calculator():
    #https://replit.com/@marekidziak1/boilerplate-time-calculator?v=1
    def README():
        '''### Assignment

Write a function named `add_time` that takes in two required parameters and one optional parameter:
* a start time in the 12-hour clock format (ending in AM or PM)
* a duration time that indicates the number of hours and minutes
* (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show `(next day)` after the time. If the result will be more than one day later, it should show `(n days later)` after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.
```py
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

### Development

Write your code in `time_calculator.py`. For development, you can use `main.py` to test your `time_calculator()` function. Click the "run" button and `main.py` will run.

### Testing

The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.
'''
    def add_time(start, duration, weekday=""):
        # initialize:
        week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        import re
        start_H, start_M, zone = re.split(r"\s|:", start)
        start_H, start_M = int(start_H), int(start_M)
        h, m = map(int, duration.split(":"))
        if zone == 'PM':
            start_H += 12

        ##endTime - computing
        ##minutes
        end_M = start_M + m
        if end_M > 59:
            h += 1
            end_M -= 60
            ##hours
        end_H = start_H + h
        ##days
        end_D = 0
        if end_H > 24:
            end_D = end_H // 24
            end_H = end_H % 24
            ##zone
        if end_H > 12:
            end_H -= 12
            zone = 'PM'
        elif end_H == 12:
            zone = 'PM'
        elif end_H == 0:
            end_H = 12
            zone = 'AM'
        else:
            zone = 'AM'

        ### weekday
        for x in week.keys():
            if weekday != "" and week[x] == weekday.capitalize():
                index = (x + end_D) % 7
                weekday = ", " + week[index]

        ### return value
        end_H = str(end_H) + ":"
        end_M = "0" + str(end_M) if end_M < 10 else str(end_M)
        zone = " " + zone
        days_later = ""
        if end_D == 1:
            days_later = " (next day)"
        if end_D > 1:
            days_later = " (" + str(end_D) + " days later)"
        new_time = end_H + end_M + zone + weekday + days_later
        return new_time
    #tests:
    print(add_time("3:30 PM", "2:12"))
    print(add_time("11:40 AM", "0:25"))
    print(add_time("11:59 PM", "24:05"))
    print(add_time("2:59 AM", "24:00", "sunDay"))
    print(add_time("11:06 PM", "2:02","monDaY"))
    print(add_time("11:06 PM", "260:02","monDaY"))
#project2_time_calculator()
def project3_budget_app():
    #https://replit.com/@marekidziak1/boilerplate-budget-app?v=1
    def README():
        '''### Assignment

Complete the `Category` class in `budget.py`. It should be able to instantiate objects based on different budget categories like *food*, *clothing*, and *entertainment*. When objects are created, they are passed in the name of the category. The class should have an instance variable called `ledger` that is a list. The class should also contain the following methods:

* A `deposit` method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of `{"amount": amount, "description": description}`.
* A `withdraw` method that is similar to the `deposit` method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return `True` if the withdrawal took place, and `False` otherwise.
* A `get_balance` method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
* A `transfer` method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return `True` if the transfer took place, and `False` otherwise.
* A `check_funds` method that accepts an amount as an argument. It returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise. This method should be used by both the `withdraw` method and `transfer` method.

When the budget object is printed it should display:
* A title line of 30 characters where the name of the category is centered in a line of `*` characters.
* A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
* A line displaying the category total.

Here is an example of the output:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Besides the `Category` class, create a function (outside of the class) called `create_spend_chart` that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

```
Percentage spent by category
100|
 90|
 80|
 70|
 60| o
 50| o
 40| o
 30| o
 20| o  o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  A
     o  l  u
     o  o  t
     d  t  o
        h
        i
        n
        g
```

The unit tests for this project are in `test_module.py`.

### Development

Write your code in `budget.py`. For development, you can use `main.py` to test your `Category` class. Click the "run" button and `main.py` will run.

### Testing

We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.
'''
    class Category:
        def __init__(self, name):
            self.name=name
            self.ledger =[]
        def deposit(self, amount, description=""):
            self.ledger.append({"amount": amount, "description": description})
        def withdraw(self, amount, description=""):
            if not self.check_funds(amount):
                return False
            else:
                self.ledger.append({"amount": amount*(-1), "description": description})
                return True
        def transfer(self, amount, another_category):
            if not self.check_funds(amount):
                return False
            else:
                self.ledger.append({"amount": amount*(-1), "description": ("Transfer to "+another_category.name)})
                another_category.ledger.append({"amount": amount, "description": ("Transfer from "+self.name)})
                return True
        def get_balance(self):
            return sum([x["amount"] for x in self.ledger])
        def check_funds(self, amount):
            return amount<=self.get_balance()
        def __str__(self):
            value=self.name.center(30,"*") +"\n"
            for x in self.ledger:
                value+= (x["description"].ljust(23," ")[:23]+str("{:.2f}".format(float(x["amount"]),2)).rjust(7," ")[:7])+"\n"
            value+=("Total: "+str(self.get_balance()))
            return value
    def create_spend_chart(categories):
        ### logic:
        sum_every=[]
        for x in categories:
            sum_withdraws=0
            for i in range(len(x.ledger)):
                if x.ledger[i]["amount"]<0:
                    sum_withdraws+=(-1)*x.ledger[i]["amount"]
            sum_every.append(sum_withdraws)
        sumAll=sum([x for x in sum_every])
        percentage_every=[((x/sumAll)*100//10*10) for x in sum_every]

        ### percentage part
        result="Percentage spent by category\n"
        for i in range(100,-1,-10):
            result+= str(i).rjust(3," ")+"| "
            for x in percentage_every:
                if x>=i:
                    result+="o  "
                else:
                    result+="   "
            result+="\n"

        ### dashes and columns
        result+=(" "*4) +("-"*3*len(categories))+"-\n"
        length=max([len(x.name) for x in categories])
        names=[]
        for i in range(len(categories)):
            names.append(categories[i].name.ljust(length," "))
        i = 0
        for x in zip(*names):
            if i > 0:
                result+="\n"
            else:
                i+=1
            result+=" "*5
            for y in x:
                result+=y+(2*" ")
        return result

    #TEST - create_spend_chart
    food = Category("Food")
    entertainment = Category("Entertainment")
    clothes = Category("Clothes")
    food.deposit(1000, "initial deposit")
    entertainment.deposit(1000, "initial deposit")
    clothes.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(84.15, "gries")
    entertainment.withdraw(15.89, "restaurant and more food for dessert")
    entertainment.withdraw(154.89, "for dessert")
    clothes.withdraw(100.15, "clothes")
    clothes.withdraw(403.15, "cl")
    print(create_spend_chart([food,entertainment,clothes]))

    #TEST - class Category:
    print("*"*30)
    food.deposit(900, "deposit")
    food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
    food.transfer(20, entertainment)
    print(food.get_balance())
    print(entertainment.get_balance())
    print(food)
    print(entertainment)
#project3_budget_app()
def project4_shape_polymorphism():
    #https://replit.com/@marekidziak1/boilerplate-polygon-area-calculator?v=1
    def README():
        '''### Assignment

In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.

#### Rectangle class
When a Rectangle object is created, it should be initialized with `width` and `height` attributes. The class should also contain the following methods:
* `set_width`
* `set_height`
* `get_area`: Returns area (`width * height`)
* `get_perimeter`: Returns perimeter (`2 * width + 2 * height`)
* `get_diagonal`: Returns diagonal (`(width ** 2 + height ** 2) ** .5`)
* `get_picture`: Returns a string that represents the shape using lines of "\*". The number of lines should be equal to the height and the number of "\*" in each line should be equal to the width. There should be a new line (`\n`) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
* `get_amount_inside`: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

Additionally, if an instance of a Rectangle is represented as a string, it should look like: `Rectangle(width=5, height=10)`

#### Square class
The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The `__init__` method should store the side length in both the `width` and `height` attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a `set_side` method. If an instance of a Square is represented as a string, it should look like: `Square(side=9)`

Additionally, the `set_width` and `set_height` methods on the Square class should set both the width and height.

#### Usage example
```py
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```
That code should return:
```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

The unit tests for this project are in `test_module.py`.

### Development

Write your code in `shape_calculator.py`. For development, you can use `main.py` to test your `shape_calculator()` function. Click the "run" button and `main.py` will run.

### Testing

We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.'''
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def set_width(self, width):
            self.width = width

        def set_height(self, height):
            self.height = height

        def get_area(self):
            return self.width * self.height

        def get_perimeter(self):
            return 2 * self.width + 2 * self.height

        def get_diagonal(self):
            return (self.width ** 2 + self.height ** 2) ** .5

        def get_picture(self):
            if self.height > 50 or self.width > 50:
                return 'Too big for picture.'
            star = ""
            for i in range(self.height):
                for j in range(self.width):
                    star += '*'
                star += "\n"
            return star

        def get_amount_inside(self, Rectangle_obj):
            return (self.width * self.height) // (Rectangle_obj.height * Rectangle_obj.width)

        def __str__(self):
            return 'Rectangle(width={}, height={})'.format(self.width, self.height)

    class Square(Rectangle):
        def __init__(self, side):
            self.width = side
            self.height = side

        def set_height(self, side):
            self.width = side
            self.height = side

        def set_width(self, side):
            self.width = side
            self.height = side

        def set_side(self, side):
            self.width = side
            self.height = side

        def __str__(self):
            return 'Square(side={})'.format(self.height)

    rect = Rectangle(5, 10)
    print(rect.get_area())
    rect.set_width(3)
    print(rect.get_perimeter())
    print(rect)

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
#project4_shape_polymorphism()
def project5_probability_calculator():
    #https://replit.com/@marekidziak1/boilerplate-probability-calculator-1?v=1
    def README():
        '''### Assignment

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.

First, create a `Hat` class in `prob_calculator.py`. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:
```
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```

A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a `contents` instance variable. `contents` should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is `{"red": 2, "blue": 1}`, `contents` should be `["red", "red", "blue"]`.

The `Hat` class should have a `draw` method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from `contents` and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

Next, create an `experiment` function in `prob_calculator.py` (not inside the `Hat` class). This function should accept the following arguments:
* `hat`: A hat object containing balls that should be copied inside the function.
* `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set `expected_balls` to `{"blue":2, "red":1}`.
* `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
* `num_experiments`: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The `experiment` function should return a probability.

For example, let's say that you want to determine the probability of getting at least 2 red balls and 1 green ball when you draw 5 balls from a hat containing 6 black, 4 red, and 3 green. To do this, we perform `N` experiments, count how many times `M` we get at least 2 red balls and 1 green ball, and estimate the probability as `M/N`. Each experiment consists of starting with a hat containing the specified balls, drawing a number of balls, and checking if we got the balls we were attempting to draw.

Here is how you would call the `experiment` function based on the example above with 2000 experiments:

```
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

Since this is based on random draws, the probability will be slightly different each time the code is run.

*Hint: Consider using the modules that are already imported at the top of `prob_calculator.py`. Do not initialize random seed within `prob_calculator.py`.*

### Development

Write your code in `prob_calculator.py`. For development, you can use `main.py` to test your code. Click the "run" button and `main.py` will run.

### Testing

The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.'''
    import copy
    import random
    class Hat:
        def __init__(self, **kwargs):
            self.contents = []
            self.copy_contents = []
            for x in kwargs.keys():
                for i in range(kwargs[x]):
                    self.contents.append(x)
                    self.copy_contents.append(x)

        def __str__(self):
            return " ".join(self.contents)

        def draw(self, number):
            if int(number) > len(self.contents):
                number = len(self.contents)
            lst = []
            for i in range(number):
                rand_value = random.choice(self.contents)
                lst.append(rand_value)
                self.contents.remove(rand_value)
            return lst

    def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
        count = 0
        for i in range(num_experiments):
            hat_copy = copy.deepcopy(hat)
            expected_balls_copy = copy.deepcopy(expected_balls)
            returned_balls = hat_copy.draw(num_balls_drawn)
            for x in returned_balls:
                if x in expected_balls_copy:
                    expected_balls_copy[x] -= 1
            if all([x <= 0 for x in expected_balls_copy.values()]):
                count += 1
        return count / num_experiments
    ##################################
    random.seed(95)
    hat = Hat(blue=4, red=2, green=6)
    probability = experiment(
        hat=hat,
        expected_balls={"blue": 2,
                        "red": 1},
        num_balls_drawn=4,
        num_experiments=3000)
    print("Probability:", probability)
#project5_probability_calculator()

#lesson13_XML_JSON_API()
#lesson12Networking()
#lesson11REGEX()
#lesson10Tuple()
#lesson9Dictionaries()
#lesson8List()
#lesson7Files()
#lesson6String()
#lesson5WhileFor()
#lesson4Function()
#lesson3IfTry()