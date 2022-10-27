# Question：
# https://leetcode.cn/problems/minimum-window-substring/

import collections
from typing import List
s = "ADOBECODEBANC"
t = "ABC"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        1. 滑动窗口判断满足t in s的区间
        2. need表示t需要的每个元素的数量,tot_need=len(t)
        3. for中每次增加一个元素i
            if i in t & need[i]>0 -> need[i]-1, tot_need-1
            if i in t & need[i]<=0 -> need[i]-1
        4. 判断 if tot_need == 0 -> 元素全部包含
                滑动左边窗口l：if need[nums[l]]==0 -> 遇到了t中元素并且不能再滑动，跳出。
                                                    if r-l+1<res[1]-res[0] res=(l,r)
                                                    need[nums[l]]+=1 l+=1 tot_need+=1
                              else need[nums[l]] += 1, l+=1
        '''
        need = collections.Counter(list(t))
        tot_need = len(t)
        l = 0
        ans = ''
        min_len = float("inf")

        for r,letter in enumerate(s):
            if letter in need.keys() and need[letter] > 0:
                need[letter] -= 1
                tot_need -= 1
            elif letter in need.keys() and need[letter] <= 0:
                need[letter] -= 1

            while tot_need == 0:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    ans = s[l:r+1]
                if s[l] in need.keys():
                    if need[s[l]] == 0:
                        tot_need += 1

                    need[s[l]] += 1
                l += 1
        return ans


print(Solution().minWindow(s, t))

