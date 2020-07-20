def isSymmetric(root):
        if not root:
            return True
        stack = [[root.left, root.right]]
        while stack:
            t1, t2 = stack.pop()
            if t1 is None and t2 is None:
                continue
            elif t1 is None or t2 is None:
                return False
            elif t1.val == t2.val:
                stack.append([t1.left, t2.right])
                stack.append([t1.right, t2.left])
            else:
                return False
        return True
            
#         if not root:
#             return True
#         return check(root.left, root.right)
        
#     def check(t1, t2):
#         if t1 == None and t2 == None:
#             return True
#         elif t1 != None and t2 != None:
#             return t1.val == t2.val and check(t1.left, t2.right) and check(t1.right, t2.left)
#         return False