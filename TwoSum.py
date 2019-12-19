#Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        output_lst = []        
        
        for idx in range(len(nums)):
            co_number = target - nums[idx]                
            try:
                co_idx = nums.index(co_number)
                if idx != co_idx:
                    output_lst.append(idx)
                    output_lst.append(co_idx)
                    break
            except:
                continue
                
        return output_lst  
