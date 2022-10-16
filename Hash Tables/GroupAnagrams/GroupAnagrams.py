class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_map = {}
        for i in range(len(strs)):
            if tuple(sorted(strs[i])) in strs_map:
                strs_map[tuple(sorted(strs[i]))].append(strs[i])
            else:
                strs_map[tuple(sorted(strs[i]))] = [strs[i]]
        return strs_map.values()