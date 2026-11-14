class Solution:
    def helper(self, root: Optional[TreeNode], low: float, high: float) -> bool:
        if root:
            if root.left:
                if root.val > root.left.val and root.left.val > low:
                    if not self.helper(root.left, low, root.val):
                        return False
                else:
                    return False
            if root.right:
                if root.val < root.right.val and root.right.val < high:
                    if not self.helper(root.right, root.val, high):
                        return False
                else:
                    return False
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))