from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        N = len(arr)

        for i in range(N-1, -1, -1):
            if i + zeroes < N:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                
                if i + zeroes < N:
                    arr[i + zeroes] = arr[i]
        