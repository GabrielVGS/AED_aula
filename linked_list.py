class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def __repr__(self):
        s = f""
        for node in self:
            s += f"{node} -> "
        
        s += "None"

        return s

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def insert_at_begin(self,node):
        node.next = self.head
        self.head = node
    
    def insert_at_end(self,node):
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
        current_node.next = node
    
    def size_of_LL(self):
        c = 0
        for i in self:
            c += 1
        return c

    def find(self,data):
        for idx,node in enumerate(self):
            if data  == node.data:
                return idx
        
        return "Not Found"
    
    def insert_at_index(self,node,idx):
        if idx == 0:
            return self.insert_at_begin(data)
        else:
            for i, current_node in enumerate(self):
                if (i + 1 == idx):
                    current_node.next.next = current_node.next
                    current_node.next = node

                    return None
            return "idx out of range"

        
    def remove_at_idx(self,idx):
        for i, node in enumerate(self):
            if i + 1 == idx:
                node.next = node.next.next
                return None
        
        return False

    
    def __getitem__(self,idx):
        for i, node in enumerate(self):
            if i == idx:
                return node.data
        
        return "Idx out of range"


llist = LinkedList()
first_node = Node("5")
llist.head = first_node
first_node.next = Node("4")
first_node.next.next = Node("3")
llist.insert_at_index(Node("2"),5)
llist.remove_at_idx(2)
print(llist)
