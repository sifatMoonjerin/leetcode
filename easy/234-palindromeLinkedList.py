def isPalindrome(head):
    slow = head
    fast = head
    pre = None
    nex = None

    while fast != None and fast.next != None:
        nex = slow.next
        fast = fast.next.next
        slow.next = pre
        pre = slow
        slow = nex

    if fast != None:
        slow = slow.next

    while pre != None and slow != None:
        if pre.val != slow.val:
            return False
        pre = pre.next
        slow = slow.next

    return True
