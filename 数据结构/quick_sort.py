def quick_sort(nums,start,end):
    #递归退出的条件
    if start >= end:
        return
    mid = nums[start]
    left = start
    right = end

    while left < right:
        while left < right and nums[right] >= mid:
            right -= 1

        nums[left] = nums[right]

        while left < right and nums[left] < mid:
            left += 1

        nums[right] = nums[left]

    nums[left] = mid
    # 对基准元素左边的子序列进行快速排序
    quick_sort(nums, start, left - 1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(nums, left + 1, end)

alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist)-1)
print(alist)