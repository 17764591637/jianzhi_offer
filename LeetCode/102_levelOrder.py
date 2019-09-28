'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        que = [root]
        res = []
        if root == None:
            return res
        while que:
            tmp = []
            for _ in range(len(que)):
                ptr = que.pop(0)
                tmp.append(ptr.val)
                if ptr.left != None:
                    que.append(ptr.left)
                if ptr.right != None:
                    que.append(ptr.right)
            res.append(tmp)
            
        return res

        