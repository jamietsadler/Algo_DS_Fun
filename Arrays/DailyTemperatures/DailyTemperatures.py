class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if not temperatures:
            return None
        
        answer = [0] * len(temperatures)
        max_temp = 0
        
        for i in range(len(temperatures)-1, -1, -1):
            if temperatures[i] >= max_temp:
                max_temp = temperatures[i]
                continue
                
            difference = 1
            while temperatures[i] >= temperatures[difference+i]:
                difference += answer[i + difference]
            
            answer[i] = difference
            
        return answer
        