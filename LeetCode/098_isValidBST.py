'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:
输入:[2,1,3]
    2
   / \
  1   3
输出: true
示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4。

思路：
中序遍历二叉树，遍历结果如果按照从小到大的顺序排列，则表明是二叉搜索树，否则不是二叉搜索树。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        self.res = []
        self.midorder(root)
        
        return sorted(list(set(self.res))) == self.res #验证是否有重复元素，并且是否是有序的
    
    def midorder(self,root):
        if not root:
            return
        self.midorder(root.left)
        self.res.append(root.val)
        self.midorder(root.right)
            


        