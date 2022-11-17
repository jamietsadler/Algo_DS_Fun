object Solution {
    def firstUniqChar(s: String): Int = {
        var hash_map = scala.collection.mutable.Map[Char, Int]()
        
        for (c <- s) {
            if (hash_map.contains(c)) hash_map(c) += 1
            else hash_map(c) = 1
        }
        
        for (i <- 0 to s.length()-1) {
            var c = s.charAt(i)
            if (hash_map(c) == 1){
                return i
            }
        }
        
        return -1
    }
}