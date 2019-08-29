'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。
'''
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        numbers = [str(i) for i in numbers]
        res = []
        def backtrack(numbers,tmp):
            if not numbers:
                res.append(tmp)
                return
            for i in range(len(numbers)):
                backtrack(numbers[:i]+numbers[i+1:],tmp+numbers[i])
        backtrack(numbers,'')
        #print(res)

        return min(res)

s = Solution()
res = s.PrintMinNumber([3,32,321])
print(res)