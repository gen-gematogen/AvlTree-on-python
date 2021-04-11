import jet

def pretty_print_tree(root):
    """
    This function pretty prints a binary tree
    :param root: root of tree
    :return: none
    """
    lines, _, _, _ = _pretty_print_tree(root)
    for line in lines:
        print(line)


def _pretty_print_tree(root):
    """
    Code credits: Stack overflow
    :param root: root of tree
    :return: none
    """
    if root.right is None and root.left is None:
        line = '%s' % root.key
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if root.right is None:
        lines, n, p, x = _pretty_print_tree(root.left)
        s = '%s' % root.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if root.left is None:
        lines, n, p, x = _pretty_print_tree(root.right)
        s = '%s' % root.key
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _pretty_print_tree(root.left)
    right, m, q, y = _pretty_print_tree(root.right)
    s = '%s' % root.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

tree = jet.AvlTree()

tree.insert(1, 1)
tree.insert(5, 1)
tree.insert(10, 1) #left rotation
pretty_print_tree(tree.root)
print()
tree.insert(9, 1)
tree.insert(8, 1) #right-left rotation
pretty_print_tree(tree.root)
print()

if tree.contains(8):
    tree.delete(8)
if tree.contains(10):
    tree.delete(10)
if tree.contains(17): #doesn't contain
    tree.delete(17)
pretty_print_tree(tree.root) 
print()

tree.insert(-1, 1)
tree.insert(-2, 1) #right rotation
pretty_print_tree(tree.root)
print()

tree.insert(2, 1) #left-right rotation
pretty_print_tree(tree.root)
print()

if tree.contains(-2):
    tree.delete(-2)
if tree.contains(-1):
    tree.delete(-1) #left rotation
pretty_print_tree(tree.root)
print()