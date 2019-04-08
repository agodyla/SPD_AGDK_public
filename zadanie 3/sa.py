import random as losuj
import time, copy, math


plik = open('parametry.txt')
try:
    tekst = plik.read()
finally:
    plik.close()  # finalnie zamknij plik

tekst=tekst.split() #zrob z pojedynczych wyrazow z stringa liste

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

def calc_cmax(list_tmp):
    cmax_final=0
    m=ilosc_maszyn+1
    n=len(list_tmp)
    taskarray = [[0 for x in range(m)] for y in range(n)]

    for i in range(len(taskarray)):
        for j in range(len(taskarray[i])):
            if j == 0:
                taskarray[i][j] = i + 1
            else:
                taskarray[i][j] = int(tekst[1 + list_tmp[i] * ilosc_maszyn + j])

    machine1, machine2, machine3, machine4, machine5 = 0, 0, 0, 0, 0
    if m > 5:
        machine6,machine7,machine8,machine9,machine10 = 0, 0, 0, 0, 0
    if m > 10:
        machine11, machine12, machine13, machine14, machine15 = 0, 0, 0, 0, 0
    if m > 20:
        machine16, machine17, machine18, machine19, machine20 = 0, 0, 0, 0, 0

    for x in range(0, n):
        machine1 += taskarray[x][1]
        if x == 0:
            if m == 3:
                machine2 = taskarray[x][1] + taskarray[x][2]
            if m==4:
                machine2 = taskarray[x][1] + taskarray[x][2]
                machine3 = machine2 + taskarray[x][3]
            if m==6:
                machine2 = taskarray[x][1] + taskarray[x][2]
                machine3 = machine2 + taskarray[x][3]
                machine4 = machine3 + taskarray[x][4]
                machine5 = machine4 + taskarray[x][5]
            elif m==11:
                machine2 = taskarray[x][1] + taskarray[x][2]
                machine3 = machine2 + taskarray[x][3]
                machine4 = machine3 + taskarray[x][4]
                machine5 = machine4 + taskarray[x][5]
                machine6 = machine5 + taskarray[x][6]
                machine7 = machine6 + taskarray[x][7]
                machine8 = machine7 + taskarray[x][8]
                machine9 = machine8 + taskarray[x][9]
                machine10 = machine9 + taskarray[x][10]
            elif m==21:
                machine2 = taskarray[x][1] + taskarray[x][2]
                machine3 = machine2 + taskarray[x][3]
                machine4 = machine3 + taskarray[x][4]
                machine5 = machine4 + taskarray[x][5]
                machine6 = machine5 + taskarray[x][6]
                machine7 = machine6 + taskarray[x][7]
                machine8 = machine7 + taskarray[x][8]
                machine9 = machine8 + taskarray[x][9]
                machine10 = machine9 + taskarray[x][10]
                machine11 = machine10 + taskarray[x][11]
                machine12 = machine11 + taskarray[x][12]
                machine13 = machine12 + taskarray[x][13]
                machine14 = machine13 + taskarray[x][14]
                machine15 = machine14 + taskarray[x][15]
                machine16 = machine15 + taskarray[x][16]
                machine17 = machine16 + taskarray[x][17]
                machine18 = machine17 + taskarray[x][18]
                machine19 = machine18 + taskarray[x][19]
                machine20 = machine19 + taskarray[x][20]
        else:
            if m == 3:
                if machine1 <= machine2:
                    machine2 += taskarray[x][2]
                else:
                    machine2 = machine1 + taskarray[x][2]
                cmax_final=machine2
            if m == 4:
                if machine1 <= machine2:
                    machine2 += taskarray[x][2]
                else:
                    machine2 = machine1 + taskarray[x][2]
                if machine2 <= machine3:
                    machine3 += taskarray[x][3]
                else:
                    machine3 = machine2 + taskarray[x][3]
                cmax_final=machine3
            elif m == 6:
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
                cmax_final=machine5

            elif m == 11:
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

                    if machine5 <= machine6:
                        machine6 += taskarray[x][6]
                    else:
                        machine6 = machine5 + taskarray[x][6]

                    if machine6 <= machine7:
                        machine7 += taskarray[x][7]
                    else:
                        machine7 = machine6 + taskarray[x][7]

                    if machine7 <= machine8:
                        machine8 += taskarray[x][8]
                    else:
                        machine8 = machine7 + taskarray[x][8]

                    if machine8 <= machine9:
                        machine9 += taskarray[x][9]
                    else:
                        machine9 = machine8 + taskarray[x][9]

                    if machine9 <= machine10:
                        machine10 += taskarray[x][10]
                    else:
                        machine10 = machine9 + taskarray[x][10]
                    cmax_final=machine10

            elif m == 21:
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

                    if machine5 <= machine6:
                        machine6 += taskarray[x][6]
                    else:
                        machine6 = machine5 + taskarray[x][6]

                    if machine6 <= machine7:
                        machine7 += taskarray[x][7]
                    else:
                        machine7 = machine6 + taskarray[x][7]

                    if machine7 <= machine8:
                        machine8 += taskarray[x][8]
                    else:
                        machine8 = machine7 + taskarray[x][8]

                    if machine8 <= machine9:
                        machine9 += taskarray[x][9]
                    else:
                        machine9 = machine8 + taskarray[x][9]

                    if machine9 <= machine10:
                        machine10 += taskarray[x][10]
                    else:
                        machine10 = machine9 + taskarray[x][10]

                    if machine10 <= machine11:
                        machine11 += taskarray[x][11]
                    else:
                        machine11 = machine10 + taskarray[x][11]

                    if machine11 <= machine12:
                        machine12 += taskarray[x][12]
                    else:
                        machine12 = machine11 + taskarray[x][12]

                    if machine12 <= machine13:
                        machine13 += taskarray[x][13]
                    else:
                        machine13 = machine12 + taskarray[x][13]

                    if machine13 <= machine14:
                        machine14 += taskarray[x][14]
                    else:
                        machine14 = machine13 + taskarray[x][14]

                    if machine14 <= machine15:
                        machine15 += taskarray[x][15]
                    else:
                        machine15 = machine14 + taskarray[x][15]

                    if machine15 <= machine16:
                        machine16 += taskarray[x][16]
                    else:
                        machine16 = machine15 + taskarray[x][16]

                    if machine16 <= machine17:
                        machine17 += taskarray[x][17]
                    else:
                        machine17 = machine16 + taskarray[x][17]

                    if machine17 <= machine18:
                        machine18 += taskarray[x][18]
                    else:
                        machine18 = machine17 + taskarray[x][18]

                    if machine18 <= machine19:
                        machine19 += taskarray[x][19]
                    else:
                        machine19 = machine18 + taskarray[x][19]

                    if machine19 <= machine20:
                        machine20 += taskarray[x][20]
                    else:
                        machine20 = machine19 + taskarray[x][20]
                    cmax_final=machine20

    return cmax_final


