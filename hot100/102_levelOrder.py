# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        deque1 = deque()
        deque2 = deque()
        deque1.append(root)
        while deque1 or deque2:
            nodes = []
            if deque1:
                while deque1:
                    node = deque1.popleft()
                    nodes.append(node.val)
                    deque2.append(node.left) if node.left else None
                    deque2.append(node.right) if node.right else None
            elif deque2:
                while deque2:
                    node = deque2.popleft()
                    nodes.append(node.val) 
                    deque1.append(node.left) if node.left else None
                    deque1.append(node.right) if node.right else None

            res.append(nodes)
        
        return res
    
if __name__ == "__main__":
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    s = Solution()
    result = s.levelOrder(root)
    print(result)  # Output: [[1], [2, 3], [4, 5, 6, 7]]


