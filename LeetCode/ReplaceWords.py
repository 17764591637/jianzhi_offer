'''In English, we have a concept called root, which can be followed by some other
words to form another longer word - let's call this word successor.
For example, the root an, followed by other, which can form another word another.
Now, given a dictionary consisting of many roots and a sentence.
You need to replace all the successor in the sentence with the root forming it.
If a successor has many roots can form it, replace it with the root with the shortest length.
You need to output the sentence after the replacement.
Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
测试用例：
https://leetcode.com/problems/replace-words/description/'''
class Solution(object):
    def replaceWords(self, dict, sentence):

        for i in dict:
            res = []
            sentence = sentence.split()
            print(sentence)
            for j in sentence:
                if i == j[0:len(i)]:
                    if i not in j:
                        res.append(j)
                        continue
                    if i in j:
                        res.append(i)
                else:
                    res.append(j)

            sentence = ' '.join(res)

        return ' '.join(res)

s = Solution()
dict = ["ae","cr","bowu","slak","s","qvlg","geuw","qx","t","vzix","ycl","xoeyd","cq","jhjm","lt","uye","hwe"]
sentence = "anlrixkeqaexh"
res = s.replaceWords(dict,sentence)
print(res)