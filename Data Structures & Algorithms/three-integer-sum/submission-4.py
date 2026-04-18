class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # i + j + k = 0

        #   i  j        k
        # [-4,-1,-1,0,1,2]
        #   i       j    k
        # [-1,-1,-1,0,1,1]

        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    #remove duplicates for left and right
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left +=1
                    right -=1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
                
        return res

