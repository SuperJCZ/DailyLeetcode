# https://leetcode.cn/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 双指针
        left = curr = 0
        while curr < len(nums):
            if nums[curr] == val:
                curr += 1
            else:
                nums[left] = nums[curr]
                curr += 1
                left += 1

        return left


nums = [1,2,3,1]
val = 1
print(Solution().removeElement(nums, val))