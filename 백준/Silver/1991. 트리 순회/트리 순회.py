class Vertex:
    def __init__(self, name, left, right):
        self.name = name
        if left != '.':
            self.left = left
        else:
            self.left = None
        if right != '.':
            self.right = right
        else:
            self.right = None


def pre_order(vertex):
    print(vertex.name, end='')
    if vertex.left is not None:
        pre_order(tree[vertex.left])
    if vertex.right is not None:
        pre_order(tree[vertex.right])


def in_order(vertex):
    if vertex.left is not None:
        in_order(tree[vertex.left])
    print(vertex.name, end='')
    if vertex.right is not None:
        in_order(tree[vertex.right])


def post_order(vertex):
    if vertex.left is not None:
        post_order(tree[vertex.left])
    if vertex.right is not None:
        post_order(tree[vertex.right])
    print(vertex.name, end='')


V = int(input())
tree = dict()
for _ in range(V):
    name, left, right = input().split()
    v = Vertex(name, left, right)
    tree[name] = v
    if name == 'A':
        root = v

pre_order(root)
print()
in_order(root)
print()
post_order(root)
