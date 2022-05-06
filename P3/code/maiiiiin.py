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

def evaluateSolution(solution, events, list_of_dictionaries):
    
    equal = 0

    for dictionary in list_of_dictionaries:
    
        #equal = 0
        last_epoch = 0    

        
        for element in solution:
            
            if type(element) == list:
                
                epoch_1 = dictionary.get(element[0])
                epoch_2 = dictionary.get(element[1])

                if epoch_1:                      
                    
                    if epoch_2:
                        
                        if int(epoch_1[0]) >= int(last_epoch):

                            equal += 2

                            last_epoch = epoch_1[0]

                            if element[0] == element[1]:
                                
                                dictionary[element[0]].pop(0)

                            else:
                                
                                dictionary[element[0]].pop(0)
                                dictionary[element[1]].pop(0)
                            
            else:

                epoch = dictionary.get(element)

                if epoch:                   
                    
                    if int(epoch[0]) >= int(last_epoch):
                    
                        equal += 1
                        
                        last_epoch = int(epoch[0])

                        dictionary[element].pop(0)

                    else:

                        equal -= 1

    #Returns the number of times that you find the events and penalize it when it doesnt match.
    return equal

def applyGeneticOperator(population, k, cProb, mProb):

    #Select parents through a tournament of size k
    #parents = TournamentSelection(population, k)

    #Cross parents with a probability cProb
    #if random.randint(1,100) <= cProb:
    #if random.uniform(0, 1) <=cProb:
        
    #children = cruzarPadres(parents,cProb)


    #Mutate parents with a probability mProb
    #if random.randint(1,100) <= mProb:
    #if random.uniform(0, 1) <=mProb:
        
    #children_mutate =  mutation(children, mProb)
    
    #population.clear()
    #population=children_mutate

    return population #Return the new population (not evaluated)


def geneticAlgorithm(nSolutions,maxGenerations,mProb,cProb,k,elitism):

    events = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
    list_of_dictionaries = readFile()

    ##n random valid solutions are created
    population = []
    pair = []
    solutions = []
    'C', 'G', 'G', ['S', 'G'], 'F'
    solutions.append('C')
    solutions.append('G')
    solutions.append('G')
    pair.append('S')
    pair.append('G')
    solutions.append(pair)
    solutions.append('F')
 
    

    print(solutions)

    
        
    population.append([solutions,evaluateSolution(solutions,events,list_of_dictionaries)])

    print(population)

    return population,accuracy


if __name__ == "__main__":

    #Genetic Algorithm
    accuracy_iterations = []
    accuracy = []

    
            
    population = geneticAlgorithm(nSolutions = 10, maxGenerations = 10, mProb = 0.2,cProb=0.7,k=3,elitism=False)

        #accuracy_iterations.append(a)

    #accuracy.append(Average(accuracy_iterations))