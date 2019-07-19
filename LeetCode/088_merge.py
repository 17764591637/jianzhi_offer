class Solution(object):
  def merge(self, nums1, m, nums2, n):
    end = m + n - 1
    m -= 1
    n -= 1
    while end >= 0 and m >= 0 and n >= 0:
      if nums1[m] > nums2[n]:
        nums1[end] = nums1[m]
        m -= 1
      else:
        nums1[end] = nums2[n]
        n -= 1

      end -= 1

    while n >= 0:
      nums1[end] = nums2[n]
      end -= 1
      n -= 1

s = Solution()
res = s.merge([1,2,3,0,0,0],3,[2,5,6],3)
print(res)