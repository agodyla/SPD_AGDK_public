class problem_rpq:
    def __init__(self):
        self.jobs = []
        self.r = []
        self.p = []
        self.q = []

    def LoadFile(self, plik):
        plik = open(plik)

        try:
            tekst = plik.read()
        finally:
            plik.close()  # finalnie zamknij plik

        tekst = tekst.split()  # zrob z pojedynczych wyrazow z stringa liste
        ilosc_wykonan = int(tekst[0])

        for x in range(ilosc_wykonan):
            tmp_do_jobs = []
            tmp_do_jobs.append(int(tekst[2 + x * 3]))
            tmp_do_jobs.append(int(tekst[3 + x * 3]))
            tmp_do_jobs.append(int(tekst[4 + x * 3]))
            self.jobs.append(tmp_do_jobs)
        return ilosc_wykonan


def Schrage(jobs):
    l_nn, l_ng, ost_kolejka = problem_rpq(), problem_rpq(), problem_rpq()

    for x in range(len(jobs)):
        l_nn.r.append(jobs[x][0])
        l_nn.p.append(jobs[x][1])
        l_nn.q.append(jobs[x][2])

    cmax, t = 0, min(l_nn.r)
    pamietaj_cmax, t_t = [], []

    while l_nn.r.__len__() != 0 or l_ng.r.__len__() != 0:  # koniec jezeli oba puste
        while l_nn.r.__len__() != 0 and min(l_nn.r) <= t:
            indeks_zadania = l_nn.r.index(min(l_nn.r))
            l_ng.r.append(l_nn.r.pop(indeks_zadania))
            l_ng.p.append(l_nn.p.pop(indeks_zadania))
            l_ng.q.append(l_nn.q.pop(indeks_zadania))

        if l_ng.r.__len__() == 0:
            t = min(l_nn.r)

        else:
            akt_q = max(l_ng.q)
            indeks_zadania = l_ng.q.index(akt_q)

            ost_kolejka.r.append(l_ng.r.pop(indeks_zadania))
            ost_kolejka.p.append(l_ng.p.pop(indeks_zadania))
            ost_kolejka.q.append(l_ng.q.pop(indeks_zadania))

            t = t + ost_kolejka.p[len(ost_kolejka.p) - 1]
            t_t.append(t)
            if cmax < t + ost_kolejka.q[len(ost_kolejka.q) - 1]:
                cmax = t + ost_kolejka.q[len(ost_kolejka.q) - 1]

            pamietaj_cmax.append(cmax)

    do_jobs = []
    for x in range(len(ost_kolejka.r)):
        tmp_do_jobs = []
        tmp_do_jobs.append(ost_kolejka.r[x])
        tmp_do_jobs.append(ost_kolejka.p[x])
        tmp_do_jobs.append(ost_kolejka.q[x])
        do_jobs.append(tmp_do_jobs)

    return cmax, do_jobs


def SchragePmtn(jobs):
    l_nn, l_ng, ost_kolejka = problem_rpq(), problem_rpq(), problem_rpq()

    for x in range(len(jobs)):
        l_nn.r.append(jobs[x][0])
        l_nn.p.append(jobs[x][1])
        l_nn.q.append(jobs[x][2])

    ost_kolejka.r, ost_kolejka.p, ost_kolejka.q = int(1e20), int(1e20), int(1e20)
    cmax = 0
    t = min(l_nn.r)

    # wg pseudokodu, schrage z przerwaniami
    while l_nn.r.__len__() != 0 or l_ng.r.__len__() != 0:  # koniec jezeli oba puste
        while l_nn.r.__len__() != 0 and min(l_nn.r) <= t:  # bo ostatni przypadek rozstrzyga, ze l_nn.r == 0, wiec false
            indeks_zadania = l_nn.r.index(min(l_nn.r))
            l_ng.r.append(l_nn.r.pop(indeks_zadania))
            l_ng.p.append(l_nn.p.pop(indeks_zadania))
            l_ng.q.append(l_nn.q.pop(indeks_zadania))

            if l_ng.q[len(l_ng.q) - 1] > ost_kolejka.q:
                ost_kolejka.p = t - l_ng.r[len(l_ng.q) - 1]
                t = l_ng.r[len(l_ng.q) - 1]

                if ost_kolejka.p > 0:
                    l_ng.r.append(ost_kolejka.r)
                    l_ng.p.append(ost_kolejka.p)
                    l_ng.q.append(ost_kolejka.q)

        if l_ng.r.__len__() == 0:
            t = min(l_nn.r)

        else:
            akt_q = max(l_ng.q)
            indeks_zadania = l_ng.q.index(akt_q)

            ost_kolejka.r = l_ng.r.pop(indeks_zadania)
            ost_kolejka.p = l_ng.p.pop(indeks_zadania)
            ost_kolejka.q = l_ng.q.pop(indeks_zadania)

            t = t + ost_kolejka.p
            if cmax < t + ost_kolejka.q:
                cmax = t + ost_kolejka.q

    # print('\nCmax tutaj (schrage_pmtn) to: {0}'.format(cmax))
    return cmax


