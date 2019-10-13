n,k = map(int,input().split())
nums = list(map(int,input().split()))

while k != 0:
    nums_no_zero = []
    for i in nums:
        if i != 0:
            nums_no_zero.append(i)
    if nums_no_zero == []:
        print(0)
    min_num = min(nums_no_zero)
    print(min_num)
    res = []
    for j in nums_no_zero:
        res.append(j-min_num)
    nums = res
    k -= 1




nums.sort()
res = [nums[0]]
for i in range(len(nums)-1):
    ans = nums[i+1] - nums[i]
    if ans > 0:
        res.append(ans)
    else:
        continue
    if len(res) == k:
        break
if len(res) < k:
    lis1 = [0] * (k-len(res))
    res.extend(lis1)

for j in res:
    print(j)
