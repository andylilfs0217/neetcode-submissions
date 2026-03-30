# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        ans = []
        while queue:
            new_queue = []
            ans_ele = []
            for node in queue:
                if node:
                    ans_ele.append(node.val)
                    new_queue.append(node.left)
                    new_queue.append(node.right)
            
            queue = new_queue
            if len(ans_ele) > 0:
                ans.append(ans_ele)
        return ans

