from timeit import timeit
import random


def selectionsort(L) :
    for i in range(len(L)-1) :
        minIndex = i
        for j in range(i+1, len(L)) :
            if L[j] < L[minIndex] :
                minIndex = j
        if minIndex != i :
            L[i], L[minIndex] = L[minIndex], L[i]

def timeOneRun() :
    print("The way to do it if you just want to time one run.")
    N = 1024
    L = [random.randrange(0,100) for x in range(N)]
    t = timeit( lambda : selectionsort(L), number = 1)
    print("time to sort (in seconds):", t)

def timeMultipleRuns(numRuns) :
    print("The way to do it to average multiple runs, repeating setup before each run")
    # Any variables shared between setup and function you're timing
    # declared first.
    N = 1024
    L = []
    def stuffYouNeedButDontWantToTime() :
        # declare variables that are shared as either global or nonlocal
        # depending on whether this is nested inside another function.
        # nonlocal if this is all inside another function, otherwise global.
        nonlocal L
        nonlocal N
        L = [random.randrange(0,100) for x in range(N)]

    def thingToTime() :
        # declare variables that are shared as either global or nonlocal
        # depending on whether this is nested inside another function.
        # nonlocal if this is all inside another function, otherwise global.
        nonlocal L
        nonlocal N
        selectionsort(L)

    t = timeit(thingToTime, setup=stuffYouNeedButDontWantToTime, number=numRuns)
    print("time to sort " + str(numRuns) + " times (in seconds):", t)
    print("average time to sort:{0:.8f}".format(t/numRuns))
    

if __name__ == '__main__' :
    timeOneRun()
    print()
    timeMultipleRuns(1)
    print()
    timeMultipleRuns(10)
    print()
    timeMultipleRuns(100)
    print()

    
    
