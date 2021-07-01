from utils import params
from random import randint

class Ant:
    def __init__(self,city):
        self.__path = [city]

    def getPath(self):
        return self.__path[0:-1] #omite -1 sau 0 (se mai adauga asta deoarece in functiile mele de decizie am dat sa se returneze -1/0, la ultimul oras adaugat se mai incearca inca un oras, dar fiindca nu s-a gasit se returneaza -1 sau 0, depinde pe ce ramura intra) 

    def getCost(self):
        s = 0
        n = params["noEdges"]
        mat = params["mat"]
        path = self.__path[0:-1]
        for i in range(n-1):
            s += mat[path[i]][path[i+1]]
        s+=mat[path[0]][path[n-1]]
        return s

    def __argMax(self,i):
        n = params["noEdges"]
        mat = params["mat"]
        pheromone = params["pheromone"]
        alpha = params["alpha"]
        betha = params["betha"]
        bestCity = -1
        bestProd = -1
        for j in range(n):
            if i != j and j not in self.__path:
                tauij = pow(pheromone[i][j], alpha)
                etaij = pow(1.0/mat[i][j], betha)
                if tauij * etaij > bestProd:
                    bestProd = tauij * etaij
                    bestCity = j
        return bestCity
 
    def __sume(self,i):
        s = 0.0
        n = params["noEdges"]
        pheromone = params["pheromone"]
        alpha = params["alpha"]
        betha = params["betha"]
        mat = params["mat"]
        for j in range(n):
            if i != j and j not in self.__path:
                tauij = pow(pheromone[i][j], alpha)
                etaij = pow(1.0/mat[i][j], betha)
                s += tauij*etaij
        return s

    def __probability(self,i,j):
        alpha = params["alpha"]
        betha = params["betha"]
        pheromone = params["pheromone"]
        mat = params["mat"]
        tauij = pow(pheromone[i][j], alpha)
        etaij = pow(1.0/mat[i][j], betha)
        prod = tauij * etaij
        return prod / self.__sume(i)

    def __selectCity(self,i):
        n = params["noEdges"]
        bestj = 0
        bestProb = -1
        for j in range(n):
            if i != j  and j not in self.__path:
                if self.__probability(i,j) > bestProb:
                    bestProb = self.__probability(i,j)
                    bestj = j
        return bestj

    def __selectNextCity(self,i):
        q = randint(1,10000) * 1.0 / 10000
        j = -1
        if q <= params["q0"]:
            j = self.__argMax(i)
        else:
            j = self.__selectCity(i) #J
        return j
    
    def addNextCity(self):
        i = self.__path[-1]
        j = self.__selectNextCity(i)
        phi = params["phi"]
        ph = randint(1,1000) * 1.0 / 1000 #cantitatea de feromon eliberat de aceasta furnica la un moment dat
        params["pheromone"][i][j] = (1 - phi) * params["pheromone"][i][j] + phi * ph
        self.__path.append(j)



