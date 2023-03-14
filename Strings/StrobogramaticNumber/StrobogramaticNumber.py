
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pairing = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }

        res = []
        def backtrack(start, finish):
            if len(start) + len(finish) == n:
                res.append("".join(start) + "".join(finish[::-1]))
                return

            elif len(start) +len(finish) == n -1:
               res.append("".join(start) + "0" + "".join(finish[::-1]))
               res.append("".join(start) + "1" + "".join(finish[::-1]))
               res.append("".join(start) + "8" + "".join(finish[::-1]))

               return

            for k in pairing.keys():
                if k == "0" and not start:
                    continue
                start.append(k)
                finish.append(pairing[k])
                backtrack(start, finish)
                start.pop()
                finish.pop()
            
        backtrack([], [])
        return res

