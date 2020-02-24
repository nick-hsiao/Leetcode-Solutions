def isSymmetric(self, root: TreeNode) -> bool:
        def compare(l,r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            
            if l.val != r.val:
                return False
            
            return compare(l.left,r.right) and compare(l.right,r.left)
        
        
        return compare(root.left, root.right) if root else True