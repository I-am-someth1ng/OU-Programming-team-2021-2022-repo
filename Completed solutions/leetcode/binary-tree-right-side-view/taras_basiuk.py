"""
    Solution to the https://leetcode.com/problems/binary-tree-right-side-view/

    Approach to the solution is a breadth first (level-wise) traversal of the tree
    favoring traversing to the rightmost node first at every level.
    Once a traversal to the new level is detected, that node is added to the result.
"""

__author__ = "Taras Basiuk"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # Handle special case of empty tree
        if not root:
            return []

        result = [] # Result container

        # Queue holding the traversal progress, initialy containg the root node
        traversal_queue = [(root, 0)]
        i, cur_level = 0, -1 # Queue progress index, and tree level seen so far
        while i < len(traversal_queue): # While there's still work in the queue

            # Retrieve the currently examined node from the queue
            node, level = traversal_queue[i]

            # If encountered new tree level
            if level > cur_level:
                result.append(node.val) # Add this node to the result
                cur_level = level # Update the current traversal level

            if node.right: # If the right child exists
                # Add it to the end of the queue for future traversal
                traversal_queue.append((node.right, level + 1))

            if node.left: # If the left child exists
                # Add it to the end of the queue for future traversal
                traversal_queue.append((node.left, level + 1))

            i += 1 # We can traverse to the next node in the queue now

        return result
