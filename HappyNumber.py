#Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_val(in_val):
            
            sum_val = 0
            while in_val > 0:
                in_val, digit = divmod(in_val, 10)
                sum_val = sum_val + digit**2
                
            return sum_val
            
        
        seen = set()
        while (n != 1) and (n not in seen):
            seen.add(n)
            n = get_val(n)
            
        return n ==1
