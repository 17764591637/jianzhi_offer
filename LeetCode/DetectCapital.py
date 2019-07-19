'''
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False

遍历的判断：
ASCII码中：
65-90 是 A-Z.
97-122 是 a-z.

若第一个字符是大写，则判断：
剩下的是否全是大写，剩下的是否全是小写。
若第一个字符是小写，则判断：
剩下的是否全是小写。
只有一个字符时，无论如何都是capital.

'''
class Solution(object):
    def detectCapitalUse(self,word):
        if len(word) < 2:
            return True

        letter_one = ord(word[0])
        if 65 <= letter_one <= 90:#第一个字母大写
            return self.letter_all_capital_or_lower(word[1:])

        return self.letter_all_lower(word[1:])

    def letter_all_capital_or_lower(self,str):
        left = 65
        right = 90

        if 97<= ord(str[0]) <=122:
            left = 97
            right = 122

        for i in str:
            if not left <= ord(i) <= right:
                return False

        return True

    def letter_all_lower(self,str):
        for j in str:
            if not 97 <= ord(j) <= 122:
                return False
        return True