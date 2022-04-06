import random
from statistics import pvariance
from turtle import clear
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def calculateStatistics(population,variable_array, accuracy_array):
    
    valores_mochila = []

    for i in range (len(population)):
        
        # Eliminamos los valores de mochila = 0 al considerarlos como no validos y porque añadirian mucha varianza al resultado.
        if population[i][1] > 0:
            valores_mochila.append(population[i][1])
            
    correlation, p_value = stats.pearsonr(variable_array, accuracy_array)

    #mean = np.average(valores_mochila)
    #var = np.var(valores_mochila)
    #std = np.std(valores_mochila)

    return valores_mochila, correlation, mean, var, std, p_value
    

def Average(lst):
    return sum(lst) / len(lst)

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

def geneticAlgorithm(nSolutions,maxGenerations,mProb,cProb,k,elitism):

    maxWeight = 6404180
    weights = [382745,799601,909247,729069,467902, 44328, 34610,698150,823460,903959,853665,551830,610856,670702,488960,951111,323046,446298,931161, 31385,496951,264724,224916,169684]
    prices = [825594,1677009,1676628,1523970, 943972,  97426,  69666,1296457,1679693,1902996,1844992,1049289,1252836,1319836, 953277,2067538, 675367, 853655,1826027,  65731, 901489, 577243, 466257, 369261]
    
    #k = 3 #Tournament selector size
    #cProb = 0.7 #Cross probability
    #mProb = 0.1 #Mutation probability

    l=len(weights)
    ##n random valid solutions are created
    population = []
    for i in range(nSolutions):
        objects = list(range(l))
        solution = []
        weight = 0
        
        #while weight < maxWeight:
        it = 0
        while it < 6:
            object = objects[random.randint(0, len(objects) - 1)]
            weight += weights[object]
            #if weight <= maxWeight:
            solution.append(object)
            objects.remove(object)

            it += 1

        s = []
        for i in range(l):
            s.append(0)
        for i in solution:
            s[i] = 1
        population.append([s,evaluateSolution(s,prices,weights,maxWeight)])

    #Guradamos la solucion de elite de la generacion inicial en caso de utilizarse elitismo
    if elitism:
        population.sort(reverse=True,key=lambda poblacion:poblacion[1])
        eliteSolucion=population[0]

    it=0
    while it < maxGenerations:

        nSolutions = applyGeneticOperator(population,k,cProb,mProb)

        #Generational model
        population = []
        for solution in nSolutions:
            population.append([solution[0],evaluateSolution(solution[0],prices,weights,maxWeight)])
        it+=1

        #Comprobamos si se utiliza elitismo
        if elitism:
            #Ordenamos la poblacion de forma descendente con respecto a su valor de fitness
            population.sort(reverse=True,key=lambda population:population[1])
                #Comprobamos si la solucion elite de la generación anterior es mejor que
                #la peor solucion de la  nueva generacion, y la conservamos en caso de ser asi 
            if population[len(population)-1][1] < eliteSolucion[1]:
                population.pop()
                population.append(eliteSolucion)
            #Guardamos la solucion elite de la nueva generación
            population.sort(reverse=True,key=lambda population:population[1])  
            eliteSolucion=population[0]

    accuracy = 0
    max_value = 0
    counter = 0
    knapsack_values = []

    for i in range(len(population)):
        
        if population[i][1] > max_value:
            max_value = population[i][1]
            counter = 1

        elif population[i][1] == max_value:
            counter = counter + 1

        if population[i][1] > 0:
            knapsack_values.append(population[i][1])

    accuracy = counter/len(population)

    mean = np.average(knapsack_values)
    var = np.var(knapsack_values)
    std = np.std(knapsack_values)

    #print(population)
    #print("Accuracy: ", accuracy)

    return population,accuracy,mean,var,std

