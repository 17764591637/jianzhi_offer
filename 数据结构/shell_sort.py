def shell_sort(nums):
    n = len(nums)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            j = i
            while j >= gap and nums[j-gap] > nums[j]:
                nums[j-gap],nums[j] = nums[j],nums[j-gap]
                j -= gap
        gap = gap//2

alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)