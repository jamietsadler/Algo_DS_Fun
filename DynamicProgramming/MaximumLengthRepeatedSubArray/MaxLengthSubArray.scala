object Solution {
    def findLength(nums1: Array[Int], nums2: Array[Int]): Int = {
        var memo = Array.ofDim[Int](nums1.length+1, nums2.length+1)
        for (i <-(nums1.length-1) to (0,-1)){
            for (j <- (nums2.length-1) to (0,-1)){
                if (nums1(i) == nums2(j)) memo(i)(j) = memo(i + 1)(j + 1) + 1
            }
        }
        memo.flatten.max
    }
}


