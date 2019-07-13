class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def insert(tmp, val):
    q = list()
    q.append(tmp)

    while len(q):
        tmp = q[0]
        q.pop(0)

        if not tmp.left:
            tmp.left = Node(val)
            break
        else:
            q.append(tmp.left)

        if not tmp.right:
            tmp.right = Node(val)
            break
        else:
            q.append(tmp.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    insert(root, 4)
    inorder(root)
