#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journey' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY path
#  2. INTEGER k
#

def journey(path, k):
    optimal_journey_points = optimal_journey(path, k, 0)
    return optimal_journey_points


def optimal_journey(path, k, points):
    if(len(path) <= 0):
        return points
    else:        
        values = []
        max_count = min(len(path),k)
        for i in range(max_count):
            values.append(optimal_journey(path[i+1:],k,points+path[i]))
        return max(values)            

if __name__ == '__main__':
    # path_count = int(str(input()).strip())

    # path = []

    # for _ in range(path_count):
    #     path_item = int(str(input()).strip())
    #     path.append(path_item)

    # k = int(str(input()).strip())

    path = [10 ,2, -20, -5]
    k=2
    print(str(path)+'-'+str(k) + '\n')
    result = journey(path, k)
    print(str(result) + '\n')
    


    path = [100, -70, -90, -80, 100]
    k=3
    print(str(path)+'-'+str(k) + '\n')
    result = journey(path, k)
    print(str(result) + '\n')


    path = [3 , -4, -5, -3, 0]
    k=2
    print(str(path)+'-'+str(k) + '\n')
    result = journey(path, k)
    print(str(result) + '\n')