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
    
    data =[
[0, 42, 12, 465, 139, 524, 743, 513, 537, 126, 617, 551, 705, 689, 852, 443, 408, 390, 929, 195] ,
[42, 0, 144, 782, 186, 711, 525, 130, 61, 128, 609, 361, 419, 284, 206, 57, 302, 725, 684, 215] ,
[12, 144, 0, 336, 76, 917, 755, 498, 276, 549, 587, 579, 989, 107, 69, 671, 49, 718, 302, 150] ,
[465, 782, 336, 0, 553, 299, 360, 514, 269, 717, 911, 175, 643, 32, 329, 491, 427, 379, 414, 218] ,
[139, 186, 76, 553, 0, 21, 579, 296, 219, 304, 788, 628, 933, 150, 600, 503, 752, 686, 84, 373] ,
[524, 711, 917, 299, 21, 0, 731, 857, 895, 114, 133, 166, 611, 229, 146, 473, 51, 39, 632, 24] ,
[743, 525, 755, 360, 579, 731, 0, 466, 353, 128, 55, 75, 58, 164, 994, 167, 776, 224, 705, 591] ,
[513, 130, 498, 514, 296, 857, 466, 0, 712, 679, 439, 345, 632, 590, 620, 891, 765, 11, 458, 719] ,
[537, 61, 276, 269, 219, 895, 353, 712, 0, 220, 863, 40, 690, 910, 577, 326, 69, 963, 110, 547] ,
[126, 128, 549, 717, 304, 114, 128, 679, 220, 0, 156, 234, 210, 484, 586, 49, 838, 327, 439, 730] ,
[617, 609, 587, 911, 788, 133, 55, 439, 863, 156, 0, 408, 369, 125, 671, 786, 979, 856, 340, 334] ,
[551, 361, 579, 175, 628, 166, 75, 345, 40, 234, 408, 0, 144, 35, 222, 837, 148, 499, 87, 510] ,
[705, 419, 989, 643, 933, 611, 58, 632, 690, 210, 369, 144, 0, 821, 240, 703, 417, 417, 985, 720] ,
[689, 284, 107, 32, 150, 229, 164, 590, 910, 484, 125, 35, 821, 0, 189, 450, 55, 407, 535, 554] ,
[852, 206, 69, 329, 600, 146, 994, 620, 577, 586, 671, 222, 240, 189, 0, 573, 942, 263, 348, 619] ,
[443, 57, 671, 491, 503, 473, 167, 891, 326, 49, 786, 837, 703, 450, 573, 0, 609, 74, 137, 289] ,
[408, 302, 49, 427, 752, 51, 776, 765, 69, 838, 979, 148, 417, 55, 942, 609, 0, 852, 789, 524] ,
[390, 725, 718, 379, 686, 39, 224, 11, 963, 327, 856, 499, 417, 407, 263, 74, 852, 0, 896, 570] ,
[929, 684, 302, 414, 84, 632, 705, 458, 110, 439, 340, 87, 985, 535, 348, 137, 789, 896, 0, 369] ,
[195, 215, 150, 218, 373, 24, 591, 719, 547, 730, 334, 510, 720, 554, 619, 289, 524, 570, 369, 0] ]


    
    start = time.time()

    iterations = 0
    # Código a medir
    for i in range(10):
        s=hillClimbing(data)
        iterations += 1
    # -------------

    end = time.time()

    endTime = end - start

    print(endTime)

    try:
        outputCSV = open('output_iterated_local_search.csv', 'a')
        fields = ['N Cities', 'Time', 'Length','Iterations']
        output = csv.DictWriter(outputCSV, fieldnames=fields)
        # output.writeheader() #- Use it only for the first time
        
        #for indice in range(6):
        #    salida.writerow({ 'Campo1':indice+1,
        #                     'Campo2':chr(ord('a') + indice)})
        output.writerow({ 'N Cities':len(s[0]),'Time':endTime,'Length':s[1],'Iterations':iterations})
                           
        output.writerow

    finally:
        outputCSV.close()

    print()
    print("--------------")
    print("Final solution: ",s[0])
    print("Final route length: ",s[1])

if __name__ == "__main__":
    main()
