def reverseList(head):
        # if head == None or head.next == None:
        #     return head
        # revList = reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return revList
        
        if not head:
            return head
        
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev