import scala.collection.mutable.ArrayBuffer

class MovingAverage(_size: Int) {
    
    var window = new ArrayBuffer[Int]
    var sum = 0D
    
    def next(`val`: Int): Double = {
        if (window.size == _size) {

          sum -= window.remove(0)
        }
        
        window += `val`
        sum += `val`

        sum / window.length
    }

}