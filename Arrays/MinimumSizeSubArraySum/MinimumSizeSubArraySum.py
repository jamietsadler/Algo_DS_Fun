class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        p1=0
        p2=0

        total=0
        res=float('inf')

        while(p2<len(nums)):
            total=total+nums[p2]
            if total<s:
                p2+=1
            else:
                res=min(res,p2-p1+1) 
                total=total-nums[p1]-nums[p2]
                p1+=1

        return res if res<float('inf')  else 0      