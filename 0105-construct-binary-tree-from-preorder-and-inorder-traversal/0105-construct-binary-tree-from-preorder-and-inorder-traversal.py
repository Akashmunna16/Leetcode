# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hash map for O(1) lookups of root indices in the inorder list
        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0
        
        def array_to_tree(left_in, right_in):
            nonlocal pre_idx
            # Base Case: no elements left to construct this subtree branch
            if left_in > right_in:
                return None
                
            # Pick current root element from preorder tracking pointer
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            
            # Split the inorder tree segment into Left and Right regions
            mid = inorder_idx_map[root_val]
            
            root.left = array_to_tree(left_in, mid - 1)
            root.right = array_to_tree(mid + 1, right_in)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)
        