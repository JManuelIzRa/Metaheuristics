import re

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

if __name__ == "__main__":

    list_of_dictionaries = readFile()

    solution = "['A', 'A', 'A', 'A', 'F', 'F', 'L', 'L', 'L', 'L']"
    print(type(solution)) 

    #for dictionary in list_of_dictionaries:
    
     #   if re.match("[('A'){4,5}?, ('F'){2,3}?, ('L'){4,5}?]",dictionary):
      #      print("Pass")
       # else:
        #    print("Fail")

    # Compara el número de elementos distintos que tienen los dos 
    cmp (dict1,dict2)