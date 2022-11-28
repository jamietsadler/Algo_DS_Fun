from typing import List
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashset = {}
        for i in range(len(cpdomains)):
            n, domain = cpdomains[i].split(' ')[0], cpdomains[i].split(' ')[1]
            while len(domain) > 0:
                if domain in hashset:
                    hashset[domain] += int(n)
                else:
                    hashset[domain] = int(n)
                domain = '.'.join(domain.split('.')[1:])
  
        
        return [f"{str(v)} {k}" for k, v in hashset.items()]