class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        appears = set(nums)
        result = []
        for num in range(1, n+1):
            if num not in appears:
                result.append(num)
        return result