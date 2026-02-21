n = int(input())
print(n)
while True:
    if n == 1:
        break
    elif n % 2 == 0:
        n /=2
        print(int(n), end=' ')
    elif n % 2 != 0:
        n = n*3 + 1
        print(int(n), end=' ')

