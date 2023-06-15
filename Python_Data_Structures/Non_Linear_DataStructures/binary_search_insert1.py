class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
            
            
    def _insert(self, data, curr_node):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(data, curr_node.left)
        elif data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(data, curr_node.right)
                
        else:
            print("Value already exist!!!")  
            
            
    def search_node(self, data):
        if self.root:
            is_found = self._search_node(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None
        
    def _search_node(self, data, curr_node):
        if data < curr_node.data and curr_node.left:
            self._search_node(data, curr_node.left)
        elif data > curr_node.data and curr_node.right:
            self._search_node(data, curr_node.right)
        if data == curr_node.data:
            return True
            
                              
            
            
if __name__ == '__main__':
    bin = BST()
    bin.insert(50)
    bin.insert(2)
    bin.insert(40)
    bin.insert(12)
    
    
    print(bin.search_node(40))
    print(bin.search_node(2))
    print(bin.search_node(50))