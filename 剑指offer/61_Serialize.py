'''
请实现两个函数，分别用来序列化和反序列化二叉树

算法思想：根据前序遍历规则完成序列化与反序列化。所谓序列化指的是遍历二叉树为字符串；
        所谓反序列化指的是依据字符串重新构造成二叉树。依据前序遍历序列来序列化二叉树，
        因为前序遍历序列是从根结点开始的。当在遍历二叉树时碰到Null指针时，
        这些Null指针被序列化为一个特殊的字符“#”。另外，结点之间的数值用逗号隔开。

'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    flag = -1
    def Serialize(self, root):
        # write code here
        s = ''
        s = self.recursionSerialize(root,s)

        return s
    
    def recursionSerialize(self,root,s):
        if not root:
            s = '$,'#特殊字符   
            return s 
        s = str(root.val) + ','
        left = self.recursionSerialize(root.left,s)
        right = self.recursionSerialize(root.right,s)
        s += left+right

        return s 

    def Deserialize(self, s):
        # write code here
        self.flag += 1 
        l = s.split(',')
        if self.flag >= len(s):
            return None 
        root = None 
        if l[self.flag] != '$':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)

        return root 
