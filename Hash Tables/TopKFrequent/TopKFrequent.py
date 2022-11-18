
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums
        hmp = {}
        for i in range(len(nums)):
            if nums[i] in hmp:
                hmp[nums[i]] += 1
            else:
                hmp[nums[i]] = 1
        res = []
        
        values = hmp.values()
        values.sort(reverse = True)
        values = values[:k]
        for k, v in hmp.items():
            if v in values:
                res.append(k)
        return res