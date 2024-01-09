class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        result = 0
        s = sorted(s)
        g = sorted(g)
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j] >= g[i]:
                    s.pop(j)
                    result += 1
                    break
        return result