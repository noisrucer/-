class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q: 
            return p == q
        
        if p.val != q.val: 
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)