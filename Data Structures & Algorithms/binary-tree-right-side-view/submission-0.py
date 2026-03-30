# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        ans = []
        while queue:
            new_queue = []
            right_most_ele = None

            for node in queue:
                if node:
                    new_queue.append(node.left)
                    new_queue.append(node.right)
                    right_most_ele = node.val

            queue = new_queue
            if right_most_ele:
                ans.append(right_most_ele)

        return ans