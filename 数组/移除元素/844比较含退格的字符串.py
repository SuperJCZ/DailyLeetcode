from typing import List
'''
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

https://leetcode.cn/problems/backspace-string-compare/
'''

s = "#aa"
t = "a#"

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # 双指针
        def compute(s: str):
            s = list(s)
            l = curr = 0
            while curr < len(s):
                if s[curr] != "#":
                    s[l] = s[curr]
                    l += 1
                    curr += 1
                else:
                    l -= 1
                    l = max(0, l)
                    curr += 1
            return "".join(s[:l])
        s = compute(s)
        t = compute(t)
        return s == t