if __name__ == "__main__":
    
    maxWeight = 100 #max weight in the knapsack

    ###############################
    # Accuracy when mProb changes #
    ###############################
    
    mProb = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #Mutation probability

    accuracy_mProb = []
    mean_mProb = []
    var_mProb = []
    std_mProb = []

    accuracy_iterations = []
    mean_iterations = []
    var_iterations = []
    std_iterations = []

    for prob in mProb:
        for i in range(0,100):
            
            population,a,mean,var,std = geneticAlgorithm(nSolutions = 10, maxGenerations = 10, mProb = prob,cProb=0.7,k=3,elitism=False)

            accuracy_iterations.append(a)
            mean_iterations.append(mean)
            var_iterations.append(var)
            std_iterations.append(std)

        accuracy_mProb.append(Average(accuracy_iterations))

        mean_mProb.append(Average(mean_iterations))
        var_mProb.append(Average(var_iterations))
        std_mProb.append(Average(std_iterations))

    print("mProb: ", mProb)
    print("Accuracy mProb: ",accuracy_mProb)
    
    valores_mochila, correlation, mean, var, std,p_value = calculateStatistics(population,mProb,accuracy_mProb)

    print("Valores mochila: ", valores_mochila)

    print("Correlación con mProb: ",correlation) # Correlación negativa. Tienen una tendencia opuesta.
    print("con una certeza de ",1-p_value)
    print("Media valor de la mochila: ", mean_mProb)
    print("Varianza valor de la mochila: ", var_mProb)
    print("Desviacion tipìca valor de la mochila: ",std_mProb)
    print()
    
    plt.plot(mProb, accuracy_mProb)
    
    plt.xlabel('Probability of mutation')
    plt.ylabel('Accuracy')
    
    plt.savefig('accuracy_mProb.png')

    ####################################
    # Accuracy when nSolutions changes #
    ####################################

    nSolutions = [10,20,30,40,50,60,70,80,90,100]

    accuracy_nSolutions = []

    mean_nSolutions = []
    var_nSolutions = []
    std_nSolutions = []

    accuracy_iterations = []
    mean_iterations = []
    var_iterations = []
    std_iterations = []


    for solution in nSolutions:

        for i in range(0,100):
            population,a,mean,var,std = geneticAlgorithm(nSolutions = solution, maxGenerations = 10, mProb = 0.1,cProb=0.7,k=3,elitism=False)
            
            accuracy_iterations.append(a)
            mean_iterations.append(mean)
            var_iterations.append(var)
            std_iterations.append(std)

        accuracy_nSolutions.append(Average(accuracy_iterations))
        mean_nSolutions.append(Average(mean_iterations))
        var_nSolutions.append(Average(var_iterations))
        std_nSolutions.append(Average(std_iterations))

    print("nSolutions: ", nSolutions)
    print("Accuracy nSolutions: ",accuracy_nSolutions)

    valores_mochila, correlation, mean, var, std,p_value = calculateStatistics(population,nSolutions,accuracy_nSolutions)
            
    print("Valores mochila: ", valores_mochila)

    print("Correlación con nSolutions: ",correlation) # Correlación negativa. Tienen una tendencia opuesta.
    print("con una certeza de ",1-1-p_value)
    print("Media valor de la mochila: ", mean_nSolutions)
    print("Varianza valor de la mochila: ", var_nSolutions)
    print("Desviacion tipìca valor de la mochila: ",std_nSolutions)
    print()

    fig, ax = plt.subplots()

    ax.plot(nSolutions, accuracy_nSolutions)
    
    ax.set_xlim(10, 100)
    ax.set_ylim(0,1)
    
    ax.set_xlabel('Number of solutions')
    ax.set_ylabel('Accuracy')

    plt.plot()

    plt.savefig('accuracy_nSolutions.png')

    ####################################
    # Accuracy when maxGenerations changes #
    ####################################

    maxGenerations = [100,500,1000,1500,2000,2500,3000,3500,4000,5000,10000] #Number of generations

    accuracy_maxGenerations = []
    mean_maxGenerations = []
    var_maxGenerations = []
    std_maxGenerations = []

    accuracy_iterations = []
    mean_iterations = []
    var_iterations = []
    std_iterations = []

    for generation in maxGenerations:

        for i in range(0,100):
            population,a,mean,var,std = geneticAlgorithm(nSolutions = 10, maxGenerations = generation, mProb = 0.1,cProb=0.7,k=3,elitism=False)

            accuracy_iterations.append(a)
            mean_iterations.append(mean)
            var_iterations.append(var)
            std_iterations.append(std)

        accuracy_maxGenerations.append(Average(accuracy_iterations))

        mean_maxGenerations.append(Average(mean_iterations))
        var_maxGenerations.append(Average(var_iterations))
        std_maxGenerations.append(Average(std_iterations))


    print("MaxGenerations: ",maxGenerations)
    print("Accuracy maxGenerations: ",accuracy_maxGenerations)

    valores_mochila, correlation, mean, var, std,p_value = calculateStatistics(population,maxGenerations,accuracy_maxGenerations)
            
    print("Valores mochila: ", valores_mochila)

    print("Correlación con maxGenerations: ",correlation) # Correlación negativa. Tienen una tendencia opuesta.
    print("con una certeza de ",1-p_value)
    print("Media valor de la mochila: ", mean_maxGenerations)
    print("Varianza valor de la mochila: ", var_maxGenerations)
    print("Desviacion tipìca valor de la mochila: ",std_maxGenerations)

    fig, ax = plt.subplots()

    ax.plot(maxGenerations, accuracy_maxGenerations)
    
    ax.set_xlim(100, 10000)
    ax.set_ylim(0,1.01)
    
    ax.set_xlabel('Maximum Generations')
    ax.set_ylabel('Accuracy')

    plt.savefig('accuracy_maxGen.png')

    print()
    ###############################
    # Accuracy when cProb changes #
    ###############################
    
    cProb = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #Crossover probability

    accuracy_cProb = []
    mean_cProb = []
    var_cProb = []
    std_cProb = []

    accuracy_iterations = []
    mean_iterations = []
    var_iterations = []
    std_iterations = []

    for prob in cProb:
        
        for i in range(0,100):
            population,a,mean,var,std = geneticAlgorithm(nSolutions = 10, maxGenerations = 10, mProb = 0.1, cProb=prob, k=3,elitism=False)

            accuracy_iterations.append(a)
            mean_iterations.append(mean)
            var_iterations.append(var)
            std_iterations.append(std)


        accuracy_cProb.append(Average(accuracy_iterations))
        mean_cProb.append(Average(mean_iterations))
        var_cProb.append(Average(var_iterations))
        std_cProb.append(Average(std_iterations))

    print("cProb: ", cProb)
    print("Accuracy cProb: ",accuracy_cProb)
    
    valores_mochila, correlation, mean, var, std,p_value = calculateStatistics(population,cProb,accuracy_cProb)

    print("Valores mochila: ", valores_mochila)

    print("Correlación con cProb: ",correlation) # Correlación negativa. Tienen una tendencia opuesta.
    print("con una certeza de ",1-p_value)
    print("Media valor de la mochila: ", mean_cProb)
    print("Varianza valor de la mochila: ", var_cProb)
    print("Desviacion tipìca valor de la mochila: ",std_cProb)
    print()

    fig, ax = plt.subplots()

    ax.plot(cProb, accuracy_cProb)
    
    ax.set_xlim(0.1, 1)
    ax.set_ylim(0,1.01)
    
    ax.set_xlabel('Probability of crossover')
    ax.set_ylabel('Accuracy')



    plt.savefig('accuracy_cProb.png')

    #########################################
    # Accuracy when tournament size changes #
    #########################################

    k = [1,3,5,7,10] #Tournament selector size

    accuracy_kSize = []
    mean_kSize = []
    var_kSize = []
    std_kSize = []

    accuracy_iterations = []
    mean_iterations = []
    var_iterations = []
    std_iterations = []

    for size in k:
        for i in range(0,100):
            population,a,mean,var,std = geneticAlgorithm(nSolutions = 10, maxGenerations = 10, mProb = 0.1, cProb=0.7,k=size,elitism=False)

            accuracy_iterations.append(a)
            mean_iterations.append(mean)
            var_iterations.append(var)
            std_iterations.append(std)

        accuracy_kSize.append(Average(accuracy_iterations))
        mean_kSize.append(Average(mean_iterations))
        var_kSize.append(Average(var_iterations))
        std_kSize.append(Average(std_iterations))

    print("Tournament size: ", k)
    print("Accuracy Tournament size: ",accuracy_kSize)
    
    valores_mochila, correlation, mean, var, std,p_value = calculateStatistics(population,k,accuracy_kSize)

    print("Valores mochila: ", valores_mochila)

    print("Correlación con kSize: ",correlation) # Correlación negativa. Tienen una tendencia opuesta.
    print("con una certeza de ",1-p_value)
    print("Media valor de la mochila: ", mean_kSize)
    print("Varianza valor de la mochila: ", var_kSize)
    print("Desviacion tipìca valor de la mochila: ",std_kSize)
    print()

    fig, ax = plt.subplots()

    ax.plot(k, accuracy_kSize)
    
    ax.set_xlim(1, 10.1)
    ax.set_ylim(0,1.01)
    
    ax.set_xlabel('Tournament Size')
    ax.set_ylabel('Accuracy')



    plt.savefig('accuracy_kSize.png')

    ###############################
    ###Same with elitism###########
    ###############################

    ###############################
    # Accuracy when mProb changes #
    ###############################
    
    mProb = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #Mutation probability

    accuracy_mProb = []
    mean_mProb = []
    var_mProb = []
    std_mProb = []

    accuracy_iterations = []
    mean_iterations = []
    var_iterations = []
    std_iterations = []


    for prob in mProb:
        for i in range(0,100):
            population,a,mean,var,std = geneticAlgorithm(nSolutions = 10, maxGenerations = 10, mProb = prob,cProb=0.7,k=3,elitism=True)
            
            accuracy_iterations.append(a)
            mean_iterations.append(mean)
            var_iterations.append(var)
            std_iterations.append(std)

        accuracy_mProb.append(Average(accuracy_iterations))

        mean_mProb.append(Average(mean_iterations))
        var_mProb.append(Average(var_iterations))
        std_mProb.append(Average(std_iterations))

    print("mProb: ", mProb)
    print("Accuracy mProb: ",accuracy_mProb)
    
    valores_mochila, correlation, mean, var, std,p_value = calculateStatistics(population,mProb,accuracy_mProb)

    print("Valores mochila: ", valores_mochila)

    print("Correlación con mProb: ",correlation) # Correlación negativa. Tienen una tendencia opuesta.
    print("con una certeza de ",1-p_value)
    print("Media valor de la mochila: ", mean_mProb)
    print("Varianza valor de la mochila: ", var_mProb)
    print("Desviacion tipìca valor de la mochila: ",std_mProb)
    print()

    fig, ax = plt.subplots()

    ax.plot(mProb, accuracy_mProb)
    
    ax.set_xlim(0.1, 1)
    ax.set_ylim(0,1.01)
    
    ax.set_xlabel('Probability of mutation')
    ax.set_ylabel('Accuracy')

    plt.plot()




    plt.savefig('accuracy_mProb_with_elitism.png')

    ####################################
    # Accuracy when nSolutions changes #
    ####################################

    nSolutions = [10,20,30,40,50,60,70,80,90,100]

    accuracy_nSolutions = []

    mean_nSolutions = []
    var_nSolutions = []
    std_nSolutions = []

    accuracy_iterations = []
    mean_iterations = []
    var_iterations = []
    std_iterations = []

    for solution in nSolutions:
        
        for i in range(0,100):
            population,a,mean,var,std = geneticAlgorithm(nSolutions = solution, maxGenerations = 10, mProb = 0.1,cProb=0.7,k=3,elitism=True)

            accuracy_iterations.append(a)
            mean_iterations.append(mean)
            var_iterations.append(var)
            std_iterations.append(std)

        accuracy_nSolutions.append(Average(accuracy_iterations))
        mean_nSolutions.append(Average(mean_iterations))
        var_nSolutions.append(Average(var_iterations))
        std_nSolutions.append(Average(std_iterations))

    print("nSolutions: ", nSolutions)
    print("Accuracy nSolutions: ",accuracy_nSolutions)

    valores_mochila, correlation, mean, var, std,p_value = calculateStatistics(population,nSolutions,accuracy_nSolutions)
            
    print("Valores mochila: ", valores_mochila)

    print("Correlación con nSolutions: ",correlation) # Correlación negativa. Tienen una tendencia opuesta.
    print("con una certeza de ",1-p_value)
    print("Media valor de la mochila: ", mean_nSolutions)
    print("Varianza valor de la mochila: ", var_nSolutions)
    print("Desviacion tipìca valor de la mochila: ",std_nSolutions)
    print()

    fig, ax = plt.subplots()

    ax.plot(nSolutions, accuracy_nSolutions)
    
    ax.set_xlim(10, 100)
    ax.set_ylim(0,1)
    
    ax.set_xlabel('Number of solutions')
    ax.set_ylabel('Accuracy')

    plt.plot()

    plt.savefig('accuracy_nSolutions_with_elitism.png')

    ####################################
    # Accuracy when maxGenerations changes #
    ####################################

    maxGenerations = [100,500,1000,1500,2000,2500,3000,3500,4000,5000,10000] #Number of generations

    accuracy_maxGenerations = []
    mean_maxGenerations = []
    var_maxGenerations = []
    std_maxGenerations = []

    accuracy_iterations = []
    mean_iterations = []
    var_iterations = []
    std_iterations = []

    for generation in maxGenerations:

        for i in range(0,100):
            population,a,mean,var,std = geneticAlgorithm(nSolutions = 10, maxGenerations = generation, mProb = 0.1,cProb=0.7,k=3,elitism=True)

            accuracy_iterations.append(a)
            mean_iterations.append(mean)
            var_iterations.append(var)
            std_iterations.append(std)

        accuracy_maxGenerations.append(Average(accuracy_iterations))

        mean_maxGenerations.append(Average(mean_iterations))
        var_maxGenerations.append(Average(var_iterations))
        std_maxGenerations.append(Average(std_iterations))


    print("MaxGenerations: ",maxGenerations)
    print("Accuracy maxGenerations: ",accuracy_maxGenerations)

    valores_mochila, correlation, mean, var, std,p_value = calculateStatistics(population,maxGenerations,accuracy_maxGenerations)
            
    print("Valores mochila: ", valores_mochila)

    print("Correlación con maxGenerations: ",correlation) # Correlación negativa. Tienen una tendencia opuesta.
    print("con una certeza de ",1-p_value)
    print("Media valor de la mochila: ", mean_maxGenerations)    
    print("Varianza valor de la mochila: ", var_maxGenerations)
    print("Desviacion tipìca valor de la mochila: ",std_maxGenerations)

    fig, ax = plt.subplots()

    ax.plot(maxGenerations, accuracy_maxGenerations)
    
    ax.set_xlim(100, 10000)
    ax.set_ylim(0,1.01)
    
    ax.set_xlabel('Maximum Generations')
    ax.set_ylabel('Accuracy')

    plt.savefig('accuracy_maxGen_with_elitism.png')

    print()
    ###############################
    # Accuracy when cProb changes #
    ###############################
    
    cProb = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #Crossover probability

    accuracy_cProb = []
    mean_cProb = []
    var_cProb = []
    std_cProb = []

    accuracy_iterations = []
    mean_iterations = []
    var_iterations = []
    std_iterations = []

    for prob in cProb:
        for i in range(0,100):
            population,a,mean,var,std = geneticAlgorithm(nSolutions = 10, maxGenerations = 10, mProb = 0.1, cProb=prob, k=3,elitism=True)

            accuracy_iterations.append(a)
            mean_iterations.append(mean)
            var_iterations.append(var)
            std_iterations.append(std)

        accuracy_cProb.append(Average(accuracy_iterations))
        mean_cProb.append(Average(mean_iterations))
        var_cProb.append(Average(var_iterations))
        std_cProb.append(Average(std_iterations))

    print("cProb: ", cProb)
    print("Accuracy cProb: ",accuracy_cProb)
    
    valores_mochila, correlation, mean, var, std,p_value = calculateStatistics(population,cProb,accuracy_cProb)

    print("Valores mochila: ", valores_mochila)

    print("Correlación con cProb: ",correlation) # Correlación negativa. Tienen una tendencia opuesta.
    print("con una certeza de ",1-p_value)
    print("Media valor de la mochila: ", mean_cProb)
    print("Varianza valor de la mochila: ", var_cProb)
    print("Desviacion tipìca valor de la mochila: ",std_cProb)
    print()

    fig, ax = plt.subplots()

    ax.plot(cProb, accuracy_cProb)
    
    ax.set_xlim(0.1, 1)
    ax.set_ylim(0,1.01)
    
    ax.set_xlabel('Probability of crossover')
    ax.set_ylabel('Accuracy')



    plt.savefig('accuracy_cProb_with_elitism.png')

    #########################################
    # Accuracy when tournament size changes #
    #########################################

    k = [1,3,5,7,10] #Tournament selector size

    accuracy_kSize = []
    mean_kSize = []
    var_kSize = []
    std_kSize = []

    accuracy_iterations = []
    mean_iterations = []
    var_iterations = []
    std_iterations = []

    for size in k:
        for i in range(0,100):

            population,a,mean,var,std = geneticAlgorithm(nSolutions = 10, maxGenerations = 10, mProb = 0.1, cProb=0.7,k=size,elitism=True)

            accuracy_iterations.append(a)
            mean_iterations.append(mean)
            var_iterations.append(var)
            std_iterations.append(std)

        accuracy_kSize.append(Average(accuracy_iterations))
        mean_kSize.append(Average(mean_iterations))
        var_kSize.append(Average(var_iterations))
        std_kSize.append(Average(std_iterations))

    print("Tournament size: ", k)
    print("Accuracy Tournament size: ",accuracy_kSize)
    
    valores_mochila, correlation, mean, var, std,p_value = calculateStatistics(population,k,accuracy_kSize)

    print("Valores mochila: ", valores_mochila)

    print("Correlación con kSize: ",correlation) # Correlación negativa. Tienen una tendencia opuesta.
    print("con una certeza de ",1-p_value)
    print("Media valor de la mochila: ", mean_kSize)
    print("Varianza valor de la mochila: ", var_kSize)
    print("Desviacion tipìca valor de la mochila: ",std_kSize)
    print()

    fig, ax = plt.subplots()

    ax.plot(k, accuracy_kSize)
    
    ax.set_xlim(1, 10.1)
    ax.set_ylim(0,1.01)
    
    ax.set_xlabel('Tournament Size')
    ax.set_ylabel('Accuracy')



    plt.savefig('accuracy_kSize_with_elitism.png')



