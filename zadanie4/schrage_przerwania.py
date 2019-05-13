import copy

def schrage(plik):

    class problem_rpq:
        def __init__(self):
            self.r=[]
            self.p=[]
            self.q=[]


    class problem_rpq_ost:
        r=int(1e20)
        p=int(1e20)
        q=int(1e20)


    l_nn=problem_rpq()
    l_ng=problem_rpq()
    ost_kolejka=problem_rpq_ost()


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


    akt_r=1e20 #poczatkowo, aby miec odwoloanie do petli
    akt_q=-1 #poczatkowo ekstremalnie male
    nr_zadania=0
    cmax=0
    indeks_zadania=-1

    t=min(l_nn.r)
    ostatecznie=[]
    l=0

    #wg pseudokodu, schrage z przerwaniami
    while l_nn.r.__len__() != 0 or l_ng.r.__len__() != 0: #koniec jezeli oba puste
        while l_nn.r.__len__() != 0 and min(l_nn.r) <= t: #bo ostatni przypadek rozstrzyga, ze l_nn.r == 0, wiec false
            indeks_zadania=l_nn.r.index(min(l_nn.r))
            l_ng.r.append(l_nn.r.pop(indeks_zadania))
            l_ng.p.append(l_nn.p.pop(indeks_zadania))
            l_ng.q.append(l_nn.q.pop(indeks_zadania))

            if l_ng.q[len(l_ng.q)-1] > ost_kolejka.q:
                ost_kolejka.p= t - l_ng.r[len(l_ng.q)-1]
                t = l_ng.r[len(l_ng.q)-1]

                if ost_kolejka.p >0:
                    l_ng.r.append(ost_kolejka.r)
                    l_ng.p.append(ost_kolejka.p)
                    l_ng.q.append(ost_kolejka.q)

        if l_ng.r.__len__() == 0:
            t=min(l_nn.r)

        else:
            akt_q = max(l_ng.q)
            indeks_zadania = l_ng.q.index(akt_q)

            ost_kolejka.r=l_ng.r.pop(indeks_zadania)
            ost_kolejka.p=l_ng.p.pop(indeks_zadania)
            ost_kolejka.q=l_ng.q.pop(indeks_zadania)

            t = t + ost_kolejka.p
            if cmax < t + ost_kolejka.q:
                cmax= t+ost_kolejka.q

    print('\nCmax tutaj to: {0}'.format(cmax))
    return cmax

tmp1=schrage('in50.txt')
cmax_all=tmp1
tmp1=schrage('in100.txt')
cmax_all+=tmp1
tmp1=schrage('in200.txt')
cmax_all+=tmp1
print('\n\n')
print(cmax_all)