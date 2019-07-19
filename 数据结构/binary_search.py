def binary_search(nums,target):
    #代码一：
    # #nums.sort()
    # start = 0
    # end = len(nums)-1
    # while start<=end:
    #     mid = (start+end)//2
    #     if nums[mid] == target:
    #         return True
    #     elif target < nums[mid]:
    #         end = mid - 1
    #     else:
    #         start = mid + 1
    #
    # return False
    #代码二：
    nums.sort()
    while len(nums) != 0:
        mid = len(nums)//2
        if nums[mid] == target:
            return True
        elif target < nums[mid]:
            nums = nums[0:mid]
        else:
            nums = nums[mid+1:]

    return False

testlist = [4,5,6,7,8,9,10]
res = binary_search(testlist,target=4)
print(res)