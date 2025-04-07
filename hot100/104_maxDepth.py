class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def maxleftorright(self,node:TreeNode)->int:
        if node is None:
            return 0
        h_l = 1
        h_r = 1
        # 递归计算左右子树的高度
        if node.left is not None:
            h_l = self.maxleftorright(node.left)+1
        if node.right is not None:
            h_r = self.maxleftorright(node.right)+1
        return max(h_l,h_r)



    def maxDepth(self, root: TreeNode) -> int:
        result = self.maxleftorright(root)

        return result

if __name__ == "__main__":
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    s = Solution()
    result = s.maxDepth(root)
    print(result)  # Output: 3