import multiprocessing
import random

def Average(lst):
    return sum(lst) / len(lst)

def readFile():
    # The dataset are going to be stored at a list of dictionaries
    list_of_dictionaries = []
    
    file = open("dataset_100_500.txt", "r")


    for line in file:
        
        # Delete the \n at the file
        split_line = line.strip('\n')
        # Delete the : at the file
        split_line = split_line.split(':')

        dictionary = {}

        # We iterate among the list to obtain the event and the epoch, for every patient we have one dictionary
        for pair in split_line:
            
            event = pair[0]

            epoch = pair[2:]

            # The event is the key of the dictionary and the epoch the value.
            if event in dictionary:
                dictionary[event].append(epoch)
                
            else:
                dictionary[event] = list()
                dictionary[event].append(epoch)

        list_of_dictionaries.append(dictionary)


    return list_of_dictionaries

def evaluateSolution_thread(solution, events, list_of_dictionaries, length, total, frequency, lock):
  
    for dictionary in list_of_dictionaries:
        
        #equal = 0
        last_epoch = 0
        count = 0    

        iterations = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0}

       # print(element)
        for element in solution:
            try:

                if type(element) == list:
                
                    epoch_1 = dictionary.get(element[0])
                    epoch_2 = dictionary.get(element[1])

                    if epoch_1:                      
                    
                        if epoch_2:
                        
                            index = iterations[element[0]]
                        
                            if int(epoch_1[index]) >= int(last_epoch) and epoch_1 == epoch_2:
                                
                                lock.acquire()
                                
                                total.value += 1
                                
                                lock.release()

                                count += 1

                                last_epoch = epoch_1[int(iterations[element[0]])]

                                if element[0] == element[1]:
                                
                                    iterations[element[0]] += 1

                                else:
                                
                                    iterations[element[0]] += 1
                                    iterations[element[1]] += 1

                            
                else:

                    epoch = dictionary.get(element)

                    if epoch:                   
                    
                        index = iterations[element]
                    
                        if int(epoch[int(index)]) >= int(last_epoch):
                            
                            lock.acquire()

                            total.value += 1
                            count += 1

                            lock.release()
                        
                            last_epoch = int(epoch[int(iterations[element])])

                        else:
                            lock.acquire()

                            total.value -= 1
                            count -= 1

                            lock.release()
   
            except IndexError:
                lock.acquire()

                total.value -= 1
                count -= 1

                lock.release()
            
                    

            if count == length:
                lock.acquire()

                frequency.value += 1

                lock.release()


    #Returns the number of times that you find the events and penalize it when it doesnt match.
    #return total, frequency

def evaluateSolution(solution, events, list_of_dictionaries, length):

    total = 0
    frequency = 0
    
    for dictionary in list_of_dictionaries:
        
        #equal = 0
        last_epoch = 0
        count = 0    

        iterations = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0}

       # print(element)
        for element in solution:
            try:

                if type(element) == list:
                
                    epoch_1 = dictionary.get(element[0])
                    epoch_2 = dictionary.get(element[1])

                    if epoch_1:                      
                    
                        if epoch_2:
                        
                            index = iterations[element[0]]
                        
                            if int(epoch_1[index]) >= int(last_epoch) and epoch_1 == epoch_2:

                                total += 1
                                count += 1

                                last_epoch = epoch_1[int(iterations[element[0]])]

                                if element[0] == element[1]:
                                
                                    iterations[element[0]] += 1

                                else:
                                
                                    iterations[element[0]] += 1
                                    iterations[element[1]] += 1

                            
                else:

                    epoch = dictionary.get(element)

                    if epoch:                   
                    
                        index = iterations[element]
                    
                        if int(epoch[int(index)]) >= int(last_epoch):
                    
                            total += 1
                            count += 1
                        
                            last_epoch = int(epoch[int(iterations[element])])

                        else:

                            total -= 1
                            count -= 1
   
            except IndexError:
                total -= 1
                count -= 1
            
                    

            if count == length:
                frequency += 1


    #Returns the number of times that you find the events and penalize it when it doesnt match.
    return total, frequency


def TournamentSelection(population, k):

    # Choose the parents of the population using tournaments of k participants.
    
    parents=[]
        
    # We generate as many childs as parents are at the moment at the population.
    for i in range(len(population)):
            
        # Randomly we select k parents for the tournament
        candidates=random.sample(population,k)
            
        # We order the candidates using it fitness value.
        candidates.sort(key=lambda candidates:candidates[1][0])
            
        # We choose the best candidate of the tournament.
        parents.append(candidates[k-1])
            
    return parents

def crossoverOnePoint(parent1,parent2):
   
 
    cruce=[]
    #Generamos aleatoriamente el punto a partir del cual se realiza el cruce de dos padres,
    x=random.randint(0,len(parent1)-2)
    #Realizamos el cruce valores de ambos padres desde la posicion x de cada  hasta el final,
    cruce.append(parent1[0:x+1]+parent2[x+1:len(parent2)])
    cruce.append(parent2[0:x+1]+parent1[x+1:len(parent1)])
    return cruce

