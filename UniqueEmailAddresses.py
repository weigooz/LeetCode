#Unique Email Addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        after_apply_rules = set()

        for m_addr in emails:
            split_tmp = []
            localname_tmp = ''
            
            split_tmp = m_addr.split('@')
            localname_tmp = split_tmp[0].replace('.', '')
            
            if '+' in localname_tmp:
                plus_index = localname_tmp.find('+')
                localname_tmp = localname_tmp.replace(localname_tmp[plus_index:],'')

            after_apply_rules.add(localname_tmp +"@"+ split_tmp[1])
            
        return len(after_apply_rules)
