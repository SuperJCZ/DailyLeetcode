# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r,mid = 0,len(nums)-1,0

        while l <= r:
            # TODO 1.取mid
            mid = (l+r) // 2  # 偶数组的len是奇//2：在中间左边  # 奇数组的len是偶//2：在中间

            # TODO 2.判断nums[mid]在target哪边，更新l,r
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
        return -1

if __name__ == "__main__":
    nums = [0,1,9]
    target = 9
    print(Solution().search(nums, target))




