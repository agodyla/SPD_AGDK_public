import random as losuj
import time, copy


plik = open('parametry.txt')
try:
    tekst = plik.read()
finally:
    plik.close()  # finalnie zamknij plik

tekst=tekst.split() #zrob z pojedynczych wyrazow z stringa liste

#funkcja do losowania
print("Jesli chcesz losowac to wpisz 1, jesli nie to wpisz cokolwiek innego.")
wybor="3" #input() #na sztywno przypisany brak losowania, co daje ciagly odczyt z pliku txt


if wybor == "1":
    print("Zaczynam losowac")

    '''print("Wpisz zadana ilosc maszyn (oecnie 2 lub 3):")
    daj_ilosc_maszyn=int(input())
    print("Wpisz zadany zakres czasowy pojedynczego zadania:")
    los_zakres=int(input())
    print("Wpisz ilosc zadan do wylosowania:")
    los_ilosc_zad=int(input())
    '''

    daj_ilosc_maszyn=int(3)
    los_zakres=int(10)
    los_ilosc_zad=int(9)

    tekst[0]=int(los_ilosc_zad)
    tekst[1]=int(daj_ilosc_maszyn)
    ilosc_osobnych_prac=los_ilosc_zad*daj_ilosc_maszyn

    for x in range(2,ilosc_osobnych_prac+2):
        try:
            tekst[x]=int(losuj.uniform(1,los_zakres)) #losuj losowy zakres od 1h do xh
        except:
            tekst.append(int(losuj.uniform(1, los_zakres) ) ) #jako, ze i tak zawsze jest odczytywany plik txt,
                                                              #jesli jego zakres jest zbyt maly do napisania
                                                              #to algorytm stworzy sobie dodatkowe miejsce
    print("Skonczylem losowac.\n")

else:
    print("Zrezygnowano z losowania. Wczytuje pliki z txt")


start = time.time() #czas obliczania wykonywania sie algorytmu

ilosc_zadan = int(tekst[0])
ilosc_maszyn = int(tekst[1])

#inicjacja macierzy do pozniejszego wczytywania maszyn
maszyny=[[0 for x in range(ilosc_maszyn)] for y in range(ilosc_zadan)]


#do wczesniej stworzonej macierzy wpisuj po kolei czas wykonywania danego zadania na odpowiednich maszynach
for x in range (ilosc_zadan):
    listatmp = []
    for i in range (ilosc_maszyn):
        listatmp.append(int(tekst[i+2+x*ilosc_maszyn])) #wkona sie tyle razy, co jest zadan
    maszyny[x]=listatmp #przepisywanie z listy temp

#helparray = [[0 for x in range(ilosc_maszyn)] for y in range(ilosc_zadan)]

#stworz kolejke zadan na podstawie ilosci zadan (niezbedne do NEHa)
kolejka_zadan=[]
for x in range(ilosc_zadan):
    kolejka_zadan.append(x)
print(kolejka_zadan)

###################################
###################################
###################################
###################################
        #REALIZACJA NEHA#
###################################
###################################
###################################


def calc_cmax(list_tmp):
    m=ilosc_maszyn+1
    n=len(list_tmp)
    taskarray = [[0 for x in range(m)] for y in range(n)]

    for i in range(len(taskarray)):
        for j in range(len(taskarray[i])):
            if j == 0:
                taskarray[i][j] = i + 1
            else:
                taskarray[i][j] = int(tekst[1 + list_tmp[i] * ilosc_maszyn + j])

    #print('taskarray',taskarray) #diagnostyka

    machine1, machine2, machine3, machine4, machine5 = 0, 0, 0, 0, 0

    for x in range(0, n):
        machine1 += taskarray[x][1]
        if x == 0:
            machine2 = taskarray[x][1] + taskarray[x][2]
            machine3 = machine2 + taskarray[x][3]
            machine4 = machine3 + taskarray[x][4]
            machine5 = machine4 + taskarray[x][5]
        else:
            if machine1 <= machine2:
                machine2 += taskarray[x][2]
            else:
                machine2 = machine1 + taskarray[x][2]
            if machine2 <= machine3:
                machine3 += taskarray[x][3]
            else:
                machine3 = machine2 + taskarray[x][3]
            if machine3 <= machine4:
                machine4 += taskarray[x][4]
            else:
                machine4 = machine3 + taskarray[x][4]
            if machine4 <= machine5:
                machine5 += taskarray[x][5]
            else:
                machine5 = machine4 + taskarray[x][5]

    #print("Czas wykonywania to:",machine5) #diagnostyka
    return machine5 #narazie zawsze machine5, ale trzeba to zrobic uniwersalne


