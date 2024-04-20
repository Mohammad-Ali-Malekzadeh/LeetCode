class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        i = 0
        while i < len(s):
            if s[i].isdigit():
                i += 1
                pass
            elif s[i].lower() == s[i].upper():
                s = s[:i] + s[i+1:]
            else:
                i += 1
        if s == s[::-1]:
            return True
        else:
            return False