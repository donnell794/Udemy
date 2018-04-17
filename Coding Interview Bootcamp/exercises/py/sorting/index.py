# --- Directions
# Implement bubbleSort, selectionSort, and mergeSort

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if arr[i] != arr[min]:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
    return arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    arr = []
    while left and right:
        if left[0] < right[0]:
            arr.append(left.pop(0))
        else: arr.append(right.pop(0))
    return arr + left + right
