from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize count
        count_dict = defaultdict(int)
        result = []

        for num in nums:
            count_dict[num] += 1

        sorted_list = sorted(count_dict.items(), key = lambda x: x[1], reverse=True)

        for item in sorted_list[:k]:
            result.append(item[0])

        return result
        
