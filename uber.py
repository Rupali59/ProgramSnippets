# Enter your code here. Read input from STDIN. Print output to STDOUT


def num_valid_triangles(arr):
    num_trianges = 0
    n = len(arr)
    for i in range(0,n-2):
        k_pos = i+2
        for j in range(i+1, n-1):
            if(k_pos == j):
                k_pos+=1
            valid_max_sum = arr[i]+arr[j]
            if(k_pos < n):
                while( k_pos < n and arr[k_pos] < valid_max_sum ):
                    k_pos = k_pos + 1
                    num_trianges = num_trianges + 1
            else:
                num_trianges = num_trianges + (k_pos- 1 - j)
                    
    return num_trianges

if __name__ == '__main__':
    # arr = [4,5,6,7,8,9,10]
    # arr = [2,3,5,6]
    arr = [2,4,6,8,16]
    res = num_valid_triangles(arr)
    print(res)
    