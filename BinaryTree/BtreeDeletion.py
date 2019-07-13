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

def delete_node(root,key_node):
    q = []
    q.append(root)

    while len(q):
        tmp = q.pop(0)
        if tmp is key_node:
            tmp = None
            return

        if tmp.left:
            if tmp.left is key_node:
                tmp.left = None
                return
            else:
                q.append(tmp.left)

        if tmp.right:
            if tmp.right is key_node:
                tmp.right = None
                return
            else:
                q.append(tmp.right)


def deletion(root,key):
    q = []
    q.append(root)
    while len(q):
        tmp = q.pop(0)
        if tmp.data == key:
            keynode = tmp
        if tmp.left:
            q.append(tmp.left)

        if tmp.right:
            q.append(tmp.right)

    x = tmp.data
    delete_node(root,tmp)
    keynode.data = x

if __name__=='__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the deletion:")
    inorder(root)
    key = 11
    deletion(root, key)
    print()
    print("The tree after the deletion;")
    inorder(root)