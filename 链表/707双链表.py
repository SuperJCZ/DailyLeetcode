# Question：
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

from typing import List


class Node:
    def __init__(self,val):
        self.prev = None
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self._head, self._tail = Node(0), Node(0)
        self._head.next, self._tail.prev = self._tail, self._head
        self._count = 0

    def get(self,index:int) -> None:
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index+1):
                node = node.next
            return node.val
        else:
            return -1

    def get_node(self,index:int) -> Node:
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index+1):
                node = node.next
            return node

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
            add_node.prev = prev_node
            add_node.next = curr_node
            curr_node.prev = add_node


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self._count:
            node = self.get_node(index)
            # 计数-1
            self._count -= 1
            node.prev.next, node.next.prev = node.next, node.prev