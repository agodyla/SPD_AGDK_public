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

    print('Ostateczna kolejka to: {0}\nCmax tutaj to: {1}'.format(ostatecznie,cmax))
    return cmax

start = time.time()
tmp1=schrage_kopc('in50.txt')
cmax_all=tmp1
tmp1=schrage_kopc('in100.txt')
cmax_all+=tmp1
tmp1=schrage_kopc('in200.txt')
cmax_all+=tmp1
print('')
print(cmax_all)

koniec = time.time()
schrage=koniec-start
print("Czas dzialania dla algorytmu Schrage to:", schrage,"s")