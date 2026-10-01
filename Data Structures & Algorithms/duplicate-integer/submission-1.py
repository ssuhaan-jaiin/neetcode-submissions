class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        value_set = set()
        for element in nums:
            if element in value_set:
                return True
            else:
                value_set.add(element)
        return False
        