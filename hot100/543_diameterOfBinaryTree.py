# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def maxPathofTree(self,node:TreeNode):
        pl = 0
        pr = 0

        if node.left is not None:
            pl = self.maxPathofTree(node.left)
        if node.right is not None:
            pr = self.maxPathofTree(node.right) 

        self.currentmax = max(self.currentmax,pl+pr)

        print("node.val:",node.val," pl:",pl," pr:",pr," currentmax:",self.currentmax)
        return max(pl,pr)+1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.currentmax = 0
        self.maxPathofTree(root)
        return self.currentmax 

if __name__ == "__main__":
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)


    s = Solution()
    result = s.diameterOfBinaryTree(root)
    print(result)  # Output: 3 (the longest path is 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)
