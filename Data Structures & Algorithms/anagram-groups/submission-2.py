class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_groups = {}

        for word in strs:
            character_counts = {}

            for character in word:
                if character in character_counts:
                    character_counts[character] += 1
                else:
                    character_counts[character] = 1

            anagram_key = tuple(sorted(character_counts.items()))

            if anagram_key in anagram_groups:
                anagram_groups[anagram_key].append(word)
            else:
                anagram_groups[anagram_key] = [word]

        return list(anagram_groups.values())