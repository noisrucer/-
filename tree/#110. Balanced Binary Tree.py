class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height = True
        self.depth(root)

        return self.height

    def depth(self, root):
        
        if not root:
            return False
        
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        if abs(left_depth - right_depth) > 1:
            self.height = False
        
        return max(left_depth, right_depth) + 1