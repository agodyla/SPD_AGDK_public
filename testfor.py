import random as losuj
import time, itertools, math


plik = open('parametry.txt')
try:
    tekst = plik.read()
finally:
    plik.close()  # finalnie zamknij plik

tekst=tekst.split() #zrob z pojedynczych wyrazow z stringa liste

#funkcja do losowania
print("Jesli chcesz losowac to wpisz 1, jesli nie to wpisz cokolwiek innego.")
wybor="9" #input()
if wybor == "1":
    print("Zaczynam losowac")

    '''print("Wpisz zadana ilosc maszyn (oecnie 2 lub 3):")
    daj_ilosc_maszyn=int(input())
    print("Wpisz zadany zakres czasowy pojedynczego zadania:")
    los_zakres=int(input())
    print("Wpisz ilosc zadan do wylosowania:")
    los_ilosc_zad=int(input())
    '''
    daj_ilosc_maszyn=int(2)
    los_zakres=int(10)
    los_ilosc_zad=int(10)

    tekst[0]=int(los_ilosc_zad)
    tekst[1]=int(daj_ilosc_maszyn)
    ilosc_osobnych_prac=los_ilosc_zad*daj_ilosc_maszyn

    for x in range(2,ilosc_osobnych_prac+2):
        try:
            tekst[x]=int(losuj.uniform(1,los_zakres)) #losuj.sample(range(los_zakres))
        except:
            tekst.append(int(losuj.uniform(1, los_zakres) ) )

    print("Skonczylem losowac.\n")
else:
    print("Zrezygnowano z losowania. Wczytuje pliki z txt")

start = time.time()

ilosc_zadan = int(tekst[0])
ilosc_maszyn = int(tekst[1])

maszyna1 = []
maszyna2 = []

if ilosc_maszyn == 3:
    maszyna3 = []

if ilosc_maszyn==2:
    for x in range(2, len(tekst), 2):
        maszyna1.append(int(tekst[x]))  # dodaj do maszyny nr 1 pierwsza wartosc
                                                # i zmien typ z str na int
        maszyna2.append(int(tekst[x + 1]))

if ilosc_maszyn==3:
    for x in range(2, len(tekst),3):
        maszyna1.append(int(tekst[x]))  # dodaj do maszyny nr 1 pierwsza wartosc i
                                            # zmien typ z str na int
        maszyna2.append(int(tekst[x + 1]))
        maszyna3.append(int(tekst[x + 2]))

'''
# sprawdzenie
print(ilosc_maszyn)
print(maszyna1)
print(maszyna2)
print(maszyna3)
print(tekst)
'''

#test nr 1
#maszyna1 = [1, 13, 13]
#maszyna2 = [4,5,6]
#maszyna3 = [7,8,9]

#test nr 3 - z programu
#maszyna1=[1,9,7,4]
#maszyna2=[3,3,8,8]
#maszyna3=[8,5,6,7]

#test nr 4 - z pdfa
#maszyna1=[5,4,4,3]
#maszyna2=[5,5,4,5]
#maszyna3=[3,2,5,7]

'''  4   3
  5   5   3
  4   5   2
  4   4   5
  3   5   7'''

'''  4   3
  1   3   8
  9   3   5
  7   8   6
  4   8   7
'''

maszyna_wirtualna_nr_1=[]
maszyna_wirtulana_nr_2=[]
kolejka_zadan=[]

#print (maszyna1, maszyna2, maszyna3)

for x in range(ilosc_zadan):
    maszyna_wirtualna_nr_1.append((maszyna1[x]+maszyna2[x]))

if ilosc_maszyn == 3:
    for x in range(ilosc_zadan):
        maszyna_wirtulana_nr_2.append((maszyna2[x]+maszyna3[x]))


for x in range (ilosc_zadan):
    kolejka_zadan.append("wolne miejsce")

znajdz_maks= int(tekst[2])

for x in range (0,len(maszyna_wirtualna_nr_1)):
    if int(maszyna_wirtualna_nr_1[x]) > znajdz_maks:
        znajdz_maks = int(maszyna_wirtualna_nr_1[x])
    if ilosc_maszyn==3:
        if int(maszyna_wirtulana_nr_2[x]) > znajdz_maks:
            znajdz_maks = int(maszyna_wirtulana_nr_2[x])

min_maszyna_wirtualna_nr_1=[znajdz_maks+1,-1] #dl zadania # nr zadania
min_maszyna_wirtulana_nr_2=[znajdz_maks+1,-1]

#print(maszyna_wirtualna_nr_1,maszyna_wirtulana_nr_2)

mw1=maszyna_wirtualna_nr_1
if ilosc_maszyn==3:
    mw2=maszyna_wirtulana_nr_2

tmp1=0
tmp2=ilosc_zadan-1

