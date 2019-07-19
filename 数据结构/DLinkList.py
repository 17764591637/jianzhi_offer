class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

class DLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        curr = self._head
        count = 0
        while curr != None:
            count += 1
            curr = curr.next

        return count

    def travel(self):
        curr = self._head
        while curr != None:
            print(curr.item)
            curr = curr.next
        print(' ')

    def add(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            curr = self._head
            while curr.next != None:
                curr = curr.next
            curr.next = node
            node.prev = curr

    def search(self, item):
        """查找元素是否存在"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self,pos,item):
        if pos <= 0 :
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            curr = self._head
            count = 0
            while count < (pos-1):
                count += 1
                curr = curr.next
            node.prev = curr
            node.next = curr.next
            curr.next.prev = node
            curr.next = node

    def remove(self,item):
        if self.is_empty():
            return
        else:
            curr = self._head
            if curr.item == item:
                if curr.next == None:
                    self._head = None
                else:
                    curr.next.prev = None
                    self._head = curr.next
                return
            while curr != None:
                if curr.item == item:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    break
                curr = curr.next

if __name__ == "__main__":
    ll = DLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print ("length:",ll.length())
    ll.travel()
    print (ll.search(3))
    print (ll.search(4))
    ll.remove(1)
    print ("length:",ll.length())
    ll.travel()