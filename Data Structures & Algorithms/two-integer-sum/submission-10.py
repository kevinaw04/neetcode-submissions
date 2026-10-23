class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i, num in enumerate (nums):
            required = target - num
            if required not in seen:
                seen[num] = i
            else: return [seen[required], i]
                


        
        

        
        