class Solution:

    def encode(self, strs: List[str]) -> str:

        stri = ""
        for ele in strs:
            stri+= str(len(ele)) + "#" + ele

        return stri

    def decode(self, s: str) -> List[str]:
        i = 0
        l = []
        while i<len(s):
            j = i
            while s[j] != "#":
                j += 1

            x = int(s[i:j])
               
            l.append(s[j+1:j+1+x])
            i = j+1+x
        return l

    
                

