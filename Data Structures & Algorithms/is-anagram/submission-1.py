class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams - same characters and same lengths and occurences
        # Create a dictionary and check the values
        # O(n)

        dict_s = {}
        dict_t = {}

        for characterS in s:
            if characterS in dict_s:
                dict_s[characterS] += 1
            else:
                dict_s[characterS] = 1

        for characterT in t:
            if characterT in dict_t:
                dict_t[characterT] += 1
            else:
                dict_t[characterT] = 1
        
        return dict_s == dict_t
            

        