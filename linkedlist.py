class LinkedList:
    
    # This class is used internally by the LinkedList class. It is 
    # invisible from outside this class due to the two underscores
    # that precede the class name. Python mangles names so that they
    # are not recognizable outside the class when two underscores
    # precede a name but aren't followed by two underscores at the
    # end of the name (i.e. an operator name). 
    class __Node:
        def __init__(self,item,next=None, priority = -1000000):
            self.item = item
            self.next = next
            self.priority = priority
            
        def getPriority(self):
            return self.priority
            
        def getItem(self):
            return self.item
        
        def getNext(self):
            return self.next
        
        def setItem(self, item):
            self.item = item
            
        def setNext(self,next):
            self.next = next
            
    def __init__(self,contents=[]):
        # Here we keep a reference to the first node in the linked list
        # and the last item in the linked list. The both point to a 
        # dummy node to begin with. This dummy node will always be in
        # the first position in the list and will never contain an item. 
        # Its purpose is to eliminate special cases in the code below. 
        self.front = LinkedList.__Node(None,None)
        self.last = self.front
        self.numItems = 0

        for e in contents:
            self.append(e)
          
    def __getitem__(self,index):
        if index < self.numItems:
            cursor = self.front.getNext()
            for i in range(index):
                cursor = cursor.getNext()
                
            return cursor.getItem()
        
        raise IndexError("LInkedList index out of range")
    
    def __setitem__(self,index,val):
        if index < self.numItems:
            cursor = self.front.getNext()
            for i in range(index):
                cursor = cursor.getNext()
                
            cursor.setItem(val)
        
        raise IndexError("LinkedList assignment index out of range")
    
    def insert(self,index,item,priority):
        cursor = self.front
        
        if index < self.numItems: 
            for i in range(index):
                cursor = cursor.getNext()
                
            node = LinkedList.__Node(item, cursor.getNext(), priority)
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)
            
            
    def __add__(self,other):
        result = LinkedList()
        
        cursor = self.front.getNext()
        
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
            
        cursor = other.front.getNext()
                    
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
   
        return result
    
    
    def __contains__(self,item):
        
        cursor = self.front.getNext()
        
        while cursor != None:
            if cursor.getItem() == item:
                return True
            cursor = cursor.getNext()
            
            
        return False
    
    def __delitem__(self,index):
        cursor = self.front
        i = 0
        
        while cursor.getNext() != None:
            if i == index:
                cursor.setNext(cursor.getNext().getNext())
                self.numItems -= 1
                if cursor.getNext() == None:
                    self.last = cursor

                return 
            else:
                cursor = cursor.getNext()
                i+=1
                

            
    def __eq__(self,other):
        if type(other) != type(self):
            return False
        
        if self.numItems != other.numItems:
            return False
        
        cursor1 = self.front.getNext()
        cursor2 = other.front.getNext()
        while cursor1 != None:
            if cursor1.getItem() != cursor2.getItem():
                return False
            cursor1 = cursor1.getNext()
            cursor2 = cursor2.getNext()
            
        return True
    
    def __iter__(self):
        cursor = self.front.getNext()
        
        while cursor != None:
            yield cursor.getItem()
            cursor = cursor.getNext()

            
    def __len__(self):
        return self.numItems
         

    def append(self,item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1

        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        s = "LinkedList(["
        i = 0
        for item in self:
            s = s + repr(item)
            if i < self.numItems - 1:
                s = s + ", "
            i+=1
        s = s + "])"
        return s        
        
                
def main():
    lst = LinkedList()
    
    for i in range(100):
        lst.append(i)
    
    lst2 = LinkedList(lst)
    
    print(lst)
    print(lst2)
    
    if lst == lst2:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
    
    lst3 = lst + lst2
    
    if len(lst3) == len(lst) + len(lst2):
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")
        
    
    if 1 in lst3:
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")        
    
    if 2 in lst3:
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")        
    
    del lst[1]
    
    if 1 in lst:
        print("Test 5 Failed")
    else:
        print("Test 5 Passed")        
    
    if len(lst) == 99:
        print("Test 6 Passed")
    else:
        print("Test 6 Failed")        
        
    if lst == lst2:
        print("Test 7 Failed")
    else:
        print("Test 7 Passed")        
    
    del lst2[2]
    
    if lst == lst2:
        print("Test 8 Failed")
    else:
        print("Test 8 Passed")  
        
    
    lst4 = LinkedList(lst)
    lst.insert(0,100, 1)
    lst4 = LinkedList([100]) + lst4
    
    if lst == lst4:
        print("Test 9 Passed")
    else:
        print("Test 9 Failed")
        
    lst.insert(1000,333,1)
    lst4.append(333)

    if lst == lst4:
        print("Test 10 Passed")
    else:
        print("Test 10 Failed")  
        
    print(lst)
    print(lst4)
    
if __name__ == "__main__":
    main()
                
            
            
        
