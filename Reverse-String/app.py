#! V1 - 205 ms 💔
#? .reverse() python builtin mehton is used in this solution

class Solution:
    def reverseString(self, s: list[str]) -> None:
        return s.reverse()
    
#! V2 - 961 ms 🥲
#? Loop on the list. add the first index on the end of the array then delete it.

class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s)):
            if i == 0:
                s.insert(len(s), s[0])
            else:
                s.insert(-1 - (i -1), s[0])
            s.pop(0)
        return s
    
#! V3 - Not accept in Site
#? String[x::y] Used

class Solution:
    def reverseString(self, s: list[str]) -> None:
        string = ''
        for i in s:
            string += i
        return list(string[::-1])

#! V4 - Not accept in Site
#? List[x::y] Used
    
class Solution:
    def reverseString(self, s: list[str]) -> None:
        print(s[::-1])