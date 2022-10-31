# Question：
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/submissions/

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 双指针法

        ## 设置虚拟头
        dummy_node = ListNode()
        dummy_node.next = head

        ## 设置指针
        left,right = dummy_node,dummy_node

        ## 初始化右指针 初试到n+1位置：为了方便后续删除操作
        while n >= 0:
            right = right.next
            n -= 1

        ## 遍历nodes找到最后一个位置
        while right != None:
            left = left.next
            right = right.next

        ## 处理left前后的node
        left.next = left.next.next

        ## 还原虚拟头
        return dummy_node.next
