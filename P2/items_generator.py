import random


num_items = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
weight = []
prize = []

for num in num_items:
    for i in range(0, num):
        
        prize.append(random.randint(30,600))
        weight.append(random.randint(5,100))
       
    print("Weight = ",weight)
    print("Prize = ", prize)
    print("Knapsack_size = ",25*len(weight))

    print("Weight_Max: ", max(weight))

    print()

    weight = []
    prize = []

