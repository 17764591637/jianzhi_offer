'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

dfs基本模板：
int check(参数)
{
    if(满足条件)
        return 1;
    return 0;
}
 
void dfs(int step)
{
        判断边界
        {
            相应操作
        }
        尝试每一种可能
        {
               满足check条件
               标记
               继续下一步dfs(step+1)
               恢复初始状态（回溯的时候要用到）
        }
}   
'''
class Solution:
    def exist(self, board, word):
        r,c = len(board),len(board[0])
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if self.dfs(board,i,j,word):
                        return True
        return False
    
    def dfs(self,tmp,i,j,word):
        if not word:
            return True
        if not(i>=0 and i<len(tmp)) or not (j>=0 and j<len(tmp[0])):
            return False
        if not tmp[i][j] == word[0]:
            return False
        tmp[i][j] += '#'
        print(tmp)
        res = self.dfs(tmp,i+1,j,word[1:]) or \
            self.dfs(tmp,i-1,j,word[1:]) or\
            self.dfs(tmp,i,j+1,word[1:]) or\
            self.dfs(tmp,i,j-1,word[1:])
        tmp[i][j] = tmp[i][j][:-1]
        return res

s = Solution()
res = s.exist(board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],word = "ABCCED")
print(res)