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
    print("Zrezygnowano z losowania. Wczytuje dane z txt")




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
    cmaxarray = [[0 for x in range(m + 1)] for y in range(n + 1)]
    tmparr = [[0 for x in range(m - 1)] for y in range(n)]

    for i in range(len(taskarray)):
        for j in range(len(taskarray[i])):
            if j == 0:
                taskarray[i][j] = i + 1
            else:
                taskarray[i][j] = int(tekst[1 + list_tmp[i] * ilosc_maszyn + j])

    for x in range(0, n):
        for y in range(0, m-1):
            tmparr[x][y] = taskarray[x][y+1]

    for x in range(0, n+1):
        for y in range(0, m+1):
            cmaxarray[x][y] = 0

    for x in range(1, n+1):
        for y in range(1, m):
            cmaxarray[x][y] = max(cmaxarray[x-1][y], cmaxarray[x][y-1]) + tmparr[x-1][y-1]

    #print('test', max(map(max, cmaxarray)))
    #print('taskarray',taskarray) #diagnostyka
    # machine1, machine2, machine3, machine4, machine5 = 0, 0, 0, 0, 0
    # machine6,machine7,machine8,machine9,machine10 = 0, 0, 0, 0, 0
    # machine11, machine12, machine13, machine14, machine15 = 0, 0, 0, 0, 0
    # machine16, machine17, machine18, machine19, machine20 = 0, 0, 0, 0, 0
    #
    # for x in range(0, n):
    #     machine1 += taskarray[x][1]
    #     if x == 0:
    #         machine2 = taskarray[x][1] + taskarray[x][2]
    #         machine3 = machine2 + taskarray[x][3]
    #         machine4 = machine3 + taskarray[x][4]
    #         machine5 = machine4 + taskarray[x][5]
    #         machine6 = machine5 + taskarray[x][6]
    #         machine7 = machine6 + taskarray[x][7]
    #         machine8 = machine7 + taskarray[x][8]
    #         machine9 = machine8 + taskarray[x][9]
    #         machine10 = machine9 + taskarray[x][10]
    #         machine11 = machine10 + taskarray[x][11]
    #         machine12 = machine11 + taskarray[x][12]
    #         machine13 = machine12 + taskarray[x][13]
    #         machine14 = machine13 + taskarray[x][14]
    #         machine15 = machine14 + taskarray[x][15]
    #         machine16 = machine15 + taskarray[x][16]
    #         machine17 = machine16 + taskarray[x][17]
    #         machine18 = machine17 + taskarray[x][18]
    #         machine19 = machine18 + taskarray[x][19]
    #         machine20 = machine19 + taskarray[x][20]
    #     else:
    #         if machine1 <= machine2:
    #             machine2 += taskarray[x][2]
    #         else:
    #             machine2 = machine1 + taskarray[x][2]
    #         if machine2 <= machine3:
    #             machine3 += taskarray[x][3]
    #         else:
    #             machine3 = machine2 + taskarray[x][3]
    #         if machine3 <= machine4:
    #             machine4 += taskarray[x][4]
    #         else:
    #             machine4 = machine3 + taskarray[x][4]
    #         if machine4 <= machine5:
    #             machine5 += taskarray[x][5]
    #         else:
    #             machine5 = machine4 + taskarray[x][5]
    #
    #         if machine5 <= machine6:
    #             machine6 += taskarray[x][6]
    #         else:
    #             machine6 = machine5 + taskarray[x][6]
    #
    #         if machine6 <= machine7:
    #             machine7 += taskarray[x][7]
    #         else:
    #             machine7 = machine6 + taskarray[x][7]
    #
    #         if machine7 <= machine8:
    #             machine8 += taskarray[x][8]
    #         else:
    #             machine8 = machine7 + taskarray[x][8]
    #
    #         if machine8 <= machine9:
    #             machine9 += taskarray[x][9]
    #         else:
    #             machine9 = machine8 + taskarray[x][9]
    #
    #         if machine9 <= machine10:
    #             machine10 += taskarray[x][10]
    #         else:
    #             machine10 = machine9 + taskarray[x][10]
    #
    #         if machine10 <= machine11:
    #             machine11 += taskarray[x][11]
    #         else:
    #             machine11 = machine10 + taskarray[x][11]
    #
    #         if machine11 <= machine12:
    #             machine12 += taskarray[x][12]
    #         else:
    #             machine12 = machine11 + taskarray[x][12]
    #
    #         if machine12 <= machine13:
    #             machine13 += taskarray[x][13]
    #         else:
    #             machine13 = machine12 + taskarray[x][13]
    #
    #         if machine13 <= machine14:
    #             machine14 += taskarray[x][14]
    #         else:
    #             machine14 = machine13 + taskarray[x][14]
    #
    #         if machine14 <= machine15:
    #             machine15 += taskarray[x][15]
    #         else:
    #             machine15 = machine14 + taskarray[x][15]
    #
    #         if machine15 <= machine16:
    #             machine16 += taskarray[x][16]
    #         else:
    #             machine16 = machine15 + taskarray[x][16]
    #
    #         if machine16 <= machine17:
    #             machine17 += taskarray[x][17]
    #         else:
    #             machine17 = machine16 + taskarray[x][17]
    #
    #         if machine17 <= machine18:
    #             machine18 += taskarray[x][18]
    #         else:
    #             machine18 = machine17 + taskarray[x][18]
    #
    #         if machine18 <= machine19:
    #             machine19 += taskarray[x][19]
    #         else:
    #             machine19 = machine18 + taskarray[x][19]
    #
    #         if machine19 <= machine20:
    #             machine20 += taskarray[x][20]
    #         else:
    #             machine20 = machine19 + taskarray[x][20]
    #print("Czas wykonywania to:",machine5) #diagnostyka
    zwroc=max(map(max, cmaxarray))
    return zwroc


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
    indeks_zad = 0 #deklaracja zm w funkcji

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
    else: #jesli dany czas wystepuje jeden raz na liscie
        indeks_zad=all_czas_zad.index(znaleziony_maks)
    return indeks_zad

