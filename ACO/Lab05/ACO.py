from Ant import *
from utils import permutation

class ACO:
    def __init__(self):
        pass

    def __initAnts(self):
        #n = m si de aia pot face asta
        #m numarul de furnicute
        n = params["noAnts"]
        perm = permutation(n)
        ants = []
        for p in perm:
            ants.append(Ant(p))
        return ants

    def __getBestAnt(self,ants):
        minCost = ants[0].getCost()
        bestAnt = ants[0]
        for ant in ants:
            if ant.getCost() < minCost:
                minCost = ant.getCost()
                bestAnt = ant
        return bestAnt

    def __updatePheromone(self, ant):
        path = ant.getPath()
        n = params["noEdges"] - 1
        phi = params["phi"]
        for i in range(n):
            ph = randint(1,1000) * 1.0 / 1000
            params["pheromone"][path[i]][path[i+1]] = (1 - phi) * params["pheromone"][path[i]][path[i+1]] + phi * ph
 
    def runAlgorithm(self):
        noIter = params["noIter"]
        phi = params["phi"]
        n = params["noAnts"]
        bestAnt = None
        bestAnts = []
        for _ in range(noIter):
            ants = self.__initAnts()
            for _ in range(n):
                for ant in ants:
                    ant.addNextCity()
            bestAnt = self.__getBestAnt(ants)
            bestAnts.append(bestAnt)
            self.__updatePheromone(ant)
            print(bestAnt.getPath())
            print(bestAnt.getCost())
        return self.__getBestAnt(bestAnts)

