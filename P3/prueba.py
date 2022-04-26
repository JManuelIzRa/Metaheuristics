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

print(list_of_dictionaries)

solutions = []

#solutions.append('J', 'B', 'Q', 'T', 'B')
solutions.append('J')
solutions.append('A')
solutions.append('E')
solutions.append('C')
solutions.append('F')
solutions.append('O')
solutions.append('G')
solutions.append('H')
solutions.append('D')
solutions.append('L')


#print(solutions)


equal = 0
#print(solution)

for dictionary in list_of_dictionaries:
    
    #equal = 0
    last_epoch = 0    

       # print(element)
    for element in solutions:

        if type(element) == list:
                
            epoch_1 = dictionary.get(element[0])
            epoch_2 = dictionary.get(element[1])

            if epoch_1 and epoch_2 and epoch_1[0] == epoch_2[0]:                      
                        
                if last_epoch <= int(epoch_1[0]):

                    equal += 2

                    last_epoch = epoch_1[0]

                    dictionary[element[0]].pop(0)
                    dictionary[element[1]].pop(0)

        else:

            epoch = dictionary.get(element)

            if epoch:
                #print(f"{element}: epoch: {epoch[0]} last epoch:{last_epoch}")                                         
                    
                if int(epoch[0]) >= last_epoch:
                    
                    equal += 1
                        
                    last_epoch = int(epoch[0])

                    dictionary[element].pop(0)

                else:

                    equal -= 1
                    

        #print("Equal", equal)

       # if equal == len(dictionary.keys()):

         #   print("Concuerda")