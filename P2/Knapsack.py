import random

def evaluateSolution(solution, prices, weights, maxWeight):
    price = 0
    weight = 0
    for i in range(len(solution)):
        price += prices[i]*solution[i]
        weight += weights[i]*solution[i]

    if weight > maxWeight:
        return 0
    else:
        return price

def applyGeneticOperator(population, k, cProb, mProb):

    #Select parents through a tournament of size k
    selection(k)

    #Cross parents with a probability cProb
    #if random.randint(1,100) <= cProb:
    operator_cross()

    #Mutate parents with a probability mProb
    #if random.randint(1,100) <= mProb:
    operator_mutate()

    return population #Return the new population (not evaluated)

def main():
    weights = [ 34, 45, 14, 76, 32 ]
    prices = [ 340, 210, 87, 533, 112 ]
    maxWeight = 100 #max weight in the knapsack
    nSolutions = 25 #Population size
    maxGenerations = 1 #Number of generations
    k = 3 #Tournament selector size
    cProb = 0.7 #Cross probability
    mProb = 0.1 #Mutation probability

    l=len(weights)
    ##n random valid solutions are created
    population = []
    for i in range(nSolutions):
        objects = list(range(l))
        solution = []
        weight = 0
        while weight < maxWeight:
            object = objects[random.randint(0, len(objects) - 1)]
            weight += weights[object]
            if weight <= maxWeight:
                solution.append(object)
                objects.remove(object)

        s = []
        for i in range(l):
            s.append(0)
        for i in solution:
            s[i] = 1
        population.append([s,evaluateSolution(s,prices,weights,maxWeight)])

    it=1
    while it < maxGenerations:
        nSolutions = applyGeneticOperator(population,k,cProb,mProb)
        #Generational model
        population = []
        for solution in nSolutions:
            population.append([solution[0],evaluateSolution(solution[0],prices,weights,maxWeight)])
        it+=1

if __name__ == "__main__":
    main()
