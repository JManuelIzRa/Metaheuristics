import random
import time
import sys
import csv

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
    
    data = []
    
    start = time.time()

    # Código a medir
    s=hillClimbing(data)
    # -------------

    end = time.time()

    endTime = end - start

    print(endTime)
    
    #line = [str(len(s[0])), str(endTime), str(s[1])]

    #with open('Output.txt', 'a') as f:
        #f.writelines(line)

    #f.close()

    try:
        outputCSV = open('output.csv', 'a')
        fields = ['N Cities', 'Time', 'Length']
        output = csv.DictWriter(outputCSV, fieldnames=fields)
        # output.writeheader() - Use it only for the first time
        
        #for indice in range(6):
        #    salida.writerow({ 'Campo1':indice+1,
        #                     'Campo2':chr(ord('a') + indice)})
        output.writerow({ 'N Cities':len(s[0]),'Time':endTime,'Length':s[1]})
                           
        output.writerow

    finally:
        outputCSV.close()

    print()
    print("--------------")
    print("Final solution: ",s[0])
    print("Final route length: ",s[1])

if __name__ == "__main__":
    main()
