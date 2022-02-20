import random
import time
import sys

def evaluateSolution(data, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += data[solution[i - 1]][solution[i]]
    return routeLength

def getBestNeighbor(solution, data):
    ##Get the neighbors
    neighbors = []
    l=len(solution)
    for i in range(l):
        for j in range(i+1, l):
            n = solution.copy()
            n[i] = solution[j]
            n[j] = solution[i]
            neighbors.append(n)

    ##Get the best neighbor
    bestNeighbor = neighbors[0]
    bestLength = evaluateSolution(data, bestNeighbor)
    for neighbor in neighbors:
        routeLength = evaluateSolution(data, neighbor)
        if routeLength < bestLength:
            bestLength = routeLength
            bestNeighbor = neighbor
    return bestNeighbor, bestLength

def hillClimbing(data):
    l=len(data)
    ##Create a random solution
    cities = list(range(l))
    solution = []
    for i in range(l):
        city = cities[random.randint(0, len(cities) - 1)]
        solution.append(city)
        cities.remove(city)
    routeLength = evaluateSolution(data, solution)

    ## print("Route length: ", routeLength) quitado que no afecte la E/S
    ##Get the best neighbor till no better neighbors can be obtained
    neighbor = getBestNeighbor(solution, data)
    while neighbor[1] < routeLength:
        solution = neighbor[0]
        routeLength = neighbor[1]
        ##print("Route length: ", routeLength)
        neighbor = getBestNeighbor(solution, data)

    return solution, routeLength

def main():
    data = [
[0, 1000, 913, 311, 495, 864, 851, 758, 869, 656] ,
[1000, 0, 788, 616, 986, 243, 791, 336, 800, 73] ,
[913, 788, 0, 410, 143, 461, 674, 634, 35, 988] ,
[311, 616, 410, 0, 965, 966, 136, 225, 884, 210] ,
[495, 986, 143, 965, 0, 368, 197, 599, 309, 17] ,
[864, 243, 461, 966, 368, 0, 116, 673, 222, 154] ,
[851, 791, 674, 136, 197, 116, 0, 742, 303, 101] ,
[758, 336, 634, 225, 599, 673, 742, 0, 326, 953] ,
[869, 800, 35, 884, 309, 222, 303, 326, 0, 369] ,
[656, 73, 988, 210, 17, 154, 101, 953, 369, 0] ]
    start = time.time()

    # Código a medir
    s=hillClimbing(data)
    # -------------

    end = time.time()
    print(end-start)
    
    print("--------------")
    print("Final solution: ",s[0])
    print("Final route length: ",s[1])

if __name__ == "__main__":
    main()
