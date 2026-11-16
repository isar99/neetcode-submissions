class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_uniq = []
        for email in emails:
            local, domain = email.split("@")
            if "." in local:
                local = "".join(local.split("."))
            if "+" in local:
                local = local.split("+")[0]
            new_email = local + domain
            if new_email not in  emails_uniq:
                emails_uniq.append(new_email)
        return len(emails_uniq)
