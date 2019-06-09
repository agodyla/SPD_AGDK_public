from __future__ import print_function
import collections
from ortools.sat.python import cp_model

def MinimalJobshopSat(tmp3):
    """Minimal jobshop problem."""
    model = cp_model.CpModel()

    jobs_data = tmp3
        # ???= [  # task = (machine_id, processing_time).
        # [(0, 3), (1, 2), (2, 2)],  # Job0
        # [(0, 2), (2, 1), (1, 4)],  # Job1
        # [(1, 4), (2, 3)]  # Job2
        # ]

    machines_count = 1 + max(task[0] for job in jobs_data for task in job)
    all_machines = range(machines_count)

    # Sumowanie czasu wykonywania
    horizon = sum(task[1] for job in jobs_data for task in job)

    # namedtuple do przechowywania informacji o utworzonych zmiennych (start_var - poczatek zadania, end_var - koniec zadania)
    task_type = collections.namedtuple('task_type', 'start end interval')

    assigned_task_type = collections.namedtuple('assigned_task_type',
                                                'start job index duration')

    # Tworzenie interwału
    all_tasks = {}
    machine_to_intervals = collections.defaultdict(list)


    for job_id, job in enumerate(jobs_data):
        for task_id, task in enumerate(job):
            machine = task[0]
            duration = task[1]
            suffix = '_%i_%i' % (job_id, task_id)
            # Górnym ograniczeniem start_var i end_var jest wyliczone wyzej horizon, czyli suma czasu wykonywania wszystkich zadan na wszystkich maszynach
            start_var = model.NewIntVar(0, horizon, 'start' + suffix)
            end_var = model.NewIntVar(0, horizon, 'end' + suffix)
            # Tworzenie interval variable, której wartość jest zmiennym przedziałem czasu
            interval_var = model.NewIntervalVar(start_var, duration, end_var,
                                                'interval' + suffix)
            all_tasks[job_id, task_id] = task_type(
                start=start_var, end=end_var, interval=interval_var)
            machine_to_intervals[machine].append(interval_var)

    # Wymuszenia - constraints

    # Tworzenie wymuszeń bez nakładania się (no overlap constraint)
    for machine in all_machines:
        model.AddNoOverlap(machine_to_intervals[machine])

    # Wymuszenie pierwszeństwa, aby kolejne zadania dla tej samej maszyny się nie nakładały
    for job_id, job in enumerate(jobs_data):
        for task_id in range(len(job) - 1):
            model.Add(all_tasks[job_id, task_id +
                                1].start >= all_tasks[job_id, task_id].end)

    # Ustawienie celu dla solvera - minimalizacja czasu wykonywania (cmax)
    obj_var = model.NewIntVar(0, horizon, 'makespan')
    model.AddMaxEquality(obj_var, [
        all_tasks[job_id, len(job) - 1].end
        for job_id, job in enumerate(jobs_data)
    ])
    model.Minimize(obj_var)

    # Deklaracja modelu solvera
    solver = cp_model.CpSolver()

    solver.parameters.max_time_in_seconds = 120.0
    status = solver.Solve(model)
    # solver.UserTime(2)

    if status == cp_model.OPTIMAL:
        # Tworzenie listy zadań przeznaczonych dla każdej z maszyn
        assigned_jobs = collections.defaultdict(list)
        for job_id, job in enumerate(jobs_data):
            for task_id, task in enumerate(job):
                machine = task[0]
                assigned_jobs[machine].append(
                    assigned_task_type(
                        start=solver.Value(all_tasks[job_id, task_id].start),
                        job=job_id,
                        index=task_id,
                        duration=task[1]))

        # Output dla każdej z maszyn
        output = ''
        for machine in all_machines:
            # Sortowanie po czasie rozpoczęcia
            assigned_jobs[machine].sort()
            sol_line_tasks = 'Machine ' + str(machine) + ': '
            sol_line = '           '

            for assigned_task in assigned_jobs[machine]:
                name = 'job_%i_%i' % (assigned_task.job, assigned_task.index)
                # Formatowanie outputu programu
                sol_line_tasks += '%-10s' % name

                start = assigned_task.start
                duration = assigned_task.duration
                sol_tmp = '[%i,%i]' % (start, start + duration)
                # Formatowanie outputu programu
                sol_line += '%-10s' % sol_tmp

            sol_line += '\n'
            sol_line_tasks += '\n'
            output += sol_line_tasks
            output += sol_line

        # Wyswietlenie wyniku dzialania
        print('Optymalny czas wykonywania: %i' % solver.ObjectiveValue())
        print(output)
    else:
        print('Potrzebuje wiecej czasu na obliczenia, aktulanie obliczylem:\nOptimal Schedule Length: %i' % solver.ObjectiveValue())






def czytaj(plik):
    plik = open(plik)
    try:
        tekst = plik.read()
    finally:
        plik.close()  # finalnie zamknij plik

    tekst = tekst.split()  # zrob z pojedynczych wyrazow z stringa liste

    ilosc_zadan = int(tekst[0])
    ilosc_w_lini=int(tekst[1])
    # ilosc_wykonan = int((len(tekst) - 2) / 3)

    jobs_data=[]
    tmp2=[]
    tmp=[]
    tmp3=[]

    for x in range (ilosc_zadan+1):
        tmp3.append(tmp2)
        tmp2=[]
        for y in range (0,ilosc_w_lini*2,2):
            tmp = []
            a=x*ilosc_w_lini*2+1*x
            if 4+y+a+1 <= len(tekst) :
                tmp.append(int(tekst[4+y+a]))
                tmp.append(int(tekst[4+y+1+a]))
                tmp2.append(tmp)

    tmp3.pop(0)
    MinimalJobshopSat(tmp3)

#czytaj('insa1.txt')    ## oryginalne d1 1411
#czytaj('insa100.txt')  ## d23 1828
#czytaj('insa2.txt')  ## d24 1951
#czytaj('insa3.txt')  ## d27 1965
#czytaj('insa4.txt')  ## d30 1890
#czytaj('tescik.txt') ## d
#czytaj('benchmark_orb10.txt')
czytaj('insa80.txt')
