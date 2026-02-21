def bubble_sort(n):
    flag = True
    while flag:
        for i in range (1, len(n)):
            if n[i-1] >= n[i]:
                n[i-1], n[i] = n[i], n[i-1]
            flag = False

    return n

print(bubble_sort([1, 3, 5, 7, 6, 10, 9]))