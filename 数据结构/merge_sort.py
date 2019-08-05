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
