from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Tree empty ayithe, emi ledu ani return chestham
        if not root:
            return []
            
        result = []
        # 1. Manam matladukunna Queue ni initialize chesthunnam
        queue = deque([root])
        
        # Queue lo items unnantha varaku loop run avtundi
        while queue:
            # Ee level lo enni items unnayo count chestham
            level_size = len(queue)
            current_level = []
            
            # Aa level lo unna anni nodes ni process chestham
            for _ in range(level_size):
                # First in, First out (FIFO) - queue mundu nunchi teestham
                node = queue.popleft()
                current_level.append(node.val)
                
                # Aa node ki left/right pillalu unte, vellani queue chivara add chestham
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # Oka level complete ayyaka, daanni main result ki add chestham
            result.append(current_level)
            
        return result

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
print(f"🌳 Level by Level Traversal: {solution.levelOrder(root)}") 
# Returns: [[3], [9, 20], [15, 7]]