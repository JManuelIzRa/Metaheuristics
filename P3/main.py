

if __name__ == "__main__":

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