from ACO import *

def main():
    aco = ACO()
    alg = aco.runAlgorithm()
    path = alg.getPath()
    cost = alg.getCost()
    print("##########################################################################################")
    print(cost)
    print(path) #+1 la fiecare el din path ca sa se vada concret drumul
main()
