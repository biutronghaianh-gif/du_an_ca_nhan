n = int(input())
arr = list(map(int, input().split()))
counter = 0
for i in range(1,len(arr)):
    if arr[i] < arr[i-1]:
        diff = arr[i-1] - arr[i]
        arr[i] = arr[i] + diff
        counter += diff

print(counter)