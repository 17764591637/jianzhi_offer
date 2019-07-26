# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorder(self, root):
        if root is None:
            return ''
        print(root.val)
        if root.left:
            self.preorder(root.left)
        if root.right:
            self.preorder(root.right)