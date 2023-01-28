class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height = True
        self.maximumDepth(root)
        return self.height
    
    def maximumDepth(self, root):

        if root is None:
            return True

        left_maximum = self.maximumDepth(root.left)
        right_maximum = self.maximumDepth(root.right)

        if abs(left_maximum - right_maximum) > 1:
            self.height = False
        
        return max(left_maximum, right_maximum) + 1