# wg strategii Deep Left
def Carlier(poukladane_prace, UB, max_iteracji):
    if max_iteracji < 10 :  # ograniczenie czasowe, gdy algorytm szuka ciagle w dol po lewej stronie i sie "zacina" tam
        max_iteracji += 1
        dane_schrage = Schrage(poukladane_prace)
        U = dane_schrage[0]  # 2. linia
        kolejka_zadan = dane_schrage[1]

        if U < UB:  # 3. linia
            UB = U  # 4. linia

        a, b, c = 0, 0, -1  # zm. pomocnicze do pozniejszego wyznaczania c

        # 6. linia - znajdz b
        akt_czas_zakonczenia, pamietaj_czas_zakonczen = 0, []
        for x in range(len(kolejka_zadan)):

            # oblicz akt_czas_zakonczenia aktualnego zadania biorac pod uwage czas zakonczenia poprzedniego
            # zadania, oraz czas przygotowania obecnego a do tego dodajemy czas p akt. zadania
            # (wczesniej przekazywano te czasy z Schrage)
            akt_czas_zakonczenia = max(akt_czas_zakonczenia, kolejka_zadan[x][0]) + kolejka_zadan[x][1]

            if U == akt_czas_zakonczenia + kolejka_zadan[x][2]:  # cmax == C(j) + q(j)
                b = x  # szukamy maxa, wiec bez breaka

        # 7. linia - znajdz a
        for x in range(len(kolejka_zadan)):  # przenalizuj kazdy przypadek od pocz. do b
            cmax_a = 0
            for y in range(x, b + 1):  # od poczatku do wlacznie z b
                cmax_a += kolejka_zadan[y][1]  # zsumuj cmaxa dla a
            if U == kolejka_zadan[x][0] + kolejka_zadan[b][2] + cmax_a:
                a = x
                break  # szukamy min dlatego jesli sie znajdzie taka wartosc to od razu break

        # 8. linia - znajdz c
        for x in range(a, b + 1):
            if kolejka_zadan[x][2] < kolejka_zadan[b][2]:
                c = x

        # # diagnostyka
        # print('Kolejne znalezione a = {}, b = {}, c = {}'.format(a, b, c))

        if c < 0:  # 9. linia
            return UB  # 10. linia

        # procedura do zmiany r
        pamietaj_stare_r_dla_zad_c = kolejka_zadan[c][0]

        # wyznaczanie r(K) - linia 12., 13. (od c+1)
        nowe_r, nowe_p, nowe_q = 1e20, 0, 1e20

        for K in range(c + 1, b + 1):  # bo od c+1 do b wlacznie!
            nowe_r = min(nowe_r, kolejka_zadan[K][0])
            nowe_p += kolejka_zadan[K][1]
            nowe_q = min(nowe_q, kolejka_zadan[K][2])

        kolejka_zadan[c][0] = max(kolejka_zadan[c][0], nowe_r + nowe_p)  # wybierz max r(c) - linia 14.

        # wyznaczanie r(K+c) - linia 12., 13. (od c) - UWZGLEDNIENIE C
        nowe_r1, nowe_p1, nowe_q1 = 1e20, 0, 1e20
        nowe_r1 = min(nowe_r1, kolejka_zadan[c][0],nowe_r)
        nowe_p1 = kolejka_zadan[c][1] + nowe_p
        nowe_q1 = min(nowe_q1, kolejka_zadan[c][2],nowe_r)

        LB = SchragePmtn(kolejka_zadan)  # linia 15.

        h_K = nowe_r + nowe_p + nowe_q  # bez uwzglednienia zadania c
        h_k_suma_c_ = nowe_r1 + nowe_p1 + nowe_q1   # z uwzglednieniem zadania c
        LB = max(h_K, h_k_suma_c_, LB)  # linia 16.

        if LB < UB:  # linia 17.
            UB = Carlier(kolejka_zadan, UB, max_iteracji)  # linia 18.

        kolejka_zadan[c][0] = pamietaj_stare_r_dla_zad_c  # przywracania poprzedniego r(c) - linia 20.

        # procedura do zmiany q
        pamietaj_stare_q_dla_zad_c = kolejka_zadan[c][2]

        # for K in range(c + 1, b + 1):  # bo od c+1 do b wlacznie!
        #     nowe_r = min(nowe_r, kolejka_zadan[K][0])
        #     nowe_p += kolejka_zadan[K][1]
        #     nowe_q = min(nowe_q, kolejka_zadan[K][2])

        kolejka_zadan[c][2] = max(kolejka_zadan[c][2], nowe_q + nowe_p)  # linia 21.

        # kroki dla lini 22., powtarzamy dla c poniewaz z moglo ulec zmianie poprzez wczesniejsze zamiany
        # nowe_r1, nowe_p1, nowe_q1 = 1e20, 0, 1e20
        # nowe_r1 = min(nowe_r1, kolejka_zadan[c][0],nowe_r)
        # nowe_p1 = kolejka_zadan[c][1] + nowe_p
        # nowe_q1 = min(nowe_q1, kolejka_zadan[c][2],nowe_r)
        nowe_r1, nowe_p1, nowe_q1 = 1e20, 0, 1e20
        for K in range(c, b + 1):  # UWZGLEDNIENIE c
            nowe_r1 = min(nowe_r1, kolejka_zadan[K][0])
            nowe_p1 += kolejka_zadan[K][1]
            nowe_q1 = min(nowe_q1, kolejka_zadan[K][2])

        LB = SchragePmtn(kolejka_zadan)  # linia 22.

        h_k_suma_c_ = nowe_r1 + nowe_p1 + nowe_q1  # z uwzglednieniem zadania c
        LB = max(h_K, h_k_suma_c_, LB)  # linia 23.

        if LB < UB:  # linia 24.
            UB = Carlier(kolejka_zadan, UB , max_iteracji)  # linia 25.

        kolejka_zadan[c][2] = pamietaj_stare_q_dla_zad_c  # przywroc poprzednie q(c) - linia 27.
        return UB

    else:
        return UB



