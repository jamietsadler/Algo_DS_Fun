class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        shift = min(arr)
        K = max(arr) - shift
        counts = [0] *(K+1)
        for num in arr:
            counts[num-shift] += 1
        
        
        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        
        sorted_list = [0] * len(arr)
        for num in arr:
            sorted_list[counts[num-shift]] = num
            counts[num-shift] += 1
            
        for i in range(len(arr)):
            arr[i] = sorted_list[i]
            
        min_distance = float('inf')
        for i in range(len(arr)-1):
            min_distance = min(min_distance, arr[i+1] - arr[i])
        result = []
        i = 0
        
        while i < len(arr) - 1:
            if arr[i+1] - arr[i] == min_distance:
                result.append([arr[i], arr[i+1]])
            i += 1
            
        return result