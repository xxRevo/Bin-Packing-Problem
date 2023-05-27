import random
import copy
import sys
import time
import statistics
import matplotlib.pyplot as plt

#brute force algorithm
def brute_force_algorithm(B,U_initial):
    start_time = time.time()
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
    elapsed_time = (time.time() - start_time) * 1000
    return (len(k)),elapsed_time

#heuristic algorithm
def heuristic_algorithm(B,U_initial):
    start_time = time.time()
    U = U_initial.copy()
    if (len(U) == 0):
        return 0,0
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
    elapsed_time = (time.time() - start_time) * 1000
    return (len(k)), elapsed_time

#random input generator
def random_input_generator(n,B):
    U = []
    for i in range(n):
        U.append(random.randint(1,B))
    return U

#RUN THIS PART FOR BRUTE FORCE & HEURISTIC ALGORITHM COMPARISON IN TERMS OF RUNTIME AND CORRECTNESS
"""
sys.stdout = open('output.txt', 'w')
run_number = 20
division_number = run_number
difference_total = 0
time_difference = 0
for x in range(run_number):
    B = random.randint(50,1000)
    n = random.randint(50,1000)
    U_initial = random_input_generator(n,B)
    b_result_bin, b_result_time = brute_force_algorithm(B,U_initial)
    h_result_bin, h_result_time = heuristic_algorithm(B,U_initial)
    print("RUN NUMBER:", x+1, "THE RESULT IS AS FOLLOWING:")
    print("Given",n, "items in U and bins with capacity B of", B)
    print("Brute force algorithm managed to pack input into", b_result_bin ,"bins in ",b_result_time, "miliseconds.")
    print("Heuristic algorithm managed to pack input into", h_result_bin ,"bins in ",h_result_time, "miliseconds.")
    print("\n")
    if(h_result_time == 0 or b_result_time == 0):
        division_number = division_number - 1
    else:
        time_difference = time_difference + (1- (h_result_time/b_result_time))
    difference_total = difference_total + (1- (b_result_bin/h_result_bin))
difference_total = difference_total/division_number
time_difference = time_difference/division_number
bin_efficiency = int((str(difference_total).split(".")[1])[:2])
time_efficiency = int((str(time_difference).split(".")[1])[:2])
print("In terms of achieving optimal number of bins; on average, brute force algorithm was %",bin_efficiency,"more efficient than heuristic algorithm.")
print("In terms of achieving optimal time to execute the algorithm; on average, heuristics algorithm was %",time_efficiency,"more efficient than brute force algorithm.")
sys.stdout.close()
"""

#RUN THIS PART FOR PERFORMANCE TESTING
"""
input_size=[]
runtime=[]
z_value = 1.645 
for y in range(100,10001,100):
    run_number = 20
    current_runtime_collection = []
    for x in range(run_number):
        B = 100
        n = y
        U_initial = random_input_generator(n,B)
        h_result_bin, h_result_time = heuristic_algorithm(B,U_initial)
        current_runtime_collection.append(h_result_time)
        if x == run_number-1:
            mean = statistics.mean(current_runtime_collection)
            stdev = statistics.stdev(current_runtime_collection)
            confidence_interval = (z_value * stdev) / (run_number ** 0.5)
            if (confidence_interval / mean) < 0.1:
                input_size.append(y)
                runtime.append(mean)
            else:
                run_number = run_number + 1

plt.plot(input_size, runtime, marker='o', linestyle='-', color='b')
plt.xlabel('Input Size')
plt.ylabel('Runtime (ms)')
plt.title('Input Size vs Runtime')
plt.show()
"""

#RUN THIS PART FOR CORRECTNESS TESTING
"""
sys.stdout = open('output_functional_testing.txt', 'w')
B = 1000
U_initial = [1,5,2,9,20]
h_result_bin, h_result_time = heuristic_algorithm(B,U_initial)
print("Test Case 1: All items can fit into 1 bin. Expected Result: 1")
print("Heuristic algorithm managed to pack input into", h_result_bin ,"bins.")
B = 1
U_initial = [1]
h_result_bin, h_result_time = heuristic_algorithm(B,U_initial)
print("Test Case 2: Only 1 item with size equal to capacity. Expected Result: 1 ")
print("Heuristic algorithm managed to pack input into", h_result_bin, "bins.")
B = 1
U_initial = []
h_result_bin, h_result_time = heuristic_algorithm(B,U_initial)
print("Test Case 3: No items to be binned. Expected Result: 0")
print("Heuristic algorithm managed to pack input into", h_result_bin, "bins.")
sys.stdout.close()
"""