def alg_neh(ilosc_zad):
    list_tmp=[]
    list_neh=[]
    all_czas_zad = []
    wykonanie=0

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

        #print('[END] LIST NEH i czas dla all',optymalne_czas, list_tmp)
        #print('[END] TIME AND LIST NEH', time1,list_tmp)

        list_neh.insert(time1.index(optymalne_czas), optymalne_zad) #umiesc na liscie NEH najlepsze przeanalizowane
                                                                    #zadanie wraz z jego najlepszym najlepszym
                                                                    #ustawieniem,aby uzyskac optymalny czas
        wykonanie += 1
        #print(wykonanie,'[END] KONIEC NORM ALG', calc_cmax(list_neh), list_neh)
        #a=input() #diagnostyka i "zatrzymywanie" petli

        ###########w tym miejscu algorytm NEH juz sie wykonal ################

    czas1= calc_cmax(list_neh)
    for x in range (len(list_neh)): #ostatecznie wypisz kolejke zadan z +1 (bo alg liczy od 0!)
        list_neh[x]+=1
    print('\nCzas wykonywania zadan na wszystkich maszynach dla alg NEH bez modyfikacji to:',czas1)
    print('Lista kolejki zadan otrzyma wg algorytmu NEH:\n',list_neh)
    return czas1

