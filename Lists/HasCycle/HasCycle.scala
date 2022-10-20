/**
 * Definition for singly-linked list.
 * class ListNode(var _x: Int = 0) {
 *   var next: ListNode = null
 *   var x: Int = _x
 * }
 */

import scala.annotation.tailrec
object Solution {
    def hasCycle(head: ListNode): Boolean = {
        @tailrec
        def loop(slow: ListNode, fast: ListNode): Boolean = {
            if (slow == fast) true
            else if (fast == null || fast.next == null) false
            else loop(slow.next, fast.next.next)
        }
      
        if (head == null || head.next == null) false else loop(head.next, head.next.next)        
    }
}