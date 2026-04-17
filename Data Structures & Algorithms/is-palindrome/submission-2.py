class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            
            if s[i].lower() != s[j].lower():
                return False

            i+=1
            j-=1
        return True

        # # remove all non-alphabetic or num
        # cleaned = ("".join(c for c in s if c.isalnum())).lower()

        # for i in range(len(cleaned)):
        #     if cleaned[i] != cleaned[len(cleaned)-1-i]:
        #         return False

        # return True