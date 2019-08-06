'''
把长度为n的输入序列分成两个长度为n/2的子序列；
对这两个子序列分别采用归并排序；
将两个排序好的子序列合并成一个最终的排序序列。

时间复杂度O(nlogn) 稳定
缺点：需要额外的空间
'''

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    #二分分解
    num = len(nums)//2
    left = merge_sort(nums[:num])
    right = merge_sort(nums[num:])
    return merge(left,right)

def merge(left,right):
    '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
    l,r = 0,0
    result = []
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]

    return result

alist = [5,8,6,2,9]
res = merge_sort(alist)
print(res)
