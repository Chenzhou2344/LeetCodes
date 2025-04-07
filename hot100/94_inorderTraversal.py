# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归写法
# class Solution:
#     def inorder(self, node: TreeNode,nodels:list):
#         if node is None:
#             return nodels
#         self.inorder(node.left,nodels)
#         nodels.append(node)
#         self.inorder(node.right,nodels)

#         return nodels
        
#     def inorderTraversal(self, root:TreeNode) -> list[int]:
#         nls = []
#         nls = self.inorder(root,nls)
#         return nls

# 迭代写法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[TreeNode]:
        stack = []
        current = root
        result = []

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current)
            current = current.right

        return result

if __name__ == "__main__":
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    s = Solution()
    result = s.inorderTraversal(root)
    print([node.val for node in result])  # Output: [4, 2, 5, 1, 3]