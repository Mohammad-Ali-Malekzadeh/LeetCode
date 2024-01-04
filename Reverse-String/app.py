#! V1 - 205 ms 💔
#? .reverse() python builtin mehton is used in this solution

class Solution:
    def reverseString(self, s: list[str]) -> None:
        return s.reverse()
    
#! V2 - ? ms 😎
#? list[x::y] Used

    class Solution:
        def reverseString(self, s: list[str]) -> None:
            string = ''
            for i in s:
                string += i
            return list(string[::-1])