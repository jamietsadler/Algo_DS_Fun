import scala.util.control.Breaks._
object Solution {
    def plusOne(digits: Array[Int]): Array[Int] = {
        var result = digits
        breakable {
            for(i <- (digits.size-1) to 0 by -1) {
                if(digits(i) != 9) {
                    result(i) += 1
                    break
                } else {
                    result(i) = 0
                    if(i == 0) {
                        // case [9] need to convert to [1,0]
                        result = Array(1) ++ result
                    }
                }
            }
        }
       result
    }
}