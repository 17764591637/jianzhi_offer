'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
思路：
对于一个二叉树的后序遍历序列来说，最后一个数一定是根节点，然后前面的数中，
从最开始到第一个大于根节点的之前数都是左子树中的数，而后面到倒数第二个数应该都是大于根节点的，是右子树，
如果后面的数中有小于根节点的，那么说明这个序列不是二叉搜索树的后序遍历序列
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False
        root_val = sequence.pop()
        index_ = -1
        for i in sequence:
            if i > root_val:
                index_ = sequence.index(i)
                break
        #print(index_)
        if index_ == -1:
            return True
        sequence = sequence[index_:]
        if sequence == []:
            return True   
        min_val = min(sequence)
        if root_val < min_val:
            return True
        return False
        
s = Solution()
res = s.VerifySquenceOfBST([4,8,6,12,16,14,10])
print(res)