class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1
      
        while r > l:

            while not s[l].isalnum() and r> l:
                l += 1
            
            while not s[r].isalnum()  and r> l:
                r -= 1
            
            if s[r].lower() != s[l].lower()  and r> l:
                return False
            
            l += 1
            r -= 1
        return True