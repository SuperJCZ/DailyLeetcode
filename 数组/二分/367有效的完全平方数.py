'''
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
进阶：不要 使用任何内置的库函数，如sqrt 。
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 1.暴力：遍历1->sqrt(num)
        # 2.二分
        l,r,mid = 1,num,0
        while l <= r:
            mid = (l+r)//2
            if mid*mid == num:
                return True
            elif mid*mid <num:
                l = mid + 1
            elif mid*mid > num:
                r = mid - 1
        return False


print(Solution().isPerfectSquare(144))