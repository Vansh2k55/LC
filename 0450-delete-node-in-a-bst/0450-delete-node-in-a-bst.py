class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Case 1: no left child
            if root.left is None:
                return root.right

            # Case 2: no right child
            if root.right is None:
                return root.left

            # Case 3: two children
            temp = root.right

            while temp.left:
                temp = temp.left

            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        return root