# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys

def effecientCabScheduling(N, k, arr):
    t = 0
    cab_travel_duration = sorted(arr)
    cab_current_status = [0]*k

    while(N > 0):
        for i in range(k):
            if(cab_current_status[i] == 0 and N > 0):
                cab_current_status[i] = cab_current_status[i] + cab_travel_duration[i]
                N = N-1
        
        while number_of_available_cabs(cab_current_status) == 0:
            t = t+1
            cab_current_status = [x-1 for x in cab_current_status ]


    t = t + sum(cab_current_status)
    return t

def number_of_available_cabs(arr):
    return sum(e==0 for e in arr)
    

if __name__ == '__main__':

    n,k = [int(x) for x in str(raw_input()).split()]

    arr = []

    for _ in range(k):
        arr.append(int(raw_input().strip()))

    res = effecientCabScheduling(n, k, arr)
    print(res)