if ilosc_maszyn==2:
    mw1=maszyna1
    mw2=maszyna2
    while kolejka_zadan.count("wolne miejsce") != 0:
        min_mw1 = [znajdz_maks+1, -1]  # dl zadania # nr zadania
        min_mw2 = [znajdz_maks+1, -1]
        for x in range (ilosc_zadan):
            if kolejka_zadan.count(x) != 1:
                if min_mw1[0]>mw1[x]:
                        min_mw1[0] = mw1[x]
                        min_mw1[1]=x #chodzi o nr zadania, nie wartosc!
                        #print(min,mw1[x])

                if min_mw2[0]>mw2[x]:
                    if kolejka_zadan.count(x) != 1:
                        min_mw2[0] = mw2[x]
                        min_mw2[1] = x

        # jesli czas zadania na maszynie wirtualnej nr 1 jest mniejszy to
        # skasuj jedna z sztucznie uwtorzonych zadan, aby zaplenic tablice
        # i dodaj zadanie wlasciwe na dobre miejsce
        # w tym przypadku zadanie dodaj na pierwszym wolnym miejscu na
        # poczatku listy zadan
        if min_mw1[0]<min_mw2[0]:
            kolejka_zadan.remove("wolne miejsce")
            kolejka_zadan.insert(tmp1,min_mw1[1])
            tmp1+=1

        else:
            kolejka_zadan.remove("wolne miejsce")
            kolejka_zadan.insert(tmp2, min_mw2[1])
            tmp2-=1


        print(kolejka_zadan)
print("\n")



if ilosc_maszyn==3:
    while kolejka_zadan.count("wolne miejsce") != 0:
        min_mw1 = [znajdz_maks+1, -1]  # dl zadania # nr zadania
        min_mw2 = [znajdz_maks+1, -1]
        for x in range (ilosc_zadan):
            if kolejka_zadan.count(x) != 1:
                if min_mw1[0]>mw1[x]:
                        min_mw1[0] = mw1[x]
                        min_mw1[1]=x #chodzi o nr zadania, nie wartosc!
                        #print(min,mw1[x])

                if min_mw2[0]>mw2[x]:
                    if kolejka_zadan.count(x) != 1:
                        min_mw2[0] = mw2[x]
                        min_mw2[1] = x

        # jesli czas zadania na maszynie wirtualnej nr 1 jest mniejszy to
        # skasuj jedna z sztucznie uwtorzonych zadan, aby zaplenic tablice
        # i dodaj zadanie wlasciwe na dobre miejsce
        # w tym przypadku zadanie dodaj na pierwszym wolnym miejscu na
        # poczatku listy zadan
        if min_mw1[0]<min_mw2[0]:
            kolejka_zadan.remove("wolne miejsce")
            kolejka_zadan.insert(tmp1,min_mw1[1])
            tmp1+=1

        else:
            kolejka_zadan.remove("wolne miejsce")
            kolejka_zadan.insert(tmp2, min_mw2[1])
            tmp2-=1


        print(kolejka_zadan)
print("\n")



def wyswietl_kolejke_zadan():
    for x in range (len(kolejka_zadan)):        # kolejka_zadan od 0 do n-1
        kolejka_zadan[x]=1+kolejka_zadan[x]     # teraz kolejka od 1 do n

    print("Kolejka wg algorytmu Johnsona: ", kolejka_zadan)


    for x in range (len(kolejka_zadan)): # przywroc kolejke od 0 do n-1, gdzie n to ilosc zadan
        kolejka_zadan[x]=-1+kolejka_zadan[x]

wyswietl_kolejke_zadan()


m=ilosc_maszyn+1
n=ilosc_zadan
taskarray = [[0 for x in range(m)] for y in range(n)]
helparray = [[0 for x in range(m)] for y in range(n)]
cmaxarray = [[0 for x in range(m+1)] for y in range(n+1)]

for i in range(len(helparray)):
    for j in range(len(helparray[i])):
        if j == 0:
            helparray[i][j] = (kolejka_zadan[i]+1)
        else:
            tmp=kolejka_zadan[i]
            helparray[i][j] = int(tekst[1+j+tmp*ilosc_maszyn])

#print(helparray)

#for x in range(0, n):
#    for y in range(0, m):
#        taskarray[x-1][y] = helparray[x][y]

taskarray=helparray
najmniejszy_czas1=znajdz_maks+1
p_number = 0

'''for k in range(len(helparray)):
    for l in range(len(taskarray[k])):
        print(taskarray[k][l], end=' ')
    print()'''

machine1, machine2, machine3 = 0, 0, 0

for x in range(0, n):
    machine1 += taskarray[x][1]
    if x == 0:
        machine2 = taskarray[x][1] + taskarray[x][2]
        if m == 4:
            machine3 = machine2 + taskarray[x][3]
    else:
        if machine1 <= machine2:
            machine2 += taskarray[x][2]
        else:
            machine2 = machine1 + taskarray[x][2]
        if m == 4:
            if machine2 <= machine3:
                machine3 += taskarray[x][3]
            else:
                machine3 = machine2 + taskarray[x][3]
#print()
#print("Maszyna 1 konczy po: ", machine1)
#print("Maszyna 2 konczy po: ", machine2)

