def binary_search(arr, target):
    left = 0
    right = len(arr) -1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid +1
        elif arr[mid] > target:
            right = mid - 1
    return -1
        
arr = list(map(int, input().split()))
target = int(input())
print(binary_search(arr, target))
