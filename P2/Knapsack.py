import random
import numpy as np
from scipy import stats

def TournamentSelection(population, k):

    #Seleccion de los padres de una población mediante torneos de k participantes.
    
        parents=[]
        
    #Generamos tantos hijos como padres hay actualmente en la población,
        for i in range(len(population)):
            
            #selecionamos aleatoriamente k  padres para el torneo,
            candidatos=random.sample(population,k)
            
            #Ordenamos los candidatos por valor de fitness ascendente,
            candidatos.sort(key=lambda candidatos:candidatos[1])
            
            #Escogemos el mejor candidato del torneo,
            parents.append(candidatos[k-1])
            
        return parents    

def cruceOnePoint(padre1,padre2):
   
 
    cruce=[]
    #Generamos aleatoriamente el punto a partir del cual se realiza el cruce de dos padres,
    x=random.randint(0,len(padre1)-2)
    #Realizamos el cruce valores de ambos padres desde la posicion x de cada  hasta el final,
    cruce.append(padre1[0:x+1]+padre2[x+1:len(padre2)])
    cruce.append(padre2[0:x+1]+padre1[x+1:len(padre1)])
    return cruce

def cruzarPadres(padres,cProb):
   
    i=0
    cruzados=[]
    while i<len(padres):
        if i+1 < len(padres): #Comprobamos que si el número de soluciones es impar, que el ultimo cromosoma no se cruzará con ninguno otro 
            if random.randint(1,100) <= (cProb*100):
                cruce=cruceOnePoint(padres[i][0],padres[i+1][0])
                
                cruzados.append([cruce[0],0])
                cruzados.append([cruce[1],0])
                
            else:
                cruzados.append(padres[i])
                cruzados.append(padres[i+1])  
            
        else: #Al ser impar el número de soluciones, se guarda el último cromosoma tal cual
            cruzados.append(padres[i])
            
        i=i+2  
            
        
    return cruzados

def mutacionMultiplesGenes(hijo):
    
    #Genereamos un número aletorio de genes a mutar 
    n_genes=random.randint(1,len(hijo))
       
    for i in range(n_genes):
        
        gen_n=random.randint(0,len(hijo)-1) #Se genera la posición aletoria del cromosoma la cual se muta
        hijo[gen_n]=(hijo[gen_n]+1)%2  
        
    return hijo
    
def mutation(hijos,mProb):
    mutados=[]
    
    for nHijo in hijos:
        
        if random.randint(1,100)<=(mProb*100): #Comprobamos si se llega a mutar ese cromosoma ó no
            mutados.append([mutacionMultiplesGenes(nHijo[0]),0]) #Realizamos una mutación multiple para codificación binaria      
        else:
             mutados.append(nHijo)
                
    return mutados 


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
    parents = TournamentSelection(population, k)

    #Cross parents with a probability cProb
    #if random.randint(1,100) <= cProb:
    #if random.uniform(0, 1) <=cProb:
        
    children = cruzarPadres(parents,cProb)


    #Mutate parents with a probability mProb
    #if random.randint(1,100) <= mProb:
    #if random.uniform(0, 1) <=mProb:
        
    children_mutate =  mutation(children, mProb)
    
    population.clear()
    population=children_mutate

    return population #Return the new population (not evaluated)

def geneticAlgorithm(nSolutions,mProb):

    weights = [ 34, 45, 14, 76, 32 ]
    prices = [ 340, 210, 87, 533, 112 ]
    maxWeight = 100 #max weight in the knapsack
    nSolutions = 10 #Population size
    maxGenerations = 10 #Number of generations
    k = 3 #Tournament selector size
    cProb = 0.7 #Cross probability
    #mProb = 0.1 #Mutation probability

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

    it=0
    while it < maxGenerations:

        nSolutions = applyGeneticOperator(population,k,cProb,mProb)

        #Generational model
        population = []
        for solution in nSolutions:
            population.append([solution[0],evaluateSolution(solution[0],prices,weights,maxWeight)])
        it+=1

    accuracy = 0
    max_value = 0
    counter = 0

    for i in range(len(population)):
        
        if population[i][1] > max_value:
            max_value = population[i][1]
            counter = 1

        elif population[i][1] == max_value:
            counter = counter + 1

    accuracy = counter/len(population)

    #print(population)
    #print("Accuracy: ", accuracy)

    return population,accuracy

if __name__ == "__main__":
    
    weights = [ 34, 45, 14, 76, 32 ]
    prices = [ 340, 210, 87, 533, 112 ]
    maxWeight = 100 #max weight in the knapsack
    nSolutions = 10 #Population size
    maxGenerations = 10 #Number of generations
    k = 3 #Tournament selector size
    
    cProb = 0.7 #Cross probability

    ###############################
    # Accuracy when mProb changes #
    ###############################
    
    mProb = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #Mutation probability

    accuracy_mProb = []

    for prob in mProb:
        
        population,a = geneticAlgorithm(nSolutions = 10,mProb = prob)

        accuracy_mProb.append(a)

    print("Accuracy mProb: ",accuracy_mProb)
    
    valores_mochila = []

    for i in range (len(population)):
        
        # Eliminamos los valores de mochila = 0 al considerarlos como no validos y porque añadirian mucha varianza al resultado.
        if population[i][1] > 0:
            valores_mochila.append(population[i][1])
            
    

    print("Valores mochila: ", valores_mochila)

    correlacion_mProb, p_value = stats.pearsonr(mProb, accuracy_mProb)

    print("Correlación con mProb: ",correlacion_mProb) # Correlación negativa. Tienen una tendencia opuesta.

    mean, var, std = stats.mvsdist(valores_mochila)

    print("Media valor de la mochila: ", mean.mean())
    print("Varianza valor de la mochila: ", mean.var())
    print("Desviacion tipìca valor de la mochila: ", mean.std())

    ####################################
    # Accuracy when nSolutions changes #
    ####################################

    nSolutions = [10,20,30,40,50,60,70,80,90,100]

    accuracy_nSolutions = []

    for solution in nSolutions:

        population,a = geneticAlgorithm(nSolutions = solution,mProb = 0.1)

        accuracy_nSolutions.append(a)

    print("Accuracy nSolutions: ",accuracy_nSolutions)