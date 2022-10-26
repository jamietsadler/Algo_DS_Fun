/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def mergeTwoLists(list1: ListNode, list2: ListNode): ListNode = {
        if (list1 == null) return list2
        if (list2 == null) return list1
        
        if (list1.x > list2.x){
            list2.next = mergeTwoLists(list1, list2.next)
            return list2
        }
        
        else{
            list1.next = mergeTwoLists(list1.next, list2)
            return list1
        }
    }
}