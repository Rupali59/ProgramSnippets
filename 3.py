
import math
import os
import random
import re
import sys

def distance_to_destination(source, destination, path_array, distance_covered, path_travelled):
    if(source == destination):
        print("distance_to_destination("+str(source)+", "+str(destination)+", path_array, " + str(distance_covered) + ", " +str(path_travelled)+")")
        return distance_covered,path_travelled;
    else:
        possible_destinations = get_connected_elements_to_point(source, path_array, path_travelled)
        if(len(possible_destinations) == 0):
            return -1
        else:
            possible_distance_covered = []
            for possible_destination in possible_destinations :
                d = path_array[source][possible_destination]
                p = (path_travelled[:])
                if(possible_destination not in p):
                    p.append(possible_destination)
                    rest_of_the_distance  = distance_to_destination(possible_destination, destination, path_array, d, p)
                    possible_distance_covered.append(d+rest_of_the_distance,path_travelled)
            distance = 1000000
            path = []
            for item in possible_distance_covered:
                if item[0]<distance:
                    distance = item[0]
                    position = item[1]
            return distance,position        
            

def get_connected_elements_to_point(source, path_array, path_travelled):
    destinations = []
    for possible_destination in range(len(path_array[source])):
        if path_array[source][possible_destination] != 0 and possible_destination not in path_travelled:
            destinations.append(possible_destination)
    return destinations

def number_of_available_cabs(arr):
    return sum(e==0 for e in arr)
    

def fill_path_array(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            arr[j][i] = arr[i][j] 
    return arr

if __name__ == '__main__':

    # source, destination = [int(x) for x in str(raw_input()).split()]

    path_array = []

    source = 0
    destination = 5
    path_array = [
                    [  0,  42,  53,  64,  75,  86,  97, 108, 119 ],
                    [  0,   0,  11,  12,  13,  14,  15,  16,  17],
                    [  0,   0,   0,  21,  22,  23,  24,  25,  26],
                    [  0,   0,   0,   0,  31,  32,  33,  34,  35],
                    [  0,   0,   0,   0,   0,  41,  42,  43,  44],
                    [  0,   0,   0,   0,   0,   0,  51,  52,  53],
                    [  0,   0,   0,   0,   0,   0,   0,  61,  62],
                    [  0,   0,   0,   0,   0,   0,   0,   0,  71],
                    [  0,   0,   0,   0,   0,   0,   0,   0,   0 ],
                ]
    res = distance_to_destination(source, destination, fill_path_array(path_array) ,0,[source])
    print(res)