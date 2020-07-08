def maxDepth(root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            return 1+max(left, right)

