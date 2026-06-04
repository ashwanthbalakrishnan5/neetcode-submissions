class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_count = len(nums)
        for i in range(nums_count):
            for j in range(i+1,nums_count):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    