def find_max(list_neh,all_czas_zad):
    max_time=0
    for x in range (ilosc_zadan): # szukaj najdluzszego zadania w zadaniach
        if all_czas_zad[x]>max_time: # jesli analizowane zad. jest dluzsze niz przyjete wczesniej to

            badany_czas = all_czas_zad[x] #zapisz akt. badana wartosc
            nr_zad_bad_czasu=all_czas_zad.index(badany_czas) #zdabac jej indeks na podstawie listy all zadania
            ilosc_powt=all_czas_zad.count(badany_czas) #zbadaj czy nie powtarza sie

            # ilosc wystapien zadania na nehu
            if list_neh.count(nr_zad_bad_czasu) == 0: #zadanie nie wystapilo w liscei neh
                max_time=badany_czas

            elif ilosc_powt> 1: #zadanie przynajmniej 2 razy wystapilo w liscie neh
                lista_tmp1 = copy.deepcopy(all_czas_zad)
                lista_tmp2 = []
                ilosc_powt_akt = all_czas_zad.count(badany_czas)
                for i in range(ilosc_powt_akt): #spisz do lista_tmp2 wszystkie indeksy zadan, ktore maja taki sam czas
                    #jako, ze index zawsze zwraca indeks 1. napotkanego elementu to zapamietuje go na osobnej liscie
                    #a nastepnie go kasuje z tej pierwotnej(lista_tmp1), aby dostac sie do kolejnych indeksow zadan
                    #tablice sa tymczasowe, wiec nienaruszam glownych list z zadaniami
                    lista_tmp2.append(lista_tmp1.index(badany_czas) + i)
                    lista_tmp1.remove(badany_czas)

                for k in range(len(lista_tmp2)):
                    if list_neh.count(lista_tmp2[k]) == 0:
                        max_time = badany_czas #jesli zadanie o danym czasie jeszcze nie pojawilo sie w liscie neh to
                                               #zapamietaj czas
    #print("maxTIME", max_time) #diagnostyka
    return max_time

def nr_zadania(list_neh,znaleziony_maks,all_czas_zad):
    if all_czas_zad.count(znaleziony_maks) > 1: # jesli dany czas wystepuje wiecej niz 1. raz na liscie sumy czasu zadan
        lista_tmp1 = copy.deepcopy(all_czas_zad)
        lista_tmp2=[]
        ilosc_powtorzen_all = all_czas_zad.count(znaleziony_maks)
        #analogia do find maxa, z ta roznica, ze tutaj nie zwracamy czasu, a nr zadania
        for i in range(ilosc_powtorzen_all):
            lista_tmp2.append(lista_tmp1.index(znaleziony_maks)+i)
            lista_tmp1.remove(znaleziony_maks)
        for x in range(len(lista_tmp2)):
            if list_neh.count(lista_tmp2[x]) == 0:
                indeks_zad = lista_tmp2[x]
                break
    else:
        indeks_zad=all_czas_zad.index(znaleziony_maks)
    return indeks_zad


def alg_neh(ilosc_zad):
    list_tmp=[]
    list_neh=[]
    all_czas_zad = []

    #zsumuj wszystkie czasy na maszynach dla poszczegolnych zadani i uwtorz liste
    for x in range(ilosc_zadan):
        czas = 0
        for y in range(ilosc_maszyn):
            czas += maszyny[x][y]
        all_czas_zad.append(czas)

    while len(list_tmp) != int(ilosc_zad-1): #dopki elementow na liscie nie bedzie tyle, co realnych zadan
                                             #dopty algorytm szuka rozwiazan

        list_tmp=copy.deepcopy(list_neh)     #deepcopy uzyta, aby kopiowac, a nie ODWOLYWAC się do list/macierzy
                                             #W tym miejscu przypisujemy na poczatku zapisana juz liste zadan wg NEH
                                             #i do tej listy probnie bedziemy chcieli umieszczac kolejne zadania
                                             #a nastepnie patrzec na rezultat

        optymalne_zad = ilosc_zadan + 1      #do porwnania
        optymalne_czas = 10000000            #mozna zastapic wyszukiwaniem maksa
        time1=[] #do zliczania i porywnywania danych czasow w zaleznosci od tego, gdzie wstawimy aktualnie analizowane
                 #zadanie

        #print('BEGIN LIST TMP',list_tmp)    #diagnostyka

        for x in range (len(list_neh)+1):
            znaleziony_maks=find_max(list_neh,all_czas_zad) #znajdz i zapisz maksymalny czas danego zadania
            nr_akt_zad=nr_zadania(list_neh,znaleziony_maks,all_czas_zad) # znajdz nr zadania na podstawie jego czasu
            list_tmp.insert(x, nr_akt_zad) #umiesc analizowane zadania w dowolonym dostepnym miejscu w liscie tmp
            #w celu pozniejszego sprawdzenia, ktory czas wykonywania bedzie najszybszy

            time1.append(calc_cmax(list_tmp)) #oblicz i zapisz czas wykonywanie zadan dla aktualnej kolejki zadan
            if optymalne_czas>time1[x]:       #jesli analizowany czas jest lepszy od innych do go zapamietaj
                optymalne_zad=list_tmp[x]
                optymalne_czas=time1[x]
            list_tmp.remove(nr_akt_zad)       #skasuj nr akt. zadania z kolejki tmp, aby w wyniku wykonywania
            # petliu for wstawic go w inne miejsce (list_tmp.insert)

        print('[END] LIST NEH', list_tmp)
        #print('[END] TIME AND LIST NEH', time1,list_tmp)

        list_neh.insert(time1.index(optymalne_czas), optymalne_zad) #umiesc na liscie NEH najlepsze przeanalizowane
                                                                    #zadanie wraz z jego najlepszym najlepszym
                                                                    #ustawieniem,aby uzyskac optymalny czas
        # a=input() #diagnostyka i "zatrzymywanie" petli

        ###########w tym miejscu algorytm NEH juz sie wykonal ################
    for x in range (len(list_neh)): #ostatecznie wypisz kolejke zadan z +1 (bo alg liczy od 0!)
        list_neh[x]+=1
    print('Lista kolejki zadan otrzyma wg algorytmu NEH:\n',list_neh)


alg_neh(len(kolejka_zadan)) #wykonaj alg_neh tyle razy, co jest zadan

end = time.time()
print("Czas dzialania dla algorytmu NEH to: ", end-start,"s\n")
print("Ilosc zadan to",ilosc_zadan,"a ilosc maszyn to",ilosc_maszyn)