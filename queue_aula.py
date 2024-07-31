from typing import Any

class Node:
    def __init__(self,data: Any):
        self.data = data
        self.next = None
    

    def __repr__(self) -> str:
        return self.data





class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0
    
    def push(self,data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1
    
    def pop(self):
        if self.top is not None:
            self.top = self.top.next
            self.size -= 1
        return None
    
    def __sizeof__(self):
        return self.size

    def __repr__(self):
        ptr = self.top
        res = []
        while ptr is not None:
            res.append(ptr.data)
            ptr = ptr.next
        return str(res)
    
    def __iter__(self):
        self.ptr = self.top
        return self


class Queue:
    def __init__(self) -> None:
        self.ini = None
        self.fim = None
    

    def consultar(self):
        if not self.is_empty():
            return self.ini.data

    def is_empty(self):
        if self.ini is None and self.fim is None:
            return True
        return False
    
    def insert(self,data):
        node = Node(data)
        if self.is_empty():
            self.ini = node
            self.fim = node
        else:
            self.fim.next = node
        self.fim = node

    def pop(self):
        if self.is_empty():
            return False
        self.ini = self.ini.next
        if self.ini is None:
            self.fim = None
        return True
    
    def __repr__(self) -> str:
        ptr = self.ini
        res = []
        while ptr is not None:
            res.append(ptr.data)
            ptr = ptr.next
        
        res = [str(x) for x in res]
        return str(",".join(res))

class Stack:
    def __init__(self) -> None:
        self.top = None
    
    def push(self,data):
        node = Node(data)
        if not self.is_empty():
            node.next = self.top
        self.top = node
    
    def pop(self):
        if not self.is_empty():
            self.top = self.top.next
        return None

    def get(self):
        if not self.is_empty():
            return self.top.data
        return None

    def is_empty(self):
        return self.top is None


    



def order_queue(queue: Queue) -> Queue:
    stack1 = Stack()
    stack2 = Stack()

    while not queue.is_empty():
        if stack1.is_empty():
            stack1.push(queue.consultar())
            queue.pop()
            continue
        



        while stack1.get() <= queue.consultar():
            stack2.push(stack1.get())
            stack1.pop()
            if stack1.get() is not None:
                continue
            else:
                break
        


        
        stack1.push(queue.consultar())

        while not stack2.is_empty():
            stack1.push(stack2.get())
            stack2.pop()

        queue.pop()




    qaux = Queue()
    while not stack1.is_empty():
        qaux.insert(stack1.get())
        stack1.pop()
    
    return qaux





 

def tests():
    t1 = [55,25,33,10,1,400,500,200,300,11]
    t2 = [20,14,12,0,25,30,66,5,500,5000000000]
    t3 = [1,2,3,4,5,0]
    t4 = [45,22,11,22,3689,22,45111,2,1]

    t = [t1,t2,t3,t4]

    for lista in t:
        q = Queue()
        for i in lista:
            q.insert(i)
        
        order = order_queue(q)
        print(f"Fila original: {q}")
        print("=========")
        print(f"Fila ordenada {order}")
            


if __name__ == "__main__":
    tests()
