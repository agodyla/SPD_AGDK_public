from __future__ import print_function
from ortools.sat.python import cp_model

class RPQ():
    def __init__(self, r, p, q):
        self.R = r
        self.P = p
        self.Q = q

def CP(jobs, instanceName): #modyfikacja na bazie: https://developers.google.com/optimization/mip/integer_opt_cp

    model_cp = cp_model.CpModel() #model cp z bibloteki ortools.sat.python

    variablesMaxValue = 0
    for a in range(len(jobs)):
        variablesMaxValue += jobs[a].R + jobs[a].P + jobs[a].Q

    #zmienne
    alfasMatrix = {}
    for i in range(len(jobs)):
        for j in range(len(jobs)):
            alfasMatrix[i, j] = model_cp.NewIntVar(0, 1, "alfa" + str(i) + "_" + str(j) )
            #zamiast IntVar dodajemy NewIntVar dla problemu cp
    starts = []
    for i in range(len(jobs)):
        starts.append(model_cp.NewIntVar(0, variablesMaxValue, "starts" + str(i)))
    cmax = model_cp.NewIntVar(0, variablesMaxValue, "cmax")

    # ograniczenia:
    for i in range(len(jobs)):
        model_cp.Add(starts[i] >= jobs[i].R)
        model_cp.Add(cmax >= starts[i] + jobs[i].P + jobs[i].Q)

    for i in range(len(jobs)):
        for j in range(i + 1, len(jobs)):
            model_cp.Add(starts[i] + jobs[i].P <= starts[j] + alfasMatrix[i, j] * variablesMaxValue)
            model_cp.Add(starts[j] + jobs[j].P <= starts[i] + alfasMatrix[j, i] * variablesMaxValue)
            model_cp.Add(alfasMatrix[i, j] + alfasMatrix[j, i] == 1)


    # solver.SetTimeLimit(100000) #10sek
    # solver:
    model_cp.Minimize(cmax)
    solver = cp_model.CpSolver() #wywlanie solvera!
    status = solver.Solve(model_cp)
    if (status is not cp_model.OPTIMAL):
        print("Nie optymalna wartosc!")
    print(instanceName, "Cmax:", solver.ObjectiveValue())
    pi = []
    for i in range(len(starts)):
        pi.append((i, solver.Value(starts[i])))
    pi.sort(key=lambda x: x[1])
    print(pi)


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
    file_paths = ["d0.txt"] #d0.txt - przyklad z 4 zadaniami RPQ

    for i in range(len(file_paths)):
        jobs = GetRPQsFromFile(file_paths[i])
        CP(jobs, file_paths[i])