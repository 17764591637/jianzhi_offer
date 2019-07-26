# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def midorder(self, root):
        if root is None:
            return ''
        if root.left:
            self.midorder(root.left)
        print(root.val)
        if root.right:
            self.midorder(root.right)