
#AVLTree with research and delete function
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def size(self, node):
        if node is None:
            return 0
        return node.size

    def difference(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        node.size = 1 + self.size(node.left) + self.size(node.right)

    def changeLeft(self, root):
        r = root.right
        rl = r.left

        r.left = root
        root.right = rl

        self.update(root)
        self.update(r)

        return r

    def changeRight(self, root):
        l = root.left
        lr = l.right

        l.right = root
        root.left = lr

        self.update(root)
        self.update(l)

        return l

    def insert(self, root, val):
        if root is None:
            return AVLNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        self.update(root)

        difference = self.difference(root)

        if difference > 1:
            if val < root.left.val:
                return self.changeRight(root)
            else:
                root.left = self.changeLeft(root.left)
                return self.changeRight(root)
        elif difference < -1:
            if val > root.right.val:
                return self.changeLeft(root)
            else:
                root.right = self.changeRight(root.right)
                return self.changeLeft(root)

        return root

    def delete(self, root, val):
        if root is None:
            return root
        elif val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        if root is None:
            return root

        self.update(root)

        difference = self.difference(root)

        if difference > 1:
            if self.difference(root.left) >= 0:
                return self.changeRight(root)
            else:
                root.left = self.changeLeft(root.left)
                return self.changeRight(root)
        elif difference < -1:
            if self.difference(root.right) <= 0:
                return self.changeLeft(root)
            else:
                root.right = self.changeRight(root.right)
                return self.changeLeft(root)

        return root

    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def find(self, root, k):
        while root:
            right_count = self.size(root.right)
            if k == right_count + 1:
                return root.val
            elif k <= right_count:
                root = root.right
            else:
                k -= right_count + 1
                root = root.left
        return None
tree = AVLTree()
root = None

n = int(input())

for i in range(n):
    s = input().split()
    if s[0] == '+1' or s[0] == '1':
        root = tree.insert(root, int(s[1]))
    elif s[0] == '0':
        print(tree.find(root, int(s[1])))
    elif s[0] == '-1':
        root = tree.delete(root, int(s[1]))