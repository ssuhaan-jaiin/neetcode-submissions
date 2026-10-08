class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # For this one, I would go by popping the max frequency element from the array
        # i times that is k times

        answer = []
        dic = {}
        

        for ele in nums:
                if ele in dic:
                    dic[ele] += 1
                else:
                    dic[ele]=1

        

        for i in range(k):
            max_count = 0
            max_ele = 0

            for ele in dic:
                if dic[ele]> max_count:
                    max_ele = ele
                    max_count = dic[ele]
            
            answer.append(max_ele)
            del dic[max_ele]

        return answer
                

            

            

        