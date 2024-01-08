class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        result = 0
        for i in s:
            if i in g:
                del g[g.index(i)]
                result += 1
        return result