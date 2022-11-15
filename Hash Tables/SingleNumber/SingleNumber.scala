object Solution {
    def singleNumber(nums: Array[Int]): Int = {
        val map = scala.collection.mutable.Map[Int, Int]()
        
        for (x <- nums){
            if (map contains x){
                map(x) += 1
            } else {
                map.put(x, 1)
            }            
        }
        
        for (x <- nums){
            if ((map get x) == 1){
                return x
            }          
        }
        
        return 0 
    }
}