# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetrictree(self, node: TreeNode)-> bool:
        fl = False
        fr = False
        if node.left != None and node.right != None:
            leftnode = node.left
            rightnode = node.right
            print(leftnode.left == rightnode.right)
            if leftnode.left == rightnode.right and leftnode.right == rightnode.left :
                fl = self.isSymmetrictree(node.left)
                fr = self.isSymmetrictree(node.right)
                print(fl,fr)
        if fl == False or fr == False:
            return False
        else:
            return True
        
    def isSymmetric(self, root: TreeNode) -> bool:
        res = self.isSymmetrictree(root)
        return res
    
if __name__ == "__main__":
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    s = Solution()
    result = s.isSymmetric(root)
    print(result)  # Output: True