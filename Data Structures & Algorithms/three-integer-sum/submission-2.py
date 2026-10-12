class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        nums.sort()
        #parent loop
        for i in range(len(nums)):

            #last scan for triplet
            if i<len(nums)-2 and not(i>0 and nums[i]==nums[i-1]):


                target = -nums[i]
                i1 = i+1
                i2 = len(nums) -1

                while i1<i2:
                    ans = nums[i1]+nums[i2]
                    if ans==target:
                        l.append([nums[i],nums[i1],nums[i2]])
                        i1+=1
                        i2-=1

                        while i1 < i2 and nums[i1] == nums[i1 - 1]:
                            i1 += 1

                        while i1 < i2 and nums[i2] == nums[i2 + 1]:
                            i2 -= 1

                            
                    elif ans<target:
                        i1+=1
                    else:
                        i2-=1
                    
        return l

        