s = input()

max_len = 1
count_len = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count_len +=1
    else:
        count_len = 1

    max_len = max(max_len, count_len)

print(max_len)