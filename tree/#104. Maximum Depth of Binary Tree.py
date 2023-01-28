''''
1. 일반화
이진 트리의 root가 주어지면 그것의 최대 깊이를 구하라

2. 점화식
f(root) = root로 부터의 maximum depth

- base case


root.left 보고 너의 maximum depth를 구해와라
root.right 보고 너의 maximum depth를 구해와라

- General Case
f(root) = max(f(root.left), f(root.right)) + 1
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1