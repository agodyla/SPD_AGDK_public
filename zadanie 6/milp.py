from ortools.linear_solver import pywraplp
from pathlib import Path

class RPQ(): #stworzenie klasy dla problemy RPQ
    def __init__(self, r, p, q):
        self.R = r
        self.P = p
        self.Q = q

def Milp(jobs, instanceName): #solver typu MILP, istota jest odpowiednie zapisanie ogarniczen

    variablesMaxValue = 0
    for a in range(len(jobs)): #oblicz war. maksymalna
        variablesMaxValue += jobs[a].R + jobs[a].P + jobs[a].Q

    solver = pywraplp.Solver('simple_mip_program', #solver
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # zmienne a wtym alfy, ktore sa potrzebne, aby odpowiednio przedstawic problem solverowi
    # tj. solver nie moze wiec warunku lub, wiec jest on "sztucznie" realizowany przez alfy
    alfasMatrix = {} #macierz!
    for i in range(len(jobs)):
        for j in range(len(jobs)):
            alfasMatrix[i, j] = solver.IntVar(0, 1, "alfa" + str(i) + "_" + str(j) )
    starts = [] #czasy ropoczynania poszczegolnych zadan
    for i in range(len(jobs)):
        starts.append(solver.IntVar(0, variablesMaxValue, "starts" + str(i)))
    cmax = solver.IntVar(0, variablesMaxValue, "cmax")

    # ograniczenia
    # kazde z zadan musi byc odpowiednio przygotowane
    for i in range(len(jobs)):
        solver.Add(starts[i] >= jobs[i].R) #czas startu nie moze byc > niz czas przygotowania danego zadania
        solver.Add(cmax >= starts[i] + jobs[i].P + jobs[i].Q) #cmax musi byc < niz wszystkie czasy zakonczen (z Q)

    #okreslenie ograniczen kolejnosci wykonywania zadan
    for i in range(len(jobs)):
        for j in range(i + 1, len(jobs)):
            solver.Add(starts[i] + jobs[i].P <= starts[j] + alfasMatrix[i, j] * variablesMaxValue)
            solver.Add(starts[j] + jobs[j].P <= starts[i] + alfasMatrix[j, i] * variablesMaxValue)
            solver.Add(alfasMatrix[i, j] + alfasMatrix[j, i] == 1) #spelnienie warunku lub, poniewaz alfa
                                                                   # moze byc = 1 lub 0 i ich suma musi byc rowna 0

    # solver:
    solver.Minimize(cmax)
    status = solver.Solve()
    if (status is not pywraplp.Solver.OPTIMAL):
        print("Nie optymalna wartosc!")
    print(instanceName, "Udalo sie. Wyliczony Cmax to:", solver.Objective().Value())
    pi = []
    for i in range(len(starts)): #wyswietl kolejke zadan i ich kolejne war. czasow zakonczen zadan
        pi.append((i, starts[i].solution_value()))
    pi.sort(key=lambda x: x[1]) #sortuj wg wartosci 2. wartosci w tuplu,
                                # gdzie w poj. tuplu (nr_zadania,aktualny cmax)
    print(pi)

#odczytaj poszczegolne wartosci RPQ z pliku i umiesc w liscie jobs
def GetRPQsFromFile(pathToFile):
    fullTextFromFile = Path(pathToFile).read_text()
    words = fullTextFromFile.replace("\n", " ").split(" ")
    words_cleaned = list(filter(None, words))
    numbers = list(map(int, words_cleaned))

    numberOfJobs = numbers[0]
    numbers.pop(0)
    numbers.pop(0)

    jobs = []
    for i in range(numberOfJobs):
        jobs.append(RPQ(numbers[0], numbers[1], numbers[2]))
        numbers.pop(0)
        numbers.pop(0)
        numbers.pop(0)
    return jobs

if __name__ == '__main__':
    file_paths = ["d0.txt"]

    for i in range(len(file_paths)):
        jobs = GetRPQsFromFile(file_paths[i])
        Milp(jobs, file_paths[i])