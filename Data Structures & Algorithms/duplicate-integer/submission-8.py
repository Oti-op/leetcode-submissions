class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for num in nums:
            if num in seen:
                return True
            seen[num] = num
        else:
            return False



        
 


        