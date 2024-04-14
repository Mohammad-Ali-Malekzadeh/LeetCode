class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        quality = ''
        for i in range(0, len(s)):
            quality = s[i+1:] + s[:i+1]
            
            if quality == goal:
                return True
        return False   