class Node(object):
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    def __init__(self,root=None):
        self.root = root

    def add(self,elem):
        node = Node(elem)

        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                curr = queue.pop(0)
                if curr.lchild == None:
                    curr.lchild = node
                    return
                elif curr.rchild == None:
                    curr.rchild = node
                    return
                else:
                    queue.append(curr.lchild)
                    queue.append(curr.rchild)