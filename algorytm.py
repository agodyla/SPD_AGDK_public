import random as losuj

plik = open('parametry.txt')
try:
    tekst = plik.read()
finally:
    plik.close()  # finalnie zamknij plik

tekst=tekst.split() #zrob z pojedynczych wyrazow z stringa liste

#funkcja do losowania
print("Jesli chcesz losowac to wpisz 1, jesli nie to wpisz cokolwiek innego.")
wybor=input()
if wybor == "1":
    print("Zaczynam losowac")
    '''
    daj_ilosc_maszyn=int(input())
    los_zakres=int(input())
    los_ilosc_zad=int(input())
    '''
    daj_ilosc_maszyn=int(3)
    los_zakres=int(200)
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

''' stare, nie pasuje to obecnego algo
#test nr 2 - losowanie
#maszyna1=losuj.sample(range(10000),300000)
#maszyna2=losuj.sample(range(10000),300000)
#maszyna3=losuj.sample(range(10000),300000)
'''

#test nr 3 - z programu
#maszyna1=[1,9,7,4]
#maszyna2=[3,3,8,8]
#maszyna3=[8,5,6,7]

#test nr 4 - z pdfa
#maszyna1=[5,4,4,3]
#maszyna2=[5,5,4,5]
#maszyna3=[3,2,5,7]

maszyna_wirtualna_nr_1=[]
maszyna_wirtulana_nr_2=[]
kolejka_zadan=[]

#print (maszyna1, maszyna2, maszyna3)

for x in range(ilosc_zadan):
    maszyna_wirtualna_nr_1.append((maszyna1[x]+maszyna2[x]))

if ilosc_maszyn == 3:
    for x in range(ilosc_zadan):
        maszyna_wirtulana_nr_2.append((maszyna2[x]+maszyna3[x]))

#print (maszyna_wirtualna_nr_1,maszyna_wirtulana_nr_2)

for x in range (ilosc_zadan):
    kolejka_zadan.append("wolne miejsce")

znajdz_maks= int(tekst[2])

for x in range (0,len(maszyna_wirtualna_nr_1)):
    if int(maszyna_wirtulana_nr_2[x]) > znajdz_maks:
        znajdz_maks=int(maszyna_wirtulana_nr_2[x])
    if int(maszyna_wirtualna_nr_1[x]) > znajdz_maks:
        znajdz_maks = int(maszyna_wirtualna_nr_1[x])

min_maszyna_wirtualna_nr_1=[znajdz_maks+1,-1] #dl zadania # nr zadania
min_maszyna_wirtulana_nr_2=[znajdz_maks+1,-1]


''' stare else, zostawiam, gdyby cos sie mocno popsulo
pozycjonowanie_zad_najwczesniej=0
pozycjonowanie_zad_najpozniej=ilosc_zadan-1
stare else:
# kolejka_zadan.remove("wolne miejsce")
# print("jestem oesef")
# kolejka_zadan.insert(pozycjonowanie_zad_najpozniej, min_maszyna_wirtulana_nr_2[1])
# pozycjonowanie_zad_najpozniej -= 1
'''

if ilosc_maszyn==2:
    while kolejka_zadan.count("wolne miejsce") != 0:
        min_maszyna_wirtualna_nr_1 = [znajdz_maks+1, -1]  # dl zadania # nr zadania
        for x in range (ilosc_zadan):
            if kolejka_zadan.count(x) != 1:
                if min_maszyna_wirtualna_nr_1[0]>maszyna_wirtualna_nr_1[x]:
                        min_maszyna_wirtualna_nr_1[0] = maszyna_wirtualna_nr_1[x]
                        min_maszyna_wirtualna_nr_1[1]=x #chodzi o nr zadania, nie wartosc!
        for miejsce in range(ilosc_zadan):
            if kolejka_zadan[miejsce] == "wolne miejsce":
                kolejka_zadan.remove("wolne miejsce")
                kolejka_zadan.insert(miejsce, min_maszyna_wirtualna_nr_1[1])
                break
        #print(kolejka_zadan)
