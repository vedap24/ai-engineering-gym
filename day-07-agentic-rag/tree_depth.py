# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 1. Base case: Node lekapothe depth 0
        if root is None:
            return 0
            
        # 2. Left side lothu entho kanukkuntunnam
        left_depth = self.maxDepth(root.left)
        
        # 3. Right side lothu entho kanukkuntunnam
        right_depth = self.maxDepth(root.right)
        
        # 4. Renditlo pedda daaniki (max) + 1 add chestham
        return max(left_depth, right_depth) + 1

# Testing the code
# Creating a tree: 
#       3
#      / \
#     9  20
#       /  \
#      15   7
node15 = TreeNode(15)
node7 = TreeNode(7)
node20 = TreeNode(20, node15, node7)
node9 = TreeNode(9)
root = TreeNode(3, node9, node20)

solution = Solution()
print(f"🌲 The maximum depth of the tree is: {solution.maxDepth(root)}") # Returns 3