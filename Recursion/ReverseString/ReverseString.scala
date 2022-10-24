object Solution {
    def reverseString(s: Array[Char]): Unit = {
        
        def loop(first: Int, second: Int): Unit = {
            if (first > second) ()
            else {
                val tmp = s(first)
                s(first) = s(second)
                s(second) = tmp
                loop(first + 1, second - 1)
            } 
        
        };
        loop(0, s.length - 1)
    }
}
