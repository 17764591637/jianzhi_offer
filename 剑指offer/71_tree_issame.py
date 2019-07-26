# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def issame(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 and root2:
            return root1.val==root2.val and issame(root1.left, root2.left) and issame(root1.right, root2.right)
        else:
            return False