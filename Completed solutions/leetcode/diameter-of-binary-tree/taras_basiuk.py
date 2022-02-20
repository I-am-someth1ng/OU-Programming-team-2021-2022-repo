"""
    Solution to the - https://leetcode.com/problems/diameter-of-binary-tree/submissions/

    Approach to the solution is a common graph diameter finding trick:
    1. Find a node most distant from any node (we'll start with the root node).
    2. Fina a node most distand from the node found in (1).
    3. Nodes found in (1) and (2) form the diameter of the graph.
"""

__author__ = "Basiuk Taras"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        """
            First we will find the node for (1) above.
            But while we do that, we will also recode the parent links to all the nodes
            we will visit. We will need those links whan we look for the node from (2).
            We don't need them now, as the node most distant from the root is one of the leafs
            and we don't need parent links to find that leaf.
        """
        root.parent = None # Root node has no parent
        furthest_node, furthest_dist = None, -1 # Init. furthest node and distance trackers

        # Init. working queue with just root node and its 0 distance
        queue = [(root, 0)]
        i = 0 # Index for working queue traversal

        while i < len(queue): # While there's work to be done in the queue

            node, dist = queue[i] # Retieve the current node and its distance from the queue

            # If the distance is larger than what we've seen before
            if dist > furthest_dist:
                furthest_node = node # Update the furthest node
                furthest_dist = dist # ... and furthest distance

            if node.left: # If our node has left child
                node.left.parent = node # Record this node as left child node parent
                queue.append((node.left, dist + 1)) # Add left child to the working queue

            if node.right: # If our node has right child
                node.right.parent = node # Record this node as right child node parent
                queue.append((node.right, dist + 1)) # Add left right to the working queue

            i += 1 # Move to working on the next node   

        """
            Now, to find the (2) furthest node, we will need to trach the nodes we visited,
            Otherwise our search can go backwards.
        """
        visited = set()
        visited.add(furthest_node) # Add the node from (1) as visited

        furthest_dist = -1 # reset the furthest distance tracker

        queue = [(furthest_node, 0)] # Re-initialize the working queue with the node from (1)
        i = 0 # Index for working queue traversal

        while i < len(queue): # While there's work to be done in the queue

            node, dist = queue[i] # Retieve the current node and its distance from the queue

            # If the distance is larger than what we've seen before
            if dist > furthest_dist:
                furthest_node = node.parent # Update the furthest node
                furthest_dist = dist # ... and furthest distance

            # If the current node has an unvisited parent
            if node.parent and node.parent not in visited:
                visited.add(node.parent) # Add the parent to the visited nodes
                queue.append((node.parent, dist + 1)) # Add the parent to the working queue

            # If the current node has an unvisited left child
            if node.left and node.left not in visited:
                visited.add(node.left) # Add the left child to the visited nodes
                queue.append((node.left, dist + 1)) # Add the left child to the working queue

            # If the current node has an unvisited right child
            if node.right and node.right not in visited:
                visited.add(node.right) # Add the right child to the visited nodes
                queue.append((node.right, dist + 1)) # Add the right child to the queue

            i += 1 # Move to working on the next node

        return furthest_dist # The furthest distance we found in the second loop is our result
