# Question：
# https://leetcode.cn/problems/reverse-linked-list/

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # 双指针
        # curr = head
        # pre = None
        # while (curr != None):
        #     temp = curr.next
        #     curr.next = pre

        #     pre = curr
        #     curr = temp
        # return pre

        # 递归
        pre = None
        curr = head
        def reverse(pre,curr):
            if not curr:
                return pre

            tmp = curr.next
            curr.next = pre

            pre = curr
            curr = tmp

            return reverse(pre,curr)

        return reverse(pre,curr)


