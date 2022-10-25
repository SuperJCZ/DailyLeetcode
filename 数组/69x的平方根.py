class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0,1):
            return x

        l,r,mid = 1,x,0
        while l <= r:
            mid = (l+r)//2
            tar = x / mid

            if tar == mid:
                return mid

            elif tar < mid:
                r = mid-1

            elif tar > mid:
                l = mid+1
        return r

x = 2147395599
print(Solution().mySqrt(x))