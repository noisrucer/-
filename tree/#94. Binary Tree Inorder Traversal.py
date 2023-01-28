'''
[STEP 1] 일반화
이진 트리에서 root가 주어지면, inorder 방식으로 node values를 반환하라

[STEP 2] 점화식
f(root) = inorder traversal로 nodes values 반환

- Base Case
f(None) = []

- General Case
root.left 로 이동해서 node values를 가져와라
root.right 로 이동해서 node values를 가져와라

f(root) = root.left
list.append(root.val)
f(root) = root.right

'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.inorder(root)
        return self.res

    def inorder(self, root):
        if root is None:
            return []
        
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)
