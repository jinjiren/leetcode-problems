# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        while(root):
            if (p.val - root.val) * (q.val - root.val) <= 0:
                return root
            else:
                root = root.left if p.val - root.val < 0 else root.right
        return None
