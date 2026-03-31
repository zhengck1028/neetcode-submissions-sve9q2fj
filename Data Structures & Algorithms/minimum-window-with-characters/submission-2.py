from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        hmT = Counter(t)
        # hm 只记录在 t 中出现过的字符，其他废话字符根本不进字典
        hm = {} 
        
        have, need = 0, len(hmT)
        res = ""
        resLen = float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            # 如果是目标字符，加入窗口统计
            if c in hmT:
                hm[c] = hm.get(c, 0) + 1
                # 当某个字符的数量【刚好】满足要求时，have + 1
                if hm[c] == hmT[c]:
                    have += 1

            # 一旦满足条件 (have == need)，就开始疯狂收缩左窗口
            while have == need:
                # 1. 更新最小结果
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                # 2. 尝试把左指针的字符踢出去
                left_char = s[l]
                if left_char in hmT:
                    hm[left_char] -= 1
                    # 如果踢掉后，数量不达标了，have - 1，破坏了循环条件
                    if hm[left_char] < hmT[left_char]:
                        have -= 1
                
                # 左指针右移，缩小窗口
                l += 1

        return res