list1 = list(map(str, input().split()))
danhsach = {}
for i in list1:
    if i not in danhsach:
        danhsach[i] = 1
    elif i in danhsach:
        danhsach[i] += 1

print(danhsach)