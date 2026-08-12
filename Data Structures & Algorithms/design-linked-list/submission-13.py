class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if (index < 0 or index >= self.length):
            return -1
        
        curr = self.head
        for i in range(0, index):
            curr = curr.next
        
        if (curr == None): return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head

        if new_node.next:
            new_node.next.prev = new_node

        self.head = new_node

        if self.length == 0:
            self.tail = new_node

        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        new_node.prev = self.tail

        if new_node.prev:
            new_node.prev.next = new_node
        
        self.tail = new_node

        if self.length == 0:
            self.head = new_node

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if (index < 0 or index > self.length):
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.length:
            self.addAtTail(val)
            return

        curr = self.head
        for i in range(0, index):
            curr = curr.next

        new_node = Node(val)
        new_node.prev = curr.prev
        new_node.next = curr

        curr.prev.next = new_node
        curr.prev = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        print("\n")
        self.print_list()
        if index >= self.length:
            return

        curr = self.head
        for i in range(0, index):
            curr = curr.next

        if (curr.prev == None):
            self.head = curr.next
        else:
            curr.prev.next = curr.next

        if (curr.next == None):
            self.tail = curr.prev
        else:
            curr.next.prev = curr.prev

        curr = None

        self.length -= 1

    def print_list(self) -> None:
        curr = self.head
        while curr:
            print(curr.val) 
            curr = curr.next


class Node:
    def __init__(self, val=None):
        self.prev = None
        self.next = None
        self.val = val


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
