'''
例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
'''
class Solution:
    def ReverseSentence(self, s):
        # write code here
        res = []
        str_list = s.split(' ')
        print(str_list)
        for i in str_list[::-1]:
            res.append(i)
            
        
        return ' '.join(res)

s = Solution()
res = s.ReverseSentence('student. a am I')
print(res)