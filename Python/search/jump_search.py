"""
NOTE:-Works only sorted arrays.
Time Complexity : O(√n)
Auxiliary Space : O(1)
SAMPLE INPUT line 1   1 2 3 4 5 6 7 8 9 10
SAMPLE INPUT line 2   5
SAMPLE OUTPUT     4
"""
import math


# main function
def jump_search_2(arr,search):
    """Takes in a sorted array arr and a value to search for"""
    interval = int(math.sqrt(len(arr)))

    ''' find last lowest element '''
    for i in range(0,len(arr),interval):
        if arr[i] < search:
            low = i
        elif arr[i] == search:
            return i
        else:
            break
    ''' apply linear search '''
    l_index = [e for e,i in enumerate(arr[low:low+interval]) if i == search]
    if l_index[0]:
        return low+l_index[0]
    return "Not Found"


# driver code
if __name__ == "__main__":
    ary = list(map(int, input().split()))
    val = int(input())
    res = jump_search(ary, val)
    print(res)
