# V1 - First, I sorted two arrays. Then, I iterated through the 'g' array. For each index in 'g', I iterated through the 's' array. If the 's' array element was equal to or greater than the 'g' array element, I incremented the result by 1. 555ms 🤦‍♂️
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        result = 0
        # Coockies
        s = sorted(s)
        # Kids
        g = sorted(g)
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j] >= g[i]:
                    s.pop(j)
                    result += 1
                    break
        return result
    
# V2 -  130 ms 😎
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # Coockies
        s.sort()
        # Kids
        g.sort()
        
        i, j = 0, 0
        ans = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                j += 1
                i += 1
                ans += 1
            else:
                j += 1
        return ans