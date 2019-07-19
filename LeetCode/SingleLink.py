class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLink(object):
    def __init__(self):
        self._head = None

    def is_empty(self):

        return self._head == None

    def length(self):
        count = 0
        curr = self._head
        while curr != None:
            count += 1
            curr = curr.next

        return count

    def travel(self):
        curr = self._head
        while curr != None:
            print(curr.item)
            curr = curr.next
        print('')

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            curr = self._head
            while curr.next != None:
                curr = curr.next
            curr.next = node

    def add(self,item):
        node = Node(item)
        node.next == self._head
        self._head = node

    def insert(self,pos,item):
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            node = Node(item)
            curr = self._head
            count = 0
            while count != pos-1:
                curr = curr.next
                count += 1
            node.next = curr.next
            curr.next = node


    def remove(self,item):
        #两个游标，pre为curr的前一个节点
        curr = self._head
        pre = None
        while curr != None:
            if curr.item == item:
                if not pre:
                    self._head = curr.next
                else:
                    pre.next = curr.next
                break
            else:
                #往后移动
                pre = curr
                curr = curr.next

    def search(self, item):
        curr = self._head
        while curr != None:
            if curr.item == item:
                return True
            curr = curr.next

        return False


if __name__ == '__main__':
    s = SingleLink()
    print(s.is_empty())
    s.add(1)
    print(s.is_empty())
    s.append(1)
    print(s.travel())






