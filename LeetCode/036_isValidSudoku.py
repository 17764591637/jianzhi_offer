class Solution:
    def isValidSudoku(self,board):
        #init data
        rows = [{} for i in range(9)]#计算每一行的数字的个数
        columns = [{} for i in range(9)]#计算每一列的数字的个数
        boxes = [{} for i in range(9)]

        #validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num) 
                    box_index = (i//3)*3 + j//3
                    rows[i][num] = rows[i].get(num,0) + 1#调用get()方法，返回的是对应的value值
                    columns[j][num] = columns[j].get(num,0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num,0) + 1
                    
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False

        return True

s = Solution()
res = s.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])
print(res)