# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。
from typing import List


class Solution:
    pass


if __name__ == "__main__":
    nums = [1,3,5,7]
    target = 4
    print(Solution().searchInsert(nums, target))