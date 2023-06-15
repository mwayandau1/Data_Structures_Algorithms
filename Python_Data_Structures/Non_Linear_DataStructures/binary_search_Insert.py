class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return 
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
                
                
                
    def inOrderTraversal(self):
        element = []
        if self.left:
            element += self.left.inOrderTraversal()
        element.append(self.data)
        if self.right:
          element +=  self.right.inOrderTraversal()
            
        return element
    
    def searchNum(self, val):
        if self.data == val:
            return True 
        if val <self.data:
            if self.left:
                return self.left.searchNum(val)
            else:
                return False
        if val > self.data:
            if self.right:                
                return self.right.searchNum(val)
            else:
                return False
            
            
            
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
           
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()   
    
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val) 
        elif val > self.data:
            if self.right:
               self.right = self.right.delete(val)   
            
        else:
            if self.left is None and self.right is None:
                return None
            if self.right is None:
                return self.left
            if self.right is None:
                return self.left
            max_val = self.left.find_max()
            #min_val = self.right.find_min()
            self.data = max_val
            #self.data = min_val
             
            self.left = self.left.delete(max_val)   
            #self.right = self.right.delete(min_val)
        return self
                
                
if __name__ == '__main__':
   
    list1 = [12, 1, 55, 7, 20, 90, 40, 30, 3, 30,20,3,8]
    bin = BinarySearchTreeNode(list1[0])
    for i in range(1, len(list1)):
       bin.add_child(list1[i]) 
       
       
    tree = bin.inOrderTraversal()
    print(tree)
    
    print(bin.searchNum(90))
    print(bin.find_max())
    print(bin.find_min())
    bin.delete(90)
    print(bin.inOrderTraversal())
    