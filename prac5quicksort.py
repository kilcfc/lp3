#DETERMINISTIC 

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quicksort(left) + [pivot] + quicksort(right)


arr = list(map(int, input("Enter numbers: ").split()))

print("Sorted array:", quicksort(arr))


#Randomized 


import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = []
    right = []

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)

    return quicksort(left) + [pivot] + quicksort(right)


arr = list(map(int, input("Enter numbers: ").split()))

print("Sorted array:", quicksort(arr))


# time complexity is O(nsquare)
