import random

#brute force algorithm
def brute_force_algorithm(B,n,U):
    k = [] #initializing the bin array
    while(len(U) != 0):
        k.append(B-U[0])
        U.pop(0)
        search_for_more = True
        while(search_for_more):
            best_index = -1
            best_gap = -1
            for new_m in range(len(U)):
                if (k[-1] > U[new_m]) and ((best_gap > k[-1] - U[new_m]) or (best_gap == -1)) :
                    best_index = new_m
                    best_gap = k[-1] - U[new_m]
            if(best_gap == -1):
                search_for_more = False
            else:
                U.pop(best_index)
                k[-1] = best_gap
    print("RUN NUMBER: ", x+1, " THE RESULT IS AS FOLLOWING:")
    print(n," objects placed in ", len(k), " bins, each bin with capacity of ", B,"\n")

#def heuristic_algorithm():

#random input generator
def random_input_generator(n,B):
    U = []
    for i in range(n):
        U.append(random.randint(1,B))
    return U

#implementation of brute force algorithm
B = random.randint(50,100)
n = random.randint(50,100)
U = random_input_generator(n,B)
run_number = 20
for x in range(run_number):
    brute_force_algorithm(B,n,U)
    #heuristic_algorithm(B,n,U)