if m == 4:
    print("Maszyna 3 konczy po: ", machine3)
    if machine3 < najmniejszy_czas1:
          nr_permutacji = p_number
          najmniejszy_czas1 = machine3
    najmniejszy_czas_john = machine3
else:
    if machine2 < najmniejszy_czas1:
          nr_permutacji = p_number
          najmniejszy_czas1 = machine2
    najmniejszy_czas_john = machine2

end = time.time()
print("Czas dzialania dla algorytmu Johansona to: ", end-start,"s\n")

##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################

start1 = time.time()
if wybor=='1':
    najmniejszy_czas = (los_zakres*ilosc_zadan)+1000
else:
    najmniejszy_czas = (znajdz_maks * ilosc_zadan) + 1000


p_number = 0
taskarray = [[0 for x in range(m)] for y in range(n)]
helparray = [[0 for x in range(m)] for y in range(n)]
tmparr = [[0 for x in range(m-1)] for y in range(n)]
pokaz_najlepsza_kolejke = [[0 for x in range(m)] for y in range(n)]

for i in range(len(helparray)):
    for j in range(len(helparray[i])):
        if j == 0:
            helparray[i][j] = i+1
        else:
            helparray[i][j] = int(tekst[1+i*ilosc_maszyn+j])
#print("lista",tekst)
#print("macierz pmocy",helparray)
#print("Poczatkowa lista zadan wygenerowana losowo: ")

'''for i in range(len(helparray)):
    for j in range(len(helparray[i])):
        print(helparray[i][j], end=' ')
    print()'''

myints = [i+1 for i in range(0, n)]

#print("maszyny",maszyna1,maszyna2,maszyna3)

for i in list(itertools.permutations(myints)):
    p_number += 1
    #print("Permutacja ", p_number)

    for x in range(0, n):
        for y in range(0, m):
            taskarray[i[x]-1][y] = helparray[x][y]

    for x in range(0, n):
        for y in range(0, m-1):
            tmparr[x][y] = taskarray[x][y+1]

    '''for k in range(len(helparray)):
        for l in range(len(taskarray[k])):
            print(taskarray[k][l], end=' ')
        print()'''

    machine1, machine2, machine3 = 0, 0, 0

    for x in range(0, n):
        machine1 += taskarray[x][1]
        if x == 0:
            machine2 = taskarray[x][1] + taskarray[x][2]
            if m == 4:
                machine3 = machine2 + taskarray[x][3]
        else:
            if machine1 <= machine2:
                machine2 += taskarray[x][2]
            else:
                machine2 = machine1 + taskarray[x][2]
            if m == 4:
                if machine2 <= machine3:
                    machine3 += taskarray[x][3]
                else:
                    machine3 = machine2 + taskarray[x][3]

    for x in range(0, n+1):
        for y in range(0, m+1):
            cmaxarray[x][y] = 0

    for x in range(1, n+1):
        for y in range(1, m):
            cmaxarray[x][y] = max(cmaxarray[x-1][y], cmaxarray[x][y-1]) + tmparr[x-1][y-1]

    print("Zadania: ")
    for k in range(len(tmparr)):
        for l in range(len(tmparr[k])):
            print(tmparr[k][l], end=' ')
        print()

    print("cmax array")
    for k in range(len(cmaxarray)):
        for l in range(len(cmaxarray[k])):
            print(cmaxarray[k][l], end=' ')
        print()
    print(max(map(max, cmaxarray)))
    #print()
    #print("Maszyna 1 konczy po: ", machine1)
    print("Maszyna 2 konczy po: ", machine2)
    if m == 4:
        #####
        #print("Maszyna 3 konczy po: ", machine3)
        if machine3 < najmniejszy_czas:
            nr_permutacji = p_number
            najmniejszy_czas = machine3
            pokaz_najlepsza_kolejke=taskarray
            pokaz_kolejke = []
            for x in range(0, ilosc_zadan):
                pokaz_kolejke.append(pokaz_najlepsza_kolejke[x][0])
            #print(taskarray)
    elif m == 3:
        if machine2 < najmniejszy_czas:
            nr_permutacji = p_number
            najmniejszy_czas = machine2
            pokaz_najlepsza_kolejke=taskarray
            pokaz_kolejke = []
            for x in range(0, ilosc_zadan):
                pokaz_kolejke.append(pokaz_najlepsza_kolejke[x][0])
            #print(taskarray)


end1 = time.time()

print("\nKoniec programu. Wyniki dla algorytmu naiwnego (brute force).")
print("Najmniejszy czas w wykonywania zadan po kolei to: ", najmniejszy_czas)
print("Nr permutacji: ", nr_permutacji)
print("Ogolna ilosc permutacji to: ", math.factorial(ilosc_zadan))
print("Czas wykonywania programu dla alg naiwnego: ", end1-start1, "s")

print("\nJakość porownywania dla alg. Johnsona: ",najmniejszy_czas_john)
print("Jakość porownywania dla brute force: ",najmniejszy_czas)

print("\nCzas wykonywania dla alg. Johnsona: ",end-start)
print("Czas wykonywania brute force: ",end1-start1)