def crossoverParents(parents,cProb):
   
    i=0
    crossover=[]
    while i<len(parents):
        if i+1 < len(parents): #Comprobamos que si el número de soluciones es impar, que el ultimo cromosoma no se cruzará con ninguno otro 
            if random.randint(1,100) <= (cProb*100):
                cruce=crossoverOnePoint(parents[i][0],parents[i+1][0])
                
                crossover.append([cruce[0],0])
                crossover.append([cruce[1],0])
                
            else:
                crossover.append(parents[i])
                crossover.append(parents[i+1])  
            
        else: #Al ser impar el número de soluciones, se guarda el último cromosoma tal cual
            crossover.append(parents[i])
            
        i=i+2  
            
        
    return crossover

def mutacionMultiplesGenes(hijo, events):
    
    #Genereamos un número aletorio de genes a mutar 
    n_genes=random.randint(1,len(hijo))
       
    for i in range(n_genes):
        
        gen_n=random.randint(0,len(hijo)-1) #Se genera la posición aletoria del cromosoma la cual se muta
        hijo[gen_n] = events[random.randint(0, len(events) - 1)]

    return hijo

def mutation(hijos,mProb, events):
    mutados=[]
    
    for nHijo in hijos:
        
        if random.randint(1,100)<=(mProb*100): #Comprobamos si se llega a mutar ese cromosoma ó no
            mutados.append([mutacionMultiplesGenes(nHijo[0], events)])
        else:
             mutados.append(nHijo)
                
    return mutados 

def applyGeneticOperator(population, k, cProb, mProb, events):

    #Select parents through a tournament of size k
    parents = TournamentSelection(population, k)

    #Cross parents with a probability cProb
    #if random.randint(1,100) <= cProb:
    #if random.uniform(0, 1) <=cProb:
        
    children = crossoverParents(parents,cProb)


    #Mutate parents with a probability mProb
    #if random.randint(1,100) <= mProb:
    #if random.uniform(0, 1) <=mProb:
        
    children_mutate =  mutation(children, mProb, events)
    
    population.clear()
    population=children_mutate

    return population #Return the new population (not evaluated)


def geneticAlgorithm(nSolutions,maxGenerations,mProb,cProb,k,elitism, length):

    events = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
    list_of_dictionaries = readFile()

    ##n random valid solutions are created
    population = []

    solutions = []

    # We create n valid solutions with a determined length (7-9,10-14, 15+)
    for i in range(nSolutions):
        solutions = []
        
        prob_occur_same_time = 0.9
        #while weight < maxWeight:
        it = 0
        while it < length:
            
            # It generates solutions with events that occur at the same time with a probability of 30%.
            if random.randint(1,100) <= (prob_occur_same_time*100):
                
                event = events[random.randint(0, len(events) - 1)]
                
                solutions.append(event)

            else:
               
                pair = []

                event = events[random.randint(0, len(events) - 1)]
                pair.append(event)

                event = events[random.randint(0, len(events) - 1)]
                pair.append(event)

                solutions.append(pair)
            
            it += 1

        population.append([solutions,evaluateSolution(solutions,events,list_of_dictionaries,length)])

    #Guradamos la solucion de elite de la generacion inicial en caso de utilizarse elitismo
    if elitism:
    
        population.sort(reverse=True,key=lambda population:population[1][0])
        eliteSolucion=population[0]

    it=0
    while it < maxGenerations:

        nSolutions = applyGeneticOperator(population,k,cProb,mProb,events)

        #Generational model
        population = []

        process = []
        for solution in nSolutions:

            # initial total and frequency (in shared memory)
            total = multiprocessing.Value('i',0)
            frequency = multiprocessing.Value('i',0)

            # creating a lock object
            lock = multiprocessing.Lock()

            # creating new processes
            p = multiprocessing.Process(target=evaluateSolution_thread, args=(solution[0],events,list_of_dictionaries,length,lock))

            process.append(p)

            # starting processes
            p.start()

            # wait until processes are finished
            p.join()

            population.append([solution[0], p])

        it+=1

        #Comprobamos si se utiliza elitismo
        if elitism:
            #Ordenamos la poblacion de forma descendente con respecto a su valor de fitness
            population.sort(reverse=True,key=lambda population:population[1][0])
                #Comprobamos si la solucion elite de la generación anterior es mejor que
                #la peor solucion de la  nueva generacion, y la conservamos en caso de ser asi 
            if population[len(population)-1][1] < eliteSolucion[1]:
                population.pop()
                population.append(eliteSolucion)
            #Guardamos la solucion elite de la nueva generación
            population.sort(reverse=True,key=lambda population:population[1][0])  
            eliteSolucion=population[0]
        
    return population


if __name__ == "__main__":

    #Genetic Algorithm
    accuracy_iterations = []
    accuracy = []
       
    population = geneticAlgorithm(nSolutions = 100, maxGenerations = 30 , mProb = 0.4,cProb=0.8,k=3,elitism=False, length = 10)

        #accuracy_iterations.append(a)
    population.sort(reverse=True,key=lambda population:population[1][0])

    print(population)