#https://leetcode.cn/problems/fruit-into-baskets/
from collections import Counter
from typing import List

fruits = [1]

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fSet = Counter()
        l = 0
        max_len = 0

        for r,f in enumerate(fruits):
            fSet[f] += 1
            while len(fSet) > 2:
                fSet[fruits[l]] -= 1
                if fSet[fruits[l]] == 0:
                    fSet.pop(fruits[l])
                l += 1
            max_len = max(max_len,r-l+1)

        return max_len


print(Solution().totalFruit(fruits))