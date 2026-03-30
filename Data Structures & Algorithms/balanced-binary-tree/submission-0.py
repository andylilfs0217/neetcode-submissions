# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        visited = {None: 0}
        stack = [root]

        while stack:
            node = stack[-1]

            if node.left and node.left not in visited:
                stack.append(node.left)
            elif node.right and node.right not in visited:
                stack.append(node.right)
            else:
                left = visited[node.left]
                right = visited[node.right]
                diff = abs(left-right)
                if diff > 1:
                    return False
                node = stack.pop()
                depth = 1 + max(left, right)
                visited[node] = depth
        
        # node = stack.pop()
        diff = abs(visited[root.left]-visited[root.right])
        if diff > 1:
            return False

        return True
        
