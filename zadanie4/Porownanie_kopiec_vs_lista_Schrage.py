import copy, time, heapq

def schrage_kopc(plik):
    nn=[]
    ng=[]
    heapq.heapify(ng)
    heapq.heapify(nn)

    plik = open(plik)
    try:
        tekst = plik.read()
    finally:
        plik.close()  # finalnie zamknij plik

    tekst = tekst.split()  # zrob z pojedynczych wyrazow z stringa liste

    ilosc_wykonan = int((len(tekst) - 2) / 3)

    for x in range(ilosc_wykonan):
        tuple=(int(tekst[(2 + x * 3)]),int(tekst[(3 + x * 3)]),int(tekst[(4 + x * 3)]),x)
        do_kopca=(tuple[0], tuple)
        heapq.heappush(nn,do_kopca)


    # #tylko dla celu pokazania co umieszono w kopcu
    # tuple = (int(tekst[(2 + 5 * 3)]), int(tekst[(3 + 5 * 3)]), int(tekst[(4 + 5 * 3)]), 5)
    # do_kopca = (tuple[0], tuple)
    # print('\nPrzykladowy element w kopcu to:', do_kopca)
    # # tylko dla celu pokazania co umieszono w kopcu

    heapq.heapify(nn)
    heapq._heapify_max(ng)

    cmax=0
    t=heapq.nsmallest(1, nn)[0][0]
    ostatecznie=[]


    while heapq.nsmallest(1,nn) != [] or heapq.nlargest(1,ng) != []: #koniec jezeli oba puste

        while heapq.nsmallest(1,nn) != [] and heapq.nsmallest(1,nn)[0][0] <= t: #bo ostatni przypadek rozstrzyga, ze l_nn.r == 0, wiec false
            do_kopca=heapq.heappop(nn) #wybierz war. minimalna
            do_kopca=(do_kopca[1][2],do_kopca[1]) # np. 30, (30, 45, 1855, 11)
            heapq.heappush(ng,do_kopca)

        if heapq.nlargest(1,ng)== []:
            t=heapq.nsmallest(1,nn)[0][0]

        else:
            heapq._heapify_max(ng)
            akt_q = heapq._heappop_max(ng)
            ostatecznie.append(akt_q[1][3]+1)
            t = t + akt_q[1][1]
            if cmax < t + akt_q[0]:
                cmax= t+akt_q[0]

    return cmax


def schrage(plik):

    class problem_rpq:
        def __init__(self):
            self.r = []
            self.p = []
            self.q = []

    l_nn=problem_rpq()
    l_ng=problem_rpq()
    ost_kolejka=problem_rpq()
    porownanie=problem_rpq()

    plik = open(plik)
    try:
        tekst = plik.read()
    finally:
        plik.close()  # finalnie zamknij plik

    tekst=tekst.split() #zrob z pojedynczych wyrazow z stringa liste

    # ilosc_zadan = int(tekst[0])
    ilosc_wykonan=int((len(tekst)-2)/3)

    for x in range (ilosc_wykonan):
        l_nn.r.append(int(tekst[2+x*3]))
        l_nn.p.append(int(tekst[3+x*3]))
        l_nn.q.append(int(tekst[4+x*3]))

    porownanie.r=copy.deepcopy(l_nn.r)
    porownanie.p=copy.deepcopy(l_nn.p)
    porownanie.q=copy.deepcopy(l_nn.q)


    akt_r=1e20 #poczatkowo, aby miec odwoloanie do petli
    akt_q=-1
    # nr_zadania=0
    cmax=0
    # indeks_zadania=-1

    t=min(l_nn.r)
    ostatecznie=[]

    def min_lnn(): #wyszukaj min w liscie lnn
        min_lnn_war=10000000000000
        for x in range (len(l_nn.r)):
            if l_nn.r[x] < min_lnn_war:
                min_lnn_war=l_nn.r[x]
        return min_lnn_war

    def max_lng(): #wyszukaj max w liscie lng
        max_lng_war=0
        for x in range (len(l_ng.q)):
            if l_ng.q[x] > max_lng_war:
                max_lng_war=l_ng.q[x]
        return max_lng_war


    while l_nn.r.__len__() != 0 or l_ng.r.__len__() != 0: #koniec jezeli oba puste
        while l_nn.r.__len__() != 0 and min_lnn() <= t: #bo ostatni przypadek rozstrzyga, ze l_nn.r == 0, wiec false
            indeks_zadania=l_nn.r.index(min_lnn())
            l_ng.r.append(l_nn.r.pop(indeks_zadania))
            l_ng.p.append(l_nn.p.pop(indeks_zadania))
            l_ng.q.append(l_nn.q.pop(indeks_zadania))

        if l_ng.r.__len__() == 0:
            t=min_lnn()

        else:
            akt_q = max_lng()
            indeks_zadania = l_ng.q.index(akt_q)

            ost_kolejka.r.append(l_ng.r.pop(indeks_zadania))
            ost_kolejka.p.append(l_ng.p.pop(indeks_zadania))
            ost_kolejka.q.append(l_ng.q.pop(indeks_zadania))

            t = t + ost_kolejka.p[len(ost_kolejka.p)-1]

            if cmax < t + ost_kolejka.q[len(ost_kolejka.q)-1]:
                cmax= t+ost_kolejka.q[len(ost_kolejka.q)-1]

    for x in range (len(ost_kolejka.r)):
        tmp1=ost_kolejka.r[x]
        tmp2=porownanie.r.index(tmp1)
        ostatecznie.append(tmp2+1)
    return cmax

print('wyniki na kopcu, dzialanie na gotowej biblotece!') #!dzialanie na gotowej biblotece!
start1 = time.time()
# tmp1=schrage_kopc('in50.txt')
tmp1=schrage_kopc('in2000.txt')
cmax_all=tmp1
print(tmp1)
# tmp1=schrage_kopc('in100.txt')
tmp1=schrage_kopc('in2000.txt')
cmax_all+=tmp1
print(tmp1)
# tmp1=schrage_kopc('in200.txt')
tmp1=schrage_kopc('in2000.txt')
cmax_all+=tmp1
print(tmp1)
print('')
print('Suma cmax:',cmax_all)
print('')
koniec1 = time.time()
kopiec_Czas=koniec1-start1

print('wyniki na liscie')
start=time.time()
# tmp1=schrage('in50.txt')
tmp1=schrage('in2000.txt')
cmax_all=tmp1
print(tmp1)
# tmp1=schrage('in100.txt')
tmp1=schrage('in2000.txt')
cmax_all+=tmp1
print(tmp1)
# tmp1=schrage('in200.txt')
tmp1=schrage('in2000.txt')
cmax_all+=tmp1
print(tmp1)
print('')
print('Suma cmax:',cmax_all)
print('')

koniec = time.time()
schrage=koniec-start
print("Czas dzialania dla alg Schrage listy (na 4.0) to:", schrage,"s")
print("Czas dzialania dla alg Schrage kopiec (na 5.0) to:", kopiec_Czas,"s")
print('Zdecydowana korzysc czasu dla list chociaż nie powinno miec to miejsca :(')