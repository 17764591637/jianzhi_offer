def selection_sort(nums):
    n = len(nums)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[i],nums[min_index] = nums[min_index],nums[i]

alist = [54,226,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)