import random
import copy
import sys

#brute force algorithm
def brute_force_algorithm(B,U_initial):
    U = U_initial.copy()
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
    return (len(k))

def heuristic_algorithm(B,U_initial):
    U = U_initial.copy()
    k = []
    k.append(B)
    while(len(U) != 0):
        could_not_bin = True
        for i in range(len(k)):
            if(k[i] >= U[0]):
                k[i] = k[i] - U[0]
                U.pop(0)
                could_not_bin = False
                break
        if (could_not_bin):
            k.append(B-U[0])
            U.pop(0)
    return (len(k))

#random input generator
def random_input_generator(n,B):
    U = []
    for i in range(n):
        U.append(random.randint(1,B))
    return U

#implementation of brute force algorithm

sys.stdout = open('output.txt', 'w')
run_number = 20
for x in range(run_number):
    B = random.randint(50,100)
    n = random.randint(50,100)
    U_initial = random_input_generator(n,B)
    b_result_bin = brute_force_algorithm(B,U_initial)
    h_result_bin = heuristic_algorithm(B,U_initial)
    print("RUN NUMBER:", x+1, "THE RESULT IS AS FOLLOWING:")
    print("Given",n, "items in U and bins with capacity B of", B)
    print("Brute force algorithm managed to pack input into", b_result_bin ,"bins." )
    print("Heuristic algorithm managed to pack input into", h_result_bin ,"bins." )
    print("\n")
sys.stdout.close()