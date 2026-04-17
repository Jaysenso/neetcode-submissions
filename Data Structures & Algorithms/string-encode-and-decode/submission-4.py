class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = s.index("#", i) #find the next #
            length = int(s[i:j]) #find the length prefix
            word = s[j+1:j+1+length]
            decoded.append(word)
            i = j+1+length
        
        return decoded
