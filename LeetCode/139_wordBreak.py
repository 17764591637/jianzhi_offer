'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：

    拆分时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。
示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
'''
class Solution:
    def wordBreak(self, s, wordDict):
        if not s:
            return True
        breakp = [0]
        # word = []
        for i in range(len(s)+1):
            for j in breakp:
                if s[j:i] in wordDict:
                    # word.append(s[j:i])
                    breakp.append(i)
                    break
        # print(breakp)
        # print(word)
        return breakp[-1] == len(s)
            
s = Solution()

res = s.wordBreak(s = "catsandog", wordDict = ["cats", "og", "sand", "and", "cat"])
print(res)