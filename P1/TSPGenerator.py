import random
import sys

def generator(nCities):
    tsp = []
    for i in range(nCities):
        distances = []
        for j in range(nCities):
            if j == i:
                distances.append(0)
            elif j < i:
                distances.append(tsp[j][i])
            else:
                distances.append(random.randint(10, 1000))
        tsp.append(distances)
    return tsp

def main():
    tsp = generator(int(sys.argv[1]))

    j = 1

    print('[')

    for i in tsp:
        
        if j == int(sys.argv[1]):
            print(i,']')
        else:
            print(i,',')
            j = j+1
        

if __name__ == "__main__":
    main()