def alg_neh_dod_rozw(ilosc_zad):
    list_tmp=[]
    list_neh=[]
    all_czas_zad = []

    wykonanie=0 #zm. pomocnicza do obliczenia ile razy wykonal sie kod

    #zsumuj wszystkie czasy na maszynach dla poszczegolnych zadan i uwtorz liste
    for x in range(ilosc_zadan):
        czas = 0
        for y in range(ilosc_maszyn):
            czas += maszyny[x][y]
        all_czas_zad.append(czas)

    while len(list_tmp) != int(ilosc_zad-1): #dopóki elementow na liscie nie bedzie tyle, co realnych zadan
                                             #dopóty algorytm szuka rozwiazan

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


        nasz_index=time1.index(optymalne_czas)
        list_neh.insert(nasz_index, optymalne_zad) #umiesc na liscie NEH najlepsze przeanalizowane
        wykonanie+=1 #licz ilosc krokow
        #print(wykonanie,'[END] KONIEC NORM ALG', optymalne_czas, list_neh)


        #############################################
        #############################################
        #############################################
        #dodanie rozwiazania nr 4, czyli wybor i analiza
        #zadania, którego usunięcie spowoduję najwieksze zmniejszenie wartości Cmax.

        #zmienne do zapamietania najmniejszego cmaxa, gdy wyrzuci sie dane zadanie (rozw_dod_nr_zad o
        #indeksie równym rozw_dod_zapisz_index)
        best_time_normal, best_nr_zad, best_zapisz_index = 10000000000, 0, 0


        for a in range(len(list_neh)): #petla wykonuje sie dla zadan w aktualanym NEHu procz:
            if a != nasz_index:        #zadania, ktore zostalo ostatnio dodane (w wyoniku dzialania normalnego NEHa)
                zapisz_nr_zad=list_neh.pop(a) #sciagnij indeks a z tablicy NEHa, a nastepnie zapisz nr zadania
                best_time_act=calc_cmax(list_neh) #oblicz aktualny cmax
                #print('czas akt',best_time_act,'dla braku zad',zapisz_nr_zad) #diagnostyka

                if best_time_act < best_time_normal: #jesli cmax mniejszy niz aktualnie zapisany to zapamietaj dane
                    best_time_normal=best_time_act
                    best_nr_zad = zapisz_nr_zad
                    best_zapisz_index=a
                list_neh.insert(a,zapisz_nr_zad) #umiesc sciagniete wczesniej zadania z powrotem na liscie i analizuj

        #print('czas akt', best_time_normal, 'dla braku zad', best_nr_zad)  # diagnostyka

        if len(list_neh) != 1: #jesli lista NEH ma więcej w sobie zadan niz 1 to
            time1 = []         #wyzruj tablice do zapisywania czasow
            nr_zad=list_neh.pop(best_zapisz_index) #sciagnij z listy zadanie o wczesniej zapisanym indeksie i zapisz
                                                   # nr zadania
            optymalne_czas=1000000000
            for b in range(len(list_neh) + 1):
                list_neh.insert(b, nr_zad)
                time1.append(calc_cmax(list_neh))
                #print(list_neh,'dal ustawienia, czas taki:',calc_cmax(list_neh)) #diagnostyka
                if optymalne_czas > time1[b]:
                    best_nr_zad = list_neh[b]
                    optymalne_czas = time1[b]
                list_neh.remove(nr_zad)

            list_neh.insert(time1.index(optymalne_czas),best_nr_zad)  # umiesc na liscie NEH najlepszy przypadek
            #print('   [END] CZAS I LISTA PO', calc_cmax(list_neh), list_neh,'\n')
        #sa=input() #diagnostyka

        ###########w tym miejscu algorytm NEH juz sie wykonal ################

    czas2= calc_cmax(list_neh)
    for x in range (len(list_neh)): #ostatecznie wypisz kolejke zadan z +1 (bo alg liczy od 0!)
        list_neh[x]+=1
    print('',list_neh)
    print('Lista kolejki zadan otrzyma wg algorytmu NEH z rozw. dod. widoczna u gory')
    print('Czas wykonywania zadan na wszystkich maszynach dla NEH z rozw. dod. to:',czas2)
    return czas2

czas1,czas2=0,0
start = time.time() #czas obliczania wykonywania sie algorytmu
czas1=alg_neh(len(kolejka_zadan)) #wykonaj alg_neh tyle razy, co jest zadan
end = time.time()

norm_neh=end-start

start = time.time() #czas obliczania wykonywania sie algorytmu
czas2=alg_neh_dod_rozw(len(kolejka_zadan)) #wykonaj alg_neh tyle razy, co jest zadan
end = time.time()

neh_dod_rozw=end-start

print("\nIlosc zadan to",ilosc_zadan,"a ilosc maszyn to",ilosc_maszyn)
print("Czas dzialania dla algorytmu NEH to:", norm_neh,"s")
print("Czas dzialania dla algorytmu NEH z dod. rozw. to:", neh_dod_rozw,"s")
print('Roznica dla czasow dzialania alg to:',neh_dod_rozw-norm_neh,'s')
print('Roznica dla czasu wykonywania zadan na maszynach w zaleznosci od alg. to:',czas1-czas2)
