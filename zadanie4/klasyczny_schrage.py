import time,copy

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

    print('Ostateczna kolejka to: {0}\nCmax tutaj to: {1}'.format(ostatecznie,cmax))
    return cmax


start=time.time()
tmp1=schrage('in50.txt')
cmax_all=tmp1
tmp1=schrage('in100.txt')
cmax_all+=tmp1
tmp1=schrage('in200.txt')
cmax_all+=tmp1
print('')
print(cmax_all)

koniec = time.time()
schrage=koniec-start
print("Czas dzialania dla algorytmu Schrage to:", schrage,"s")

