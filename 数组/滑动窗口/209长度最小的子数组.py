# https://leetcode.cn/problems/minimum-size-subarray-sum/

from typing import List

target = 7
nums = [2,3]

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        l,r = 0,0
        tot = 0
        for r in range(len(nums)):
            tot += nums[r]
            while tot >= target:
                ans = min(ans,r-l+1)
                tot -= nums[l]
                l += 1
        return ans if ans != float("inf") else -1


print(Solution().minSubArrayLen(target, nums))