# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。
from typing import List


class Solution:

    # 应该左开右闭的方法：左闭右闭时最后一个指到最后一个元素时无法确定插入位置在元素的左边还是右边
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r,mid = 0,len(nums)-1,0

        # len(nums) = 1
        if len(nums) == 1:
            return 0 if target < nums[0] or target == nums[0] else 1

        # len(nums) != 1
        else:
            ## target < min(nums) or target > max(nums)
            if target < min(nums) or target > max(nums):
                return 0 if target < nums[0] else len(nums)

            ## target between min(nums) and max(nums)
            else:
                while l < r:
                    mid = (l+r)//2
                    if target == nums[mid]:
                        return mid
                    elif target < nums[mid]:
                        l = mid
                    else:
                        r = mid
                return r


if __name__ == "__main__":
    nums = [1,3,5,7]
    target = 4
    print(Solution().searchInsert(nums, target))