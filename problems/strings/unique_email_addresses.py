# 929. Unique Email Addresses
# https://leetcode.com/problems/unique-email-addresses/description/


# Example 1:
# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

# Example 2:
# Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output: 3

from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq_email: set[str] = set()
        for email in emails:
            left_part, right_part = email.split("@")[0], email.split("@")[-1]
            left_part = left_part.split("+")[0].replace(".", "")
            email = left_part + "@" + right_part
            uniq_email.add(email)
        return len(uniq_email)
            
        
        
if __name__ == "__main__":
    sol = Solution()
    assert sol.numUniqueEmails(
        [
         "test.email+alex@leetcode.com",
         "test.e.mail+bob.cathy@leetcode.com",
         "testemail+david@lee.tcode.com"
        ]
    ) == 2