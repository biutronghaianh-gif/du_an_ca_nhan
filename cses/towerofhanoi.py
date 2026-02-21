# bai toan ap dung de quy

def hanoi(num, start, end): 
    if num == 1:
        pm(start, end)
    else:
        others = 6 - (start + end)

        hanoi(num-1, start, others)

        pm(start, end)

        hanoi(num-1, others, end)


def pm(start, end):
    print(start, '->', end)


nums = int(input())
start, end = map(int, input().split())

print(hanoi(nums, start, end))