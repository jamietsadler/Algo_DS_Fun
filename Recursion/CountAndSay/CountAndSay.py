
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def helper(s):
            count = 1
            res = ''
            for i in range(0, len(s)):

                if i < len(s) - 1 and s[i+1] == s[i]:
                    count += 1
                else:
                    tmp = str(count) + s[i]
                    res = res + tmp
                    count = 1

            return res

        total = '1'
        for i in range(1, n):
            print(total)
            total = helper(total)

        print(total)
        return total

        