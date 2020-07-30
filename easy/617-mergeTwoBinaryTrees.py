def mergeTrees(t1, t2):
    if t1 == None:
        return t2
    elif t2 == None:
        return t1
    else:
        t1.val += t2.val
        t1.left = mergeTrees(t1.left, t2.left)
        t1.right = mergeTrees(t1.right, t2.right)
        return t1
