def mergeTwoLists(l1, l2):
        if not l2: return l1
        if not l1: return l2
        if l1.val <= l2.val:
            nex = l1.next
            l1.next = mergeTwoLists(nex, l2)
            return l1
        else:
            nex = l2.next
            l2.next = mergeTwoLists(nex, l1)
            return l2
        
        
#         mergeHead = None
#         mergeTail = None
        
#         if not l1 or not l2:
#            return l1 if not l2 else l2 
#         elif l1.val <=l2.val:
#             mergeHead = l1
#             mergeTail = l1
#             l1 = l1.next
#         else:
#             mergeHead = l2
#             mergeTail = l2
#             l2 = l2.next
            
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 mergeTail.next = l1
#                 mergeTail = mergeTail.next
#                 l1 = l1.next
#             else:
#                 mergeTail.next = l2
#                 mergeTail = mergeTail.next
#                 l2 = l2.next
                
#         mergeTail.next = l1 if l2 == None else l2
        
#         return mergeHead
        