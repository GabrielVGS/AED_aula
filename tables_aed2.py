class Table:
    def __init__(self,size) -> None:
        self.size = size
        self.keys = [None] * size
        self.values =  [None] * size
        self.ini = 0
        self.end = None

    
    def __getitem__(self,key):
        for key_table,value in self:
            if key_table == key:
                return value
            
        return None
    
    def index(self,key):
        c = self.ini
        for key_table, value_table in self:
            if key_table == key:
                return c
            c += 1
    
    def __iter__(self):
        ini_aux = self.ini
        while ini_aux != self.end + 1:
            yield self.keys[ini_aux],self.values[ini_aux]
            ini_aux+=1
    
    def __repr__(self):
        s = ""

        for key,value in zip(self.keys,self.values):
            s += f"{key} -> {value} \n"
        
        return s

    
    def insert(self,key,value):
        if self.end is None:
            self.end = self.ini
            self.keys[self.end] = key
            self.values[self.end] = value
        else:
            if self[key] is not None:
                idx = self.index(key)
                self.keys[idx] = key
                self.values[idx] = value
            else:
                self.end +=1 
                self.keys[self.end] = key
                self.values[self.end] = value


    def insert_ord(self,key,value):
        if self.end is None:
            self.end = self.ini
            self.keys[self.end] = key
            self.values[self.end] = value
        else:
            if self[key] is not None:
                idx = self.index(key)
                self.keys[idx] = key
                self.values[idx] = value
            else:
                for key_table, value_table in self:
                    if key_table > key:
                        end_aux = self.end + 1
                        idx_key_table = self.index(key_table)
                        while idx_key_table != end_aux + 1:

                            self.keys[end_aux] = self.keys[end_aux - 1]
                            self.values[end_aux] = self.values[end_aux- 1]
                            end_aux -=1
                        
                        self.keys[idx_key_table] = key
                        self.values[idx_key_table] = value
                        self.end += 1
                        break
        
    
    def binary_search(self,key):
        l,r = 0, self.end
        m = (l+r)//2
        while key != self.keys[m]:
        
            if l > r:
                return None
            m = (l+r)//2
            if self.keys[m] < key:
                l = m + 1
    
            if self.keys[m] > key:
                r = m - 1
    
    
        return m
    





table = Table(10)
table.insert(77,"555")
table.insert_ord(5,"valor1")
table.insert_ord(1,"valor2")
table.insert_ord(2,"valor")
table.insert_ord(3,"valorteste")
print(table)
print(table.binary_search(5))
