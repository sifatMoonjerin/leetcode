def reverseList(head):
        # if head == None or head.next == None:
        #     return head
        # revList = reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return revList
        
        if not head:
            return head
        
        p = None
        c = head
        n = None
        
        while c != None:
            n = c.next
            c.next = p
            p = c
            c = n
        
        return p