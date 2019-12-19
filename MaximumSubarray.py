class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #max sum
        max_sum = nums[0]
        #current sum
        temp_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < (temp_sum + nums[i]):
                temp_sum = temp_sum + nums[i]
            else:
                temp_sum = nums[i]
            
            if temp_sum > max_sum:
                max_sum = temp_sum
        
        return max_sum