if __name__ == "__main__":
    # pliki = ['in50_1.txt', 'in100.txt', 'in200.txt',  # bez ograniczen (max_iteracji)
    #          'd0.txt', 'd1.txt', 'd3.txt', 'd4.txt']
    # wyniki_pliki = [1492, 3070, 6398, 228, 3026, 3309, 3191]


    pliki = ['in50_1.txt', 'in100.txt', 'in200.txt',
             'd0.txt', 'd1.txt', 'd3.txt', 'd4.txt', 'd5.txt', 'd6.txt', 'd7.txt', 'd8.txt']
    wyniki_pliki = [1492, 3070, 6398, 228, 3026, 3309, 3191, 3618, 3446, 3821, 3634]

    for x in range(len(pliki)):
        pierwotnie = problem_rpq()
        plik = pliki[x]
        ilosc_zadan = pierwotnie.LoadFile(plik)
        print('Przeczytalem plik:', plik)
        Cmax = Carlier(pierwotnie.jobs, 1e20, 0)  # kolejne zadania, czas UB, pocz. ilosc iteracji
        print("Cmax wg Carlier = ", Cmax)

        if Cmax == wyniki_pliki[x]:
            print('Poprawny\n')
        else:
            print('Wyniki sie nie zgadzaja!')
            print(Cmax, 'vs', wyniki_pliki[x],'\n')