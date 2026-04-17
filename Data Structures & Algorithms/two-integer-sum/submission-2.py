class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff_dict = {}
        result = []

        for idx,num in enumerate(nums):
            difference = target - num

            if difference in diff_dict:
                result = [diff_dict.get(difference), idx]
                break
            else:
                diff_dict[num] = idx

        return result






