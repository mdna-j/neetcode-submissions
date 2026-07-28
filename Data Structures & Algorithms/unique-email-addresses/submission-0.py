class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            
            # Ignore everything after the first '+'
            if '+' in local:
                local = local.split('+')[0]
                
            # Remove all dots '.'
            local = local.replace('.', '')
            
            # Add unique combination
            unique_emails.add((local, domain))
            
        return len(unique_emails)
        