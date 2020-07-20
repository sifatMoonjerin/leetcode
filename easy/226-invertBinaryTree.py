def invertTree(root):
        # if root == None:
        #     return None
        # root.left, root.right = invertTree(root.right), invertTree(root.left)
        # return root
        
        queue = [root]
        while queue:
            r = queue.pop(0)
            if r == None: continue
            queue.append(r.left)
            queue.append(r.right)
            r.left, r.right = r.right, r.left
        return root
            