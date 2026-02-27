numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

index_unsorted = linear_search(numbers, 9)
print("Linear search (unsorted list) - index of 9 : ", index_unsorted)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    
    return arr

sorted_numbers = insertion_sort(numbers.copy())
print("\nSorted list using Insertion Sort: ")
print(sorted_numbers)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

index_sorted = binary_search(sorted_numbers, 9)
print("\nBinary search (sorted list) - index of 9: ", index_sorted)
             
         
