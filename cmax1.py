"""
Losowanie listy zadan + wszystkie permutacje
"""

import random
import itertools
import time

start = time.time()
najmniejszy_czas = 100000
nr_permutacji = 0
n = 4 # ilosc zadan
m = 2 # ilosc maszyn
m += 1
p_number = 0
taskarray = [[0 for x in range(m)] for y in range(n)]
helparray = [[0 for x in range(m)] for y in range(n)]

for i in range(len(helparray)):
    for j in range(len(helparray[i])):
        if j == 0:
            helparray[i][j] = i+1
        else:
            helparray[i][j] = random.randint(1, 10)

print("Poczatkowa lista zadan wygenerowana losowo: ")

for i in range(len(helparray)):
    for j in range(len(helparray[i])):
        print(helparray[i][j], end=' ')
    print()

myints = [i+1 for i in range(0, n)]

for i in list(itertools.permutations(myints)):
    p_number += 1
    print("Permutacja ", p_number)

    for x in range(0, n):
        for y in range(0, m):
            taskarray[i[x]-1][y] = helparray[x][y]

    for k in range(len(helparray)):
        for l in range(len(taskarray[k])):
            print(taskarray[k][l], end=' ')
        print()

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
    print()
    print("Maszyna 1 konczy po: ", machine1)
    print("Maszyna 2 konczy po: ", machine2)
    if m == 4:
        print("Maszyna 3 konczy po: ", machine3)
        if machine3 < najmniejszy_czas:
            nr_permutacji = p_number
            najmniejszy_czas = machine3
    elif m == 3:
        if machine2 < najmniejszy_czas:
            nr_permutacji = p_number
            najmniejszy_czas = machine2

end = time.time()

print("Koniec programu")
print("Najmniejszy czas: ", najmniejszy_czas)
print("Nr permutacji: ", nr_permutacji)
print("Czas wykonywania programu: ", end-start, "s")
