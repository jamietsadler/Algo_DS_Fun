/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def swapPairs(head: ListNode): ListNode = {
        if (head == null || head.next == null) return head
        else {
        val firstNode = head
        val secondNode = head.next
        
        firstNode.next  = swapPairs(secondNode.next);
        secondNode.next = firstNode;
        
        return secondNode}
    }
}