class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seq = ""
        max_length = 0

        for i in range(len(s)):

            while s[i] in seq:
                seq = seq[1:]

            seq += s[i]

            if len(seq)>max_length:
                max_length = len(seq)

        return max_length