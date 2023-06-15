class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
        
class Sorted_Doubly:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            
            
        elif data < self.head.value:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
           
            self.head = new_node
            
        elif data > self.tail.value:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
        else:
            new_node = Node(data)
            cur = self.head
            while self.head is not None and cur.value < data:
               cur = cur.next
               
            new_node.next = cur
            new_node.prev = cur.prev
            cur.prev.next = new_node
            cur.prev = new_node
  
  
    def print_List(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next              
            
if __name__ == "__main__":
    dll = Sorted_Doubly()
    dll.append(3)
    dll.append(1)
    dll.append(4)
    dll.append(-1)
    dll.append(6)
    dll.append(6 )
    dll.append(7)

    dll.print_List()