
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        answer = set()
        for mail in emails:
            res, domain = mail.split('@')
            local = res.split("+")[0].replace(".", "")

     
            answer.add(local + "@" + domain)

        return len(answer)