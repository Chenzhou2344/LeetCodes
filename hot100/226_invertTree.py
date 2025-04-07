# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invert(self, node: TreeNode) -> TreeNode:
        if node is None:
            return []
        self.invertTree(node.left)
        self.invertTree(node.right)

        tmpnode = node.left
        node.left = node.right
        node.right = tmpnode

        return node

    def invertTree(self, root: TreeNode) -> TreeNode:
        
        root = self.invert(root)
        return root
    
if __name__ == "__main__":
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    s = Solution()
    result = s.invertTree(root)
    print(result.val)  # Output: 1




        