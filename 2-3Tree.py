import string
#      write A
# A    /  |  \
#      write B
# B  /\   /\   /\
#   1  2 3  4  5 6
# input:
#4
#1 2 3 4
#output:
#1 B 2 A 3 B 4 A 5 B 6
class Node():
    def __init__(self, val, children=[None], height = 1, k = 1):
        self.height = height
        self.k = k
        self.val = []
        self.val.extend(val)
        self.children = children
    def add(self, val):
        self.val.append(val)
        self.val.sort()
        self.k += 1
        self.children.append(None)
class Tree:
    def insert(self, root, x):
        if not root:
            return Node([x])
        elif not root.children[0]:
            root.add(x)
        else:
            number = self.choose(root, x)
            tmp = self.insert(root.children[number], x)
            if tmp.height == root.height:
                root.val = root.val[:number] + tmp.val + root.val[number + 1:]
                root.children = root.children[:number] + tmp.children + root.children[number + 1:]
                root.k = len(root.val)
        return self.balance(root)
    def choose(self, root, x):
        for index, i in enumerate(root.val):
            if x < i:
                return index
        return root.k - 1

    def balance(self, root):
        if root.k == 4:
            return Node(root.val[1::2], [Node(root.val[0:2], root.children[0:2],height=root.height, k=2),
                                         Node(root.val[2:4], root.children[2:4], height=root.height, k=2)],height=root.height + 1, k=2)
        return root
    def print(self, root, answer=''):
        if root.children[0]:
            for i in root.children:
                answer += self.print(i)
                if i != root.children[-1]:
                    answer += f' {a[root.height - 1]} '
            return answer

        else:
            return f' {a[0]} '.join(map(str, root.val))
tree = Tree()
root = None

n = int(input())
k = list(map(int, input().split()))
for i in range(n):
        root = tree.insert(root, k[i])
a = string.ascii_uppercase[root.height - 1:: - 1]
answer = f''
answer = tree.print(root, answer)
print(answer)