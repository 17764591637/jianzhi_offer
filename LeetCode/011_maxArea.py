class Solution:
    def maxArea(self, height):
        maxA = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                area = (j-i)*min(height[i],height[j])
                if area > maxA:
                    maxA = area
        return maxA

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        maxarea = 0
        while i < j:
            area = min(height[i],height[j])*(j-i)
            maxarea = max(maxarea,area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxarea

s = Solution()
list = [1,8,6,2,5,4,8,3,7]
res = s.maxArea(list)
print(res)