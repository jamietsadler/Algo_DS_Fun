class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                diff = abs(i - hash_map[nums[i]])
                if diff <= k:
                    return True
                else:
                    hash_map[nums[i]] = i
            else:
                hash_map[nums[i]] = i
        
        return False