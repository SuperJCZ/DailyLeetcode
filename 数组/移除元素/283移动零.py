'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = curr = 0
        while curr < len(nums):
            if nums[curr] == 0:
                curr += 1
            else:
                nums[left],nums[curr] = nums[curr],nums[left]
                curr += 1
                left += 1
        print(nums)

nums = [1,0,2,2,0,3,]

print(Solution().moveZeroes(nums))