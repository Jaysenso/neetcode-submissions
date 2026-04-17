class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        
        # remove all non-alphabetic or num
        cleaned = ("".join(c for c in s if c.isalnum())).lower()

        for i in range(len(cleaned)):
            print(cleaned[i],cleaned[len(cleaned)-1-i])
            if cleaned[i] != cleaned[len(cleaned)-1-i]:
                return False

        return True