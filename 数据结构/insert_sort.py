def insert_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i,0,-1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

alist = [54,26,93,17,77,31,44,55,20]
insert_sort(alist)
print(alist)