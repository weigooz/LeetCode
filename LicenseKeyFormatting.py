#License Key Formatting

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

        wo_dash = ''
        wo_dash = S.upper().replace('-','')

        first_grp = wo_dash[:len(wo_dash)%K]
        last_str = wo_dash[len(wo_dash)%K:]
        last_grp = []

        for i in range(0, len(last_str), K):
            last_grp.append(last_str[i:i+K])
            
        if first_grp != '':
            last_grp.insert(0, first_grp)
        
        return '-'.join(last_grp)
