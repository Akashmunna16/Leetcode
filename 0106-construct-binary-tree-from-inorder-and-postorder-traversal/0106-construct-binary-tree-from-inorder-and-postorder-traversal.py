# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}
        post_idx = len(postorder) - 1
        
        def array_to_tree(left_in, right_in):
            nonlocal post_idx
            if left_in > right_in:
                return None
                
            root_val = postorder[post_idx]
            root = TreeNode(root_val)
            post_idx -= 1
            
            mid = inorder_idx_map[root_val]
            
            # CRITICAL: Build right branch first when working backwards from postorder
            root.right = array_to_tree(mid + 1, right_in)
            root.left = array_to_tree(left_in, mid - 1)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)