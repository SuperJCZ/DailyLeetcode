# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 思路：
        # [a,b,c]
        # 1. tar < b -> [a]
        # 2. tar > b -> [c]

        # [a,b]
        # 1. tar > a -> [b]
        # 2. tar < a -> right = a.index-1 -> !stop

        # [a]
        # 1. tar > a -> l = a.index+1 -> 应该插入的位置是a后面+1
        # 2. tar < a -> r = a.index-1 -> 应该插入的位置是a.index
        l,r,mid = 0,len(nums)-1,0
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
        return r+1


if __name__ == "__main__":
    nums = [1,2,3,5,7]
    target = 4
    print(Solution().searchInsert(nums, target))