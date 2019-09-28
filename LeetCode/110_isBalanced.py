'''
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点的左右两个子树的高度差的绝对值不超过1。
条件：
左子树是平衡二叉树。
右子树是平衡二叉树。
左右子树之间的深度不超过1.

示例 1:

给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, root):
        if not root:
            return True
        if not self.IsBalanced_Solution(root.left) or not self.IsBalanced_Solution(root.right):
            return False
        
        left_d = self.TreeDepth(root.left)
        right_d = self.TreeDepth(root.right)
        if abs(left_d-right_d) < 2:
            return True
            
        return False
     
    def TreeDepth(self,pNode):
        if not pNode:
            return 0
        nleft = self.TreeDepth(pNode.left)
        nright = self.TreeDepth(pNode.right)

        return max(nleft+1,nright+1)