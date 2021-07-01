from random import randint

def initData(filename):
    f = open(filename,"r")
    n = int(f.readline().strip())
    mat = []
    pheromone = []
    for _ in range(n):
        attr = f.readline().strip().split(",")
        attr = [int(val) for val in attr]
        ph = [0.1 for _ in range(n)]
        pheromone.append(ph)
        mat.append(attr)
    params = {}
    params["noEdges"] = n
    params["mat"] = mat
    params["q0"] = 0.5
    params["alpha"] = 0.8 #pt feromon
    params["betha"] = 0.2 #pt distanta
    #etaij = 1/dij --> visibiliatea (dij distanta dintre i,j)
    #tauij = pheromon de pe muchia i,j
    params["pheromone"] = pheromone
    params["phi"] = randint(1,1000) * 1.0 / 1000 #coeficientu de degradare a feromonului
    params["noIter"] = 1000
    #numarul furnicutelor va fi n (dimensiunea grafului)
    params["noAnts"] = n
    return params

params = initData("C:\\Users\\alexandru.sabou\\university\\An3\\Sem2\\AI\\Lab05\\Lab05\\data\\input.txt")

def permutation(n):
    perm = []
    for _ in range(n):
        r = randint(0,n-1)
        while (r in perm):
            r = randint(0,n-1)
        perm.append(r)
    return perm

