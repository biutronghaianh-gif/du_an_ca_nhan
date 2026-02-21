#viet lai thuat toan merge sort

def merge_sort(arr):

    if len(arr) == 1:
        return arr
    m = len(arr) // 2

    left = arr[:m]
    right = arr[m:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)

def merge(left, right):

    l = r = 0
    res = []

    while l < len(left) and r < len(right):
        if l < r:
            res.append(l)
            l += 1

        if r <l:
            res.append(r)
            r += 1

    res.extend(left[l:])
    res.extend(right[r:])

    return res

n = [1, 4, 3, 6, 5, 7, 9, 13, 11]

print(merge_sort(n))
    