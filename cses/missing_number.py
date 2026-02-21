n = int(input())
nums1 = list(map(int, input().split()))
nums2 = []
for i in range (n+1):
    nums2.append(i)
missing_num = sum(nums2) - sum(nums1)
print(missing_num)