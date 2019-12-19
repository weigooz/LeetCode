#Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2 != 0:
            return False
        
        else:
            left_set = {'{','(','['}
            right_set = {'}',')',']'}
            stack_list = []

            for x in s:
                
                if stack_list == []:
                    if x in right_set:
                        return False
                    else:
                        stack_list.append(x)    
                        
                elif x in left_set:
                    stack_list.append(x)
                    
                elif x in right_set:
                    top_val = stack_list.pop()
                    if top_val == '{':
                        res_val = '}'
                    elif top_val == '[':
                        res_val = ']'
                    else:
                        res_val = ')'
                    if x != res_val:
                        return False
                    else:
                        continue
                        
            if stack_list == []:    
                return True
            else:
                return False
