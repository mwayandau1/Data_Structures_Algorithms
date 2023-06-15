class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def createNode(self, data):
        return Node(data)
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node
    def traverse_InOrder(self, data):
        if data:
            self.traverse_InOrder(data.left)
            print(data.data)
            self.traverse_InOrder(data.right)

if __name__ == "__main__":
    tree = Tree()
    rt = tree.createNode(2)
   # print(rt.data)
    tree.insert(rt, 6)
    tree.insert(rt, 45)
    tree.insert(rt, 10)
    tree.insert(rt, 5)
    tree.insert(rt, 20)
    tree.traverse_InOrder(rt)




