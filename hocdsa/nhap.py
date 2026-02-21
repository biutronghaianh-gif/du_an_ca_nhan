def tinhtoan(a, b, c):
    if b == 0:
        return 1
    else:
        return a*tinhtoan(a, b-1, c)%c
    
print(tinhtoan(2, 10, 1000))