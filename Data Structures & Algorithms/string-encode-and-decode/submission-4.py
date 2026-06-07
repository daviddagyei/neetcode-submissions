class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Append the length, a '#', and the actual string
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # i points to the start of the number. 
            # We need a second pointer 'j' to find the '#'
            j = i
            while s[j] != "#":
                j += 1
                
            # Now 'j' is sitting on the '#'. 
            # Everything between 'i' and 'j' is our length number!
            length = int(s[i:j])
            
            # The actual word starts at j+1, and ends at j+1+length.
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Move our main pointer 'i' to the start of the next encoded word
            i = j + 1 + length
            
        return res