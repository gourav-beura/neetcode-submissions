class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredStr = ""

        for ch in s:
            if ch.isalnum():
                filteredStr+=ch.lower()
        
        return filteredStr == filteredStr[::-1]

        