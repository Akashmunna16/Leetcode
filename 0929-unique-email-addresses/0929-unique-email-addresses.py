class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            
            # Rule 1: Split by '+' and keep only the first part
            local = local.split('+')[0]
            # Rule 2: Remove all periods '.'
            local = local.replace('.', '')
            
            # Reconstruct the finalized clean email address
            unique_emails.add(local + '@' + domain)
            
        return len(unique_emails)