class  Node(object):
    """docstring for  Node."""
    def __init__(self, data):
        super( Node, self).__init__()
        self.data = data
        self.left = None
        self.right = None


class  BST(object):
    """docstring for  BST."""
    def __init__(self):
        super( BST, self).__init__()
        self.root = None


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertNode(self.root, data)

    def insertNode(self, currentNode, data):
        if(data <= currentNode.data):
            if currentNode.left is None:
                currentNode.left = Node(data)
            else:
                self.insertNode(currentNode.left, data)
        else:
            if currentNode.right is None:
                currentNode.right = Node(data)
            else:
                self.insertNode(currentNode.right, data)

    def inorder(self):
        if(self.root):
            self.inorderPrint(self.root)

    def inorderPrint(self, root):
        temp = root
        if(temp):
            self.inorderPrint(temp.left)
            print(temp.data)
            self.inorderPrint(temp.right)




bs = BST()
bs.insert(50)
bs.insert(30)
bs.insert(20)
bs.insert(40)
bs.insert(70)
bs.insert(60)
bs.insert(80)
bs.inorder()
