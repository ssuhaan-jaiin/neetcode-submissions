class Solution:
    def maxArea(self, heights: List[int]) -> int:

        product = 0
        i1 = 0
        i2 = len(heights)-1


        
        while i1<i2:

            x = (i2-i1)*(min(heights[i2],heights[i1]))


            if x>product:
                product=x
                    
            if heights[i1]<heights[i2]:
                i1+=1
            else:
                i2-=1

        return product


        
  
        





