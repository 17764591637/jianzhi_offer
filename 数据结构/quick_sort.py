'''
快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。
具体算法描述如下：
1.从数列中挑出一个元素，称为 “基准”（pivot）；
2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

时间复杂度：O(nlogn)  不稳定
'''
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