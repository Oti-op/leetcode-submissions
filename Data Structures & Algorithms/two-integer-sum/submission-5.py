class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            c = target - x
            if c in seen:
                return [seen[c], i]
            seen[x] = i
