class Solution(object):
    def counting_sort(self, lst, place_val):
        """
        Sorts a list of integers where minimum value is 0 and maximum value is K
        """
        # intitialize count array of size K
        counts = [0] * 10

        for elem in lst:
            digit = (elem // place_val) % 10
            counts[digit] += 1

        # we now overwrite our original counts with the starting index
        # of each digit over our group of digits
        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0] * len(lst)
        for elem in lst:
            digit = (elem // place_val) % 10
            sorted_lst[counts[digit]] = elem
            # since we have placed an item in index counts[digit],
            # we need to increment counts[digit] index by 1 so the
            # next duplicate digit is placed in appropriate index
            counts[digit] += 1

        # common practice to copy over sorted list into original lst
        # it's fine to just return the sorted_lst at this point as well
        for i in range(len(lst)):
            lst[i] = sorted_lst[i]

    def radix_sort(self, lst):
        # shift the minimum value in lst to be 0
        shift = min(lst)
        lst[:] = [num - shift for num in lst]
        max_elem = max(lst)

        # apply the radix sort algorithm
        place_val = 1
        while place_val <= max_elem:
            self.counting_sort(lst, place_val)
            place_val *= 10

        # undo the original shift
        lst[:] = [num + shift for num in lst]

        return lst

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        
        nums = self.radix_sort(nums)

        max_diff = 0

        for i in range(1, len(nums)):
            max_diff = max(max_diff, nums[i] - nums[i-1])
        
        return max_diff