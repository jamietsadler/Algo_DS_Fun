object Solution {
    def climbStairs(n: Int): Int = {
        if (n < 2) return 1
        if (n == 2) return 2
        var first = 1
        var second = 2
        
        for (i <-3 to n){
            var total = first + second
            first = second
            second = total
        }
        
        return second
        
    }
}