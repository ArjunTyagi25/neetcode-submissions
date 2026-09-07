class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email = set()

        for email in emails:
            local_name, domain_name = email.split("@")

            local_name_formatted = ""
            for c in local_name:
                if c == ".":
                    continue
                elif c == "+":
                    break
                else:
                    local_name_formatted += c

            email_formatted = local_name_formatted + "@" + domain_name
            unique_email.add(email_formatted)

        return len(unique_email)

            
        