#Symulowane wyzarzanie
def sym_wyz(ilosc_zadan,temperatura,wspol_schladzania,wybor): #dl_kolejki,wybor temp,schladzanie,wybor insert(1),swap(2)
    print('Algorytm zaczyna prace!\n')
    print('Cmax best   Cmax aktualny')

    start = time.time() #czas do timera podsumowującego czas pracy alg.

    #zmienne pomocnicze
    list_zad_los = []
    list_zad_los_tmp = []
    bez_rezultatu=0
    ilosc_interacji=0 #poczatkowa ilosc iteracji
    ilosc_powtorzen=130000 # maks. ilosc iteracji
    wyb=2

    #etap 1 Inicjalizacja
    for x in range (ilosc_zadan): #tworzenie listy zadan od 0 do tyle ile
        list_zad_los.append(x)    #!!!zadan po kolei!!!

    losuj.shuffle(list_zad_los) #losowe rozstawienie zadan

    # lista z NEHa bez modyfikacji, ta_098, cmax - 10 829
    # list_zad_los=[150, 42, 104, 18, 153, 167, 162, 179, 100, 178, 1, 155, 169, 130, 64, 46, 196, 183, 188, 65, 7, 82, 69, 59, 136, 117, 61, 15, 190, 25, 189, 91, 84, 86, 27, 128, 54, 23, 118, 115, 93, 101, 127, 140, 105, 44, 71, 28, 32, 72, 119, 6, 149, 20, 9, 50, 47, 30, 131, 194, 21, 133, 191, 8, 176, 158, 99, 121, 134, 94, 19, 79, 56, 109, 88, 125, 63, 80, 164, 70, 106, 22, 114, 159, 12, 53, 98, 39, 154, 185, 76, 36, 132, 186, 120, 116, 148, 129, 52, 192, 157, 58, 122, 137, 103, 49, 5, 14, 77, 163, 34, 171, 123, 112, 13, 40, 156, 31, 41, 85, 2, 38, 141, 139, 135, 161, 187, 173, 16, 126, 97, 68, 160, 35, 60, 145, 90, 78, 177, 146, 11, 174, 199, 26, 197, 4, 170, 172, 198, 144, 62, 138, 87, 193, 108, 51, 143, 43, 96, 55, 195, 29, 168, 45, 182, 75, 142, 92, 184, 102, 95, 83, 10, 147, 110, 124, 3, 111, 151, 73, 166, 175, 74, 180, 81, 67, 24, 165, 113, 48, 33, 89, 0, 17, 66, 37, 57, 152, 181, 107]

    # lista z NEHa z modyfikacja, ta_098, cmax - 10 808
    # list_zad_los = [113, 57, 42, 153, 22, 37, 151, 18, 130, 180, 167, 111, 121, 123, 64, 117, 72, 74, 46, 150, 100, 65, 24, 81, 142, 169, 15, 1, 162, 84, 3, 196, 105, 124, 140, 34, 149, 136, 27, 49, 67, 163, 61, 69, 183, 91, 155, 190, 141, 86, 54, 9, 127, 44, 191, 110, 115, 187, 32, 186, 39, 48, 71, 14, 6, 128, 82, 77, 20, 28, 25, 119, 181, 7, 189, 188, 159, 17, 139, 118, 131, 176, 194, 51, 63, 50, 138, 164, 30, 116, 56, 12, 173, 87, 158, 26, 45, 23, 172, 112, 70, 157, 85, 83, 21, 76, 179, 106, 177, 132, 89, 120, 98, 92, 52, 137, 129, 198, 5, 88, 4, 103, 16, 175, 135, 161, 126, 185, 122, 41, 36, 94, 35, 160, 53, 31, 80, 60, 40, 19, 125, 2, 58, 96, 193, 114, 171, 146, 197, 109, 154, 68, 199, 38, 62, 192, 99, 145, 90, 55, 165, 13, 170, 144, 108, 174, 143, 79, 11, 8, 133, 97, 43, 78, 47, 195, 29, 168, 101, 148, 166, 93, 134, 178, 156, 102, 95, 10, 184, 59, 182, 75, 33, 66, 152, 73, 147, 104, 0, 107]

    cmax_akt = calc_cmax(list_zad_los) #obliczenie cmaxa na poczatek
    cmax_best=cmax_akt #przypisanie cmaxa akt do best przy poczatku dzialania alg.

    while ilosc_interacji != ilosc_powtorzen: #dopoki ilosc wykonania petli != ilosc_powtorzen, to dzialaj
        # etap2 generowanie ruchu

        if wybor == 1:   # insert
            list_zad_los_tmp=copy.deepcopy(list_zad_los) #kopiowanie (a nie wskaznik na liste!)
            zdejmij_zadanie = losuj.randint(0, ilosc_zadan - 1) #losowanie indeksu do zdjecia
            nr_zadania=list_zad_los_tmp.pop(zdejmij_zadanie) #zdjecie danego zadania z listy
            list_zad_los_tmp.insert(losuj.randint(0,ilosc_zadan-1),nr_zadania) #umiesc zdjete zadanie w losowym miejscu

        elif wybor == 2: # swap
            list_zad_los_tmp = copy.deepcopy(list_zad_los)
            miejsce_1 = losuj.randint(0, ilosc_zadan - 1) #losowy wybor nr indeksow do swapa
            miejsce_2 = losuj.randint(0, ilosc_zadan - 1)

            while miejsce_1 == miejsce_2: #gdyby oba zadania mialy taka sama wylosowana wartosc to losuj dalej
                miejsce_2 = losuj.randint(0, ilosc_zadan - 1)

            #operacja swap
            list_zad_los_tmp[miejsce_1],list_zad_los_tmp[miejsce_2]=list_zad_los_tmp[miejsce_2],list_zad_los_tmp[miejsce_1]


        # obliczenie cmaxa po operacji insert/swap
        cmax_akt = calc_cmax(list_zad_los_tmp)

        maks_ilosc_prob=30
        akt_ilosc_prob=0

        while (cmax_best == cmax_akt): #gdyby cmax po oepracji swpa/insert byl taki sam, to ponownie przeprowadz operacje
                                       #insert/swap az do skutku!
            # print('camaxy takie same!')
            # insert
            if wybor == 1:
                list_zad_los_tmp = copy.deepcopy(list_zad_los)
                zdejmij_zadanie = losuj.randint(0, ilosc_zadan - 1)
                nr_zadania = list_zad_los_tmp.pop(zdejmij_zadanie)
                list_zad_los_tmp.insert(losuj.randint(0, ilosc_zadan - 1), nr_zadania)
            # swap
            elif wybor == 2:
                list_zad_los_tmp = copy.deepcopy(list_zad_los)
                miejsce_1 = losuj.randint(0, ilosc_zadan - 1)
                miejsce_2 = losuj.randint(0, ilosc_zadan - 1)
                while miejsce_1 == miejsce_2:  # gdyby oba zadania mialy taka sama wylosowana wartosc
                    miejsce_2 = losuj.randint(0, ilosc_zadan - 1)
                list_zad_los_tmp[miejsce_1], list_zad_los_tmp[miejsce_2] = list_zad_los_tmp[miejsce_2], \
                                                                           list_zad_los_tmp[miejsce_1]
            cmax_akt = calc_cmax(list_zad_los_tmp) #na koniec petli policz nowy cmax_akt
            akt_ilosc_prob += 1
            if maks_ilosc_prob == akt_ilosc_prob: # jesli algorytm probuje ponad 30 razy bez skutku to:
                cmax_akt+=1 #aby wyjsc z poszukiwania nowego cmaxa, przydaje sie przy skrajnie malej ilosci zadam/maszyn

        #etap 3 liczenie prawdopodobienstwa i decyzja o ruchu

        ################################### Dodatkowy algorytm I-MSAA (Boltzman) ###################################
        Boltzman =0
        war_do_prawd=0
        if wyb==2:
            if temperatura < 9e-320: #break ze wzgledu na zbyt niska temp.
                break
            elif temperatura == 0: # gdyby temp. szybko przeskoczyla wartosc 9e-330 i stala sie 0
                break
            else:
                war_do_prawd=(cmax_akt - cmax_best) / temperatura #do exp-onenty
                if war_do_prawd > 709:
                    war_do_prawd=709 #limit liczenia e^(709)

            if cmax_akt - cmax_best <= 0:
                Boltzman = 1
            else:
                Boltzman = 1/(1+2*math.exp(war_do_prawd))

            if Boltzman > losuj.uniform(0,0.33): #warunek wykonania zamiany, jesli cmax_akt - cmax_best > 0
                    print(' ',cmax_best,'        ',cmax_akt,'  Iteracja nr {0}, wybor trybu {1}, wstawianie {2} '.format(ilosc_interacji,wyb,wybor))
                    cmax_best=cmax_akt
                    list_zad_los=copy.deepcopy(list_zad_los_tmp)
                    bez_rezultatu=1 #restart rezultatu
            else:
                bez_rezultatu+=1 #jesli nie dokonano ifa (brak zmiany analizowanej kolejki), do rozpatrywanych dalej modyfikacji


        ################################### z intrukcji (PDF) ###################################
        # if wyb ==1:
        #     war_do_prawd=0
        #     if temperatura < 9e-320: #break ze wzgledu na zbyt niska temp.
        #         break
        #     elif temperatura == 0: # gdyby temp. szybko przeskoczyla wartosc 9e-330 i stala sie 0
        #         break
        #     else:
        #         war_do_prawd=(cmax_akt - cmax_best) / temperatura #do exp-onenty
        #         if war_do_prawd > 709:
        #             war_do_prawd=709 #limit liczenia e^(709)
        #
        #     if cmax_akt < cmax_best:
        #         prawd=1
        #     else:
        #         prawd = math.exp(war_do_prawd)
        #
        #     if prawd >= losuj.uniform(0,1): #od pewnego momentu exp zawsze > 1 i dzieje sie bledne dzialnie
        #                                     #co mozna zauwazyc podczas dzialania funkcji
        #         print(' ',cmax_best,'        ',cmax_akt,'  Iteracja nr {0}, wybor trybu {1}, wstawianie {2} '.format(ilosc_interacji,wyb,wybor))
        #         cmax_best=cmax_akt
        #         list_zad_los=copy.deepcopy(list_zad_los_tmp)
        #         bez_rezultatu=1
        #     else:
        #         bez_rezultatu+=1
        ## etap 3 bazujacy na porownywaniu tylko cmaxow bez temp.
        # if cmax_akt < cmax_best:
        #     print(' ',cmax_best,'        ',cmax_akt)
        #     cmax_best=cmax_akt
        #     list_zad_los=copy.deepcopy(list_zad_los_tmp)

        #################
        ################# etap 3.5 - wlasne modyfikacje (a raczej proby)
        #################

        ## proba modyfikacji nr 1
        # if math.fmod(bez_rezultatu,6500) == 0:
        #     print('zmiana insert/swap','      Iteracja nr {0}'.format(ilosc_interacji))
        #     if wybor == 1:
        #         wybor=2
        #     else:
        #         wybor=1

        ## proba modyfikacji nr 2
        # if bez_rezultatu == 40000:
        #     print('zmiana tablic i bez_rezultatu=0')
        #     list_zad_los = copy.deepcopy(old_best_kolejka) #trzeba zaimplementowac old_best_kolejka

        ## proba modyfikacji nr 3 - DOSC UDANA
        if bez_rezultatu == 1:
            # print('przelaczam na insert')
            wybor = 1
        if bez_rezultatu == 20000 or (ilosc_interacji>70000 and bez_rezultatu > 5000):
            wybor = 2
            if bez_rezultatu == 20000:
                print('przelaczam na swap')

        ## proba modyfikacji nr 4 - DOSC UDANA
        if bez_rezultatu > 40000 or ilosc_interacji>100000:
            wybor = losuj.randint(1, 2)
        if bez_rezultatu == 20000:
            print('przelaczam na insert')
            wybor = 1
        #
        ## proba modyfikacji nr 5
        # '''if bez_rezultatu == 30000 and ilosc_interacji<80000:
        #     list_zad_los=[]
        #     for x in range(ilosc_zadan):  # tworzenie listy zadan od 0 do tyle ile zadan
        #         list_zad_los.append(x)
        #     cmax_best = calc_cmax(list_zad_los)
        #     cmax_akt = calc_cmax(list_zad_los)
        #     print('Losowanie od nowa!')
        #     bez_rezultatu=0'''
        #
        ## proba modyfikacji nr 6
        # if math.fmod(bez_rezultatu,2500) == 0:
        #     if bez_rezultatu >= 10000:
        #         wyb = 1
        #         if bez_rezultatu == 10000:
        #             print('tryb pdf')
        #
        #     elif wyb == 1:
        #         print('tryb Boltzman')
        #         wyb =2
        #     else:
        #         print('tryb pdf')
        #         wyb=1

        #po 5k iterecji wyswietlij, ze juz minelo tyle iteracji
        if math.fmod(ilosc_interacji, 5000) == 0:
            print('Iteracja:',ilosc_interacji)

        #etap 4 schladzanie
        ilosc_interacji += 1
        if wspol_schladzania == 0: #jesli nie wybrano wspolczynnika schladzania
            schladzanie = temperatura*ilosc_interacji/ilosc_powtorzen
        else: #gdy wspolczynnik schladzania zostal wybrany
            schladzanie=wspol_schladzania*temperatura

        temperatura = temperatura - schladzanie #obliczenie aktualnej temperatury
        # print(temperatura) #diagnostyka

        #etap 5 ilosc_interacji = 130000 lub break ze wzgledu na niska temp.

    end=time.time() #koniec wykonywania alg.
    czas=round(end-start,2)  #czas dzialania

    ##################
    #   Statystyki   #
    ##################
    print('Koniec dzialania algorytmu\n'
          'Najlepszy cmax to:  {0}'.format(cmax_best))
    print('Ilosc interacji:    {0}\nCzas dzialania alg: {1}s'.format(ilosc_interacji, czas))

    if wspol_schladzania !=0:
        print('Uzyty wspol. schladzania to:',wspol_schladzania,'\n')
