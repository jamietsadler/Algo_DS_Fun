object Solution {
    def sortList(head: ListNode): ListNode = {
        if ((head == null) || (head.next == null)) {
            return head
        }
        var fast = head.next
        var slow = head

        while ((fast != null) && (fast.next != null)){
            fast = fast.next.next
            slow = slow.next
        }

        var mid = slow.next
        slow.next = null
        var l = sortList(head)
        var r = sortList(mid)
        return merge(l, r)        
    }

    def merge(l: ListNode, r: ListNode): ListNode = {
        if (l == null) return r
        if (r == null) return l
        if (l.x > r.x) {
            r.next = merge(l, r.next)
            return r
        } else {
            l.next = merge(l.next, r)
            return l
        }
    }
}