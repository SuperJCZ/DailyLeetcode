# Question：
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self._head = Node(0)
        self._count = 0

    def get(self, index: int) -> int:
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        index = (0 if index < 0 else index)
        if index > self._count:
            return

        self._count += 1

        add_node = Node(val)
        prev_node, curr_node = None, self._head
        for _ in range(index + 1):
            prev_node, curr_node = curr_node, curr_node.next
        else:
            prev_node.next = add_node
            add_node.next = curr_node

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._count:
            self._count -= 1
            prev_node, curr_node = None, self._head
            for _ in range(index + 1):
                prev_node, curr_node = curr_node, curr_node.next
            else:
                prev_node.next, curr_node.next = curr_node.next, None
        else:
            return
