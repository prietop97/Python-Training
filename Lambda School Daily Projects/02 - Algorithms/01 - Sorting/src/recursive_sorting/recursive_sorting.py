# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    a = 0
    b = 0


    for i in range(elements):
        if a not in range(len(arrA)):
            merged_arr[i] = arrB[b]
            b += 1
        elif b not in range(len(arrB)):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] <= arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] > arrB[b]:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr





# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    
    middle = (len(arr)) // 2

    arrA = merge_sort(arr[:middle])
    arrB = merge_sort(arr[middle:])

    merged = merge(arrA,arrB)

    return merged


print(merge_sort([3,2,3,5,1,5,3,1,6,2233,532,235,5,34,12,21442,7]))



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO


    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if l == r:
        return arr[l]

    m = (r - l) - 1 // 2

    

#     return merge_sort_in_place(arr,l,r)

# print(merge_sort_in_place([1,2,3,5,3],0,4))



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):



    return arr

#print(timsort([1,2,3,2,3,5,7,2,52,2,4,5,6,8]))