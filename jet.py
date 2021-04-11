class AvlTreeNode:
    def __init__(self, key, val=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.val = val
        self.height = 1
        self.diff = 0


class AvlTree:
    def __init__(self):
        self.root = None

    def get_height(self):
        return self._get_height(self.root)

    def _get_height(self, root):
        if not root:
            return 0
        return 1 + max(self._get_height(root.left), self._get_height(root.right))

    def rotate_left(self, root):
        if not root:
            return

        right_son = root.right
        right_left_grandson = right_son.left

        right_son.left = root
        right_son.parent = root.parent
        root.parent = right_son
        root.right = right_left_grandson

        if right_left_grandson:
            right_left_grandson.parent = root

        if right_son.parent:
            if right_son.parent.left == root:
                right_son.parent.left = right_son
            else:
                right_son.parent.right = right_son

        root.height = self._get_height(root)
        root.diff = self._get_height(root.left) - self._get_height(root.right)
        right_son.height = self._get_height(right_son)
        right_son.diff = self._get_height(
            right_son.left) - self._get_height(right_son.right)

        return right_son

    def rotate_right(self, root):
        left_son = root.left
        left_right_grandson = left_son.right

        left_son.right = root
        left_son.parent = root.parent
        root.parent = left_son
        root.left = left_right_grandson

        if left_right_grandson:
            left_right_grandson.parent = root

        if left_son.parent:
            if left_son.parent.left == root:
                left_son.parent.left = left_son
            else:
                left_son.parent.right = left_son

        root.height = self._get_height(root)
        root.diff = self._get_height(root.left) - self._get_height(root.right)
        left_son.height = self._get_height(left_son)
        left_son.diff = self._get_height(
            left_son.left) - self._get_height(left_son.right)

        return left_son

    def insert(self, key, val=None):
        self.root = self._insert(self.root, key, val)

    def _insert(self, root, key, val=None):
        if not root:
            return AvlTreeNode(key, val)
        elif key < root.key:
            new_left_son = self._insert(root.left, key, val)
            root.left = new_left_son
            new_left_son.parent = root
        elif key > root.key:
            new_right_son = self._insert(root.right, key, val)
            root.right = new_right_son
            new_right_son.parent = root
        else:
            return root

        root.height = self._get_height(root)
        root.diff = self._get_height(root.left) - self._get_height(root.right)
        root = self.balance(root)

        return root

    def get_elem(self, root, key):
        if not root:
            return None
        elif root.key == key:
            return root.val
        elif root.key > key:
            return self.get_elem(root.left, key)
        else:
            return self.get_elem(root.right, key)

    def contains(self, key):
        return self._contains(self.root, key)

    def _contains(self, root, key):
        if not root:
            return False
        elif root.key == key:
            return True
        elif root.key > key:
            return self._contains(root.left, key)
        else:
            return self._contains(root.right, key)

    def get_min(self, root):
        if not root:
            return None
        elif root.left:
            return self.get_min(root.left)
        return root

    def balance(self, root):
        if root.diff == 2:
            if root.left.diff < 0:
                root.left = self.rotate_left(root.left)
                root = self.rotate_right(root)
            else:
                root = self.rotate_right(root)
        elif root.diff == -2:
            if root.right.diff > 0:
                root.right = self.rotate_right(root.right)
                root = self.rotate_left(root)
            else:
                root = self.rotate_left(root)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return None

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.right:
                left = root.left
                if left:
                    left.parent = root.parent
                root = None
                return left
            elif not root.left:
                right = root.right
                if right:
                    right.parent = root.parent
                root = None
                return right
            else:
                next_key = self.get_min(root.right)
                root.key = next_key.key
                root.val = next_key.val
                root.right = self._delete(root.right, next_key.key)

        if not root:
            return None
        root.height = self._get_height(root)
        root.diff = self._get_height(
            root.left) - self._get_height(root.right)

        root = self.balance(root)

        return root

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, root):
        if not root:
            return

        self._print_tree(root.left)
        print("key =", root.key, "val =", root.val, "height =", root.height)
        self._print_tree(root.right)