print("\n")

if ilosc_maszyn==3:
    while kolejka_zadan.count("wolne miejsce") != 0:
        min_maszyna_wirtualna_nr_1 = [znajdz_maks+1, -1]  # dl zadania # nr zadania
        min_maszyna_wirtulana_nr_2 = [znajdz_maks+1, -1]
        for x in range (ilosc_zadan):
            if kolejka_zadan.count(x) != 1:
                if min_maszyna_wirtualna_nr_1[0]>maszyna_wirtualna_nr_1[x]:
                        min_maszyna_wirtualna_nr_1[0] = maszyna_wirtualna_nr_1[x]
                        min_maszyna_wirtualna_nr_1[1]=x #chodzi o nr zadania, nie wartosc!

                if min_maszyna_wirtulana_nr_2[0]>maszyna_wirtulana_nr_2[x]:
                    if kolejka_zadan.count(x) != 1:
                        min_maszyna_wirtulana_nr_2[0] = maszyna_wirtulana_nr_2[x]
                        min_maszyna_wirtulana_nr_2[1] = x

        # jesli czas zadania na maszynie wirtualnej nr 1 jest mniejszy to
        # skasuj jedna z sztucznie uwtorzonych zadan, aby zaplenic tablice
        # i dodaj zadanie wlasciwe na dobre miejsce
        # w tym przypadku zadanie dodaj na pierwszym wolnym miejscu na
        # poczatku listy zadan
        if min_maszyna_wirtualna_nr_1[0]<min_maszyna_wirtulana_nr_2[0]:
            for miejsce in range(ilosc_zadan - 1):
                if kolejka_zadan[miejsce] == "wolne miejsce":
                    kolejka_zadan.remove("wolne miejsce")
                    kolejka_zadan.insert(miejsce, min_maszyna_wirtualna_nr_1[1])
                    break
        else:
            for miejsce in range(ilosc_zadan):
                if kolejka_zadan[(ilosc_zadan-1-miejsce)] == "wolne miejsce":
                    kolejka_zadan.remove("wolne miejsce")
                    kolejka_zadan.insert(ilosc_zadan-1-miejsce, min_maszyna_wirtualna_nr_1[1])
                    break
        print("Postep sortowania: ", kolejka_zadan)

print("\n")

def wyswietl_kolejke_zadan():
    for x in range (len(kolejka_zadan)):        # kolejka_zadan od 0 do n-1
        kolejka_zadan[x]=1+kolejka_zadan[x]     # teraz kolejka od 1 do n

    print("Aktualna kolejka zadan to ", kolejka_zadan)


    for x in range (len(kolejka_zadan)): # przywroc kolejke od 0 do n-1, gdzie n to ilosc zadan
        kolejka_zadan[x]=-1+kolejka_zadan[x]


def policz_czas():
    czas = maszyna1[kolejka_zadan[0]] + maszyna2[kolejka_zadan[0]]
    for x in range (ilosc_zadan):
        czas+=maszyna3[x]
        if x+1<ilosc_zadan:
            test= abs(maszyna1[kolejka_zadan[x+1]]-maszyna2[kolejka_zadan[x]]-maszyna3[kolejka_zadan[x]]+maszyna2[kolejka_zadan[x+1]])
    wyswietl_kolejke_zadan()
    print("Ogolny czas wykonywania zadan to przynajmniej:", czas,"h")
    print("\n")

def policz_czas_1don():
    kolejka_zadan.sort()
    czas = maszyna1[kolejka_zadan[0]] + maszyna2[kolejka_zadan[0]]
    for x in range (ilosc_zadan):
        czas+=maszyna3[x]
        if x+1<ilosc_zadan:
            test= abs(maszyna1[kolejka_zadan[x+1]]-maszyna2[kolejka_zadan[x]]-maszyna3[kolejka_zadan[x]]+maszyna2[kolejka_zadan[x+1]])
    wyswietl_kolejke_zadan()
    print("Czas wykonywania zadan wg alg 1..n to przynajmniej", czas," h")

policz_czas()
policz_czas_1don()