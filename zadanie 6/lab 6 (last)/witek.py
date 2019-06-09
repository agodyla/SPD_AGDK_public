from pathlib import Path
from ortools.linear_solver import pywraplp


#  http://mariusz.makuchowski.staff.iiar.pwr.wroc.pl/download/courses/sterowanie.procesami.dyskretnymi/lab.instrukcje/lab02.witi/witi.literatura/SPD_WiTi.pdf
#  http://mariusz.makuchowski.staff.iiar.pwr.wroc.pl/download/courses/sterowanie.procesami.dyskretnymi/lab.instrukcje/lab02.witi/witi.data.txt

class Milp_WiTi():  # odpowiedni opis pod WiTi
    def __init__(self, czas, waga, max_czas):
        self.c = czas
        self.w = waga
        self.m = max_czas


def Milp(jobs, instnaceName):
    cmax_po_p, variablesMaxValue = 0, 0  # inicjacja zmiennych do fora

    for a in range(len(jobs)):  # zsumowanie calego czasu, jako ustalenie czasu koncowego wykonania wszystkich zadan
        cmax_po_p += jobs[a].c

    for b in range(len(jobs)):
        calkowita_kara = jobs[b].w * cmax_po_p             # wyliczenie kary gdyby dotyczyla calego czasu wszystkich zadan
        odejmij_dopuszczalny_czas = jobs[b].w * jobs[b].m  # odjecie czasu, ktory jest dopuszczalny do wykonywania zadan
        variablesMaxValue = max(variablesMaxValue,calkowita_kara - odejmij_dopuszczalny_czas) + cmax_po_p  # maksymalna wartosc

    solver = pywraplp.Solver('simple_mip_program',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # zmienne:
    alfasMatrix = {}
    for i in range(len(jobs)):
        for j in range(len(jobs)):
            alfasMatrix[i, j] = solver.IntVar(0, 1, "alfa" + str(i) + "_" + str(j)) # do warunku lub

    start, koniec, delays = [], [], []
    for i in range(len(jobs)): # aby zapamiaetac konrketne poczatki i konce zadan
        start.append(solver.IntVar(0, variablesMaxValue, "start" + str(i)))
        koniec.append(solver.IntVar(0, variablesMaxValue, "koniec" + str(i)))
        delays.append(solver.IntVar(0, variablesMaxValue, "delays" + str(i)))

    najmniejsza_kara = solver.IntVar(0, variablesMaxValue, "najmniejsza kara")


    # ogranicznia!
    # aktualna_kara = 0
    for i in range(len(jobs)):


        # solver.Add(koniec[i] >= jobs[i].m)  # zadania koniec musi nastapic w chwili niemniejszej niz koniec czasu dopuszczalnego
        solver.Add(koniec[i] == start[i] + jobs[i].c)  # koniec nie moze byc mniejszy od czasu startu aktualnego zadania i jego skonczenia
        # kara_all = jobs[i].w * koniec[i]
        # odejmij_dopuszczalny_czas = jobs[i].w * jobs[i].m
        #solver.Add(najmniejsza_kara >= kara_all - odejmij_dopuszczalny_czas + aktualna_kara)
        #aktualna_kara += jobs[i].w * (koniec[i] - jobs[i].m)  # pamietaj aktualna wartosc kary do kolejnych porownan!
        solver.Add(delays[i]>=0) # opoznienie wieksze lub = 0
        solver.Add(delays[i]>=(koniec[i] - jobs[i].m)* jobs[i].w) # opoznienie wiekszer rowne niz
        # (warunek z preznetacji WiTi od dr Makuchowskiego)


    for i in range(len(jobs)):
        for j in range(i + 1, len(jobs)):
            solver.Add(start[i] + jobs[i].c <= start[j] + alfasMatrix[i, j] * variablesMaxValue)
            solver.Add(start[j] + jobs[j].c <= start[i] + alfasMatrix[j, i] * variablesMaxValue)
            solver.Add(alfasMatrix[i, j] + alfasMatrix[j, i] == 1)

    solver.Minimize(sum(delays))
    status = solver.Solve()

    if (status is not pywraplp.Solver.OPTIMAL):
        print("Nie optymalna wartosc!")
    print(instnaceName, "\nUdalo sie. Wyliczona najmniejsza kara to:", solver.Objective().Value())

    pi = []
    for i in range(len(start)):
        pi.append((i + 1, start[i].solution_value(),koniec[i].solution_value()))
    pi.sort(key=lambda x: x[1])
    print('Kolejka zadan:', pi)
    print('\n')


def GetWiTisFromFile(pathToFile):
    fullTextFromFile = Path(pathToFile).read_text()
    words = fullTextFromFile.replace("\n", " ").split(" ")
    words_cleaned = list(filter(None, words))
    numbers = list(map(int, words_cleaned))

    numbersOfJobs = numbers[0]
    numbers.pop(0)
    numbers.pop(0)

    jobs = []
    for i in range(numbersOfJobs):
        jobs.append(Milp_WiTi(numbers[0], numbers[1], numbers[2]))
        numbers.pop(0)
        numbers.pop(0)
        numbers.pop(0)

    return jobs


if __name__ == '__main__':
    file_paths = ["witi13.txt"]  # data.13

    for i in range(len(file_paths)):
        jobs = GetWiTisFromFile(file_paths[i])
        Milp(jobs, file_paths[i])

    file_paths = ["witi14.txt"]  # data.14

    for i in range(len(file_paths)):
        jobs = GetWiTisFromFile(file_paths[i])
        Milp(jobs, file_paths[i])

    file_paths = ["witi15.txt"]  # data.15

    for i in range(len(file_paths)):
        jobs = GetWiTisFromFile(file_paths[i])
        Milp(jobs, file_paths[i])

    file_paths = ["witi16.txt"]  # data.16

    for i in range(len(file_paths)):
        jobs = GetWiTisFromFile(file_paths[i])
        Milp(jobs, file_paths[i])

    file_paths = ["witi17.txt"]  # data.17

    for i in range(len(file_paths)):
        jobs = GetWiTisFromFile(file_paths[i])
        Milp(jobs, file_paths[i])

    file_paths = ["witi18.txt"]  # data.18

    for i in range(len(file_paths)):
        jobs = GetWiTisFromFile(file_paths[i])
        Milp(jobs, file_paths[i])

    file_paths = ["witi19.txt"]  # data.19

    for i in range(len(file_paths)):
        jobs = GetWiTisFromFile(file_paths[i])
        Milp(jobs, file_paths[i])

    file_paths = ["witi20.txt"]  # data.20

    for i in range(len(file_paths)):
        jobs = GetWiTisFromFile(file_paths[i])
        Milp(jobs, file_paths[i])