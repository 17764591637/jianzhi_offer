class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        curr = 0
        count = 1
        nums.append('#')
        print(nums)
        for i in range(1,len(nums)-1):
            if nums[i] == nums[i-1]:
                count += 1
                if nums[i] != nums[i+1] and count >= 2:
                    count = 2
                    curr += count
                if nums[i] != nums[i+1] and count < 2:
                    curr += count

            if nums[i] != nums[i-1]:
                count = 1
                if nums[i] != nums[i+1]:
                    curr += 1
                if i == len(nums)-2:
                    curr += 1

        return curr
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for e in nums:
            if i < 2 or e != nums[i - 2]:
                nums[i] = e
                i += 1
        #print(nums)
        return i

s = Solution()
res = s.removeDuplicates([0,0,1,1,1,1,2,3,3])
print(res)