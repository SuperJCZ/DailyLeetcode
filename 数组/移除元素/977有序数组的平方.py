'''
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
'''



from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 双指针
        # 一个指针在开头，一个指针在结尾
        l = 0
        r = len(nums)-1
        ans = [0]*len(nums)
        curr = len(nums)-1

        while l <= r:
            if nums[l]**2 > nums[r]**2:
                ans[curr] = nums[l]**2
                l += 1
            else:
                ans[curr] = nums[r]**2
                r -= 1
            curr -= 1
        return ans


print(Solution().sortedSquares([1,1,1,]))