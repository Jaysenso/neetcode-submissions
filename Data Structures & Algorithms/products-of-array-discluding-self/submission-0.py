class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    
        # BRUTE FORCE METHOD
        curr_idx = 0
        result = []

        for curr_idx, curr_num in enumerate(nums):
            total_sum = 1

            for idx, num in enumerate(nums):
                if curr_idx == idx:
                    continue
                total_sum *= num

            result.append(total_sum)

        return result        
        