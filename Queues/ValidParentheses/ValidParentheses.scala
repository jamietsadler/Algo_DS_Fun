object Solution {
    def isValid(s: String): Boolean = {
        val stack = new scala.collection.mutable.Stack[Char]()
        
        for (chr <- s) chr match{
            case '(' | '{' | '[' => stack.push(chr)
            case _ =>  if (stack.isEmpty || math.abs(chr - stack.pop) > 2) return false
        }
        
        stack.isEmpty
        
    }
}
