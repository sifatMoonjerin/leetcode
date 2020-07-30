class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None
    else:
        mid = len(nums)//2
        left = sortedArrayToBST(nums[:mid])
        right = sortedArrayToBST(nums[mid+1:])
        return TreeNode(nums[mid], left, right)


root = sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8])

print(root.val)
print(root.left)
print(root.right)
