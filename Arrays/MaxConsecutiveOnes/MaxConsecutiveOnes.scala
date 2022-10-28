object Solution {
    def findMaxConsecutiveOnes(nums: Array[Int]): Int = {
        var count = 0
        var maxcount = 0
        for (n <- nums){
            if (n == 1){
                count += 1
            } else{
                maxcount = count.max(maxcount)
                count = 0
            }
        }
        return maxcount.max(count)
    }
}