#######################################


sym_wyz(len(kolejka_zadan),3e+400,0,1)

# wybor=1 lub 2 (ost. opcja w fun. powyzej) - wybor dzialania alg: 1 - insert, 2 - swap

###################
## testowane temp.:
###################
# temperatura = 3e+400
# temperatura = 3e+300
# temperatura = 3e+1
# temperatura = 3e-100

############################
## testowane wspol. chlodz.:
############################

# wspol_schladzania = 0.99 #wplywa na ilosc iteracji, czym mniejszy tym wiecej iteracji
# wspol_schladzania = 0.95
# wspol_schladzania = 0.9
# wspol_schladzania = 0.8
# wspol_schladzania = 0.4
# wspol_schladzania = 0.01
# wspol_schladzania = 0.01


# do testowania:
# sym_wyz(len(kolejka_zadan),3e+400,0,1)
# sym_wyz(len(kolejka_zadan),3e+300,0,1)
# sym_wyz(len(kolejka_zadan),3e+400,0,2)
# sym_wyz(len(kolejka_zadan),3e+300,0,2)
# print('0000000')
# print('-------')
# sym_wyz(len(kolejka_zadan),3e+400,0.99,1)
# sym_wyz(len(kolejka_zadan),3e+300,0.99,1)
# sym_wyz(len(kolejka_zadan),3e+1,0.99,1)
# sym_wyz(len(kolejka_zadan),(3e-100),0.99,1)
# print('1-------')
# sym_wyz(len(kolejka_zadan),3e+400,0.95,1)
# sym_wyz(len(kolejka_zadan),3e+300,0.95,1)
# sym_wyz(len(kolejka_zadan),3e+1,0.95,1)
# sym_wyz(len(kolejka_zadan),(3e-100),0.95,1)
# print('2-------')
# print('2-------')
# sym_wyz(len(kolejka_zadan),3e+400,0.9,1)
# sym_wyz(len(kolejka_zadan),3e+300,0.9,1)
# sym_wyz(len(kolejka_zadan),3e+1,0.9,1)
# sym_wyz(len(kolejka_zadan),(3e-100),0.9,1)
# print('3-------')
# print('3-------')
# print('3-------')
# sym_wyz(len(kolejka_zadan),3e+400,0.8,1)
# sym_wyz(len(kolejka_zadan),3e+300,0.8,1)
# sym_wyz(len(kolejka_zadan),3e+1,0.8,1)
# sym_wyz(len(kolejka_zadan),(3e-100),0.8,1)
# print('4-------')
# print('4-------')
# print('4-------')
# print('4-------')
# sym_wyz(len(kolejka_zadan),3e+400,0.4,1)
# sym_wyz(len(kolejka_zadan),3e+300,0.4,1)
# sym_wyz(len(kolejka_zadan),3e+1,0.4,1)
# sym_wyz(len(kolejka_zadan),(3e-100),0.4,1)
# print('5-------')
# print('5-------')
# print('5-------')
# print('5-------')
# print('5-------')
# sym_wyz(len(kolejka_zadan),3e+400,0,1)
# sym_wyz(len(kolejka_zadan),3e+300,0,1)
# sym_wyz(len(kolejka_zadan),3e+1,0,1)
# sym_wyz(len(kolejka_zadan),(3e-100),0,1)
#
# print('-------')
# print('-------')
# print('DRUGI WYBOR 2 SWAP!!!!!!!!')
# print('-------')
# print('-------\n\n')
#
# sym_wyz(len(kolejka_zadan),3e+400,0.99,2)
# sym_wyz(len(kolejka_zadan),3e+300,0.99,2)
# sym_wyz(len(kolejka_zadan),3e+1,0.99,2)
# sym_wyz(len(kolejka_zadan),(3e-100),0.99,2)
# print('1-------')
# sym_wyz(len(kolejka_zadan),3e+400,0.95,2)
# sym_wyz(len(kolejka_zadan),3e+300,0.95,2)
# sym_wyz(len(kolejka_zadan),3e+1,0.95,2)
# sym_wyz(len(kolejka_zadan),(3e-100),0.95,2)
# print('2-------')
# print('2-------')
# sym_wyz(len(kolejka_zadan),3e+400,0.9,2)
# sym_wyz(len(kolejka_zadan),3e+300,0.9,2)
# sym_wyz(len(kolejka_zadan),3e+1,0.9,2)
# sym_wyz(len(kolejka_zadan),(3e-100),0.9,2)
# print('3-------')
# print('3-------')
# print('3-------')
# sym_wyz(len(kolejka_zadan),3e+400,0.8,2)
# sym_wyz(len(kolejka_zadan),3e+300,0.8,2)
# sym_wyz(len(kolejka_zadan),3e+1,0.8,2)
# sym_wyz(len(kolejka_zadan),(3e-100),0.8,2)
# print('4-------')
# print('4-------')
# print('4-------')
# print('4-------')
# sym_wyz(len(kolejka_zadan),3e+400,0.4,2)
# sym_wyz(len(kolejka_zadan),3e+300,0.4,2)
# sym_wyz(len(kolejka_zadan),3e+1,0.4,2)
# sym_wyz(len(kolejka_zadan),(3e-100),0.4,2)
# print('5-------')
# print('5-------')
# print('5-------')
# print('5-------')
# print('5-------')
# sym_wyz(len(kolejka_zadan),3e+400,0,2)
# sym_wyz(len(kolejka_zadan),3e+300,0,2)
# sym_wyz(len(kolejka_zadan),3e+1,0,2)
# sym_wyz(len(kolejka_zadan),(3e-100),0,2)

print("\nIlosc zadan to",ilosc_zadan,"a ilosc maszyn to",ilosc_maszyn)
