import linkedlist

class PriorityQueue:
    def __init__(self):
        self.items = linkedlist.LinkedList()
    
    def enqueue(self, item, priority):
        ''' Enqueues the item, a, on the queue, q; complexity O(1). '''
        cursor = self.items.front
        crsrnxt = cursor.next
        cursor.priority = priority
        
        idx = 0
        while cursor is not None:
            print(cursor.priority)
        
            if crsrnxt is None:
                self.items.insert(idx, item, priority)
                break
            elif cursor.priority >= crsrnxt.priority:
                print(crsrnxt.priority)
                print(idx)
                print(item)
                self.items.insert(idx, item, priority)
                break
            else:
                cursor = cursor.next
                crsrnxt = crsrnxt.next
                idx +=1
                
        return self
    def dequeue(self):
        ''' Returns the first item enqueued and removes
            it from queue; complexity O(1). ''' 
        if self.isEmpty():
            raise RuntimeError('Attempt to access front of empty queue') 
        
        item = self.items[0]
        del self.items[0]
        
        return item
    
    def isEmpty(self):
        ''' Returns True if q has not enqueued items; complexity O(1). '''
        if len(self.items) != 0:
            return False
        else:
            return True
        
    def front(self):
           # Returns the front item without dequeuing the
            #item; complexity O(1).
        if self.isEmpty():
            raise RuntimeError('Attempt to access front of empty queue')
        
        return self.items[0]
def main():
    q = PriorityQueue()
    items = list(range(10))
    items2 = []
    
    for k in items:
        q.enqueue(k)
        
    if q.front() == 0:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
        
    while not q.isEmpty():
        items2.append(q.dequeue())
    
    if items2 != items:
        print("Test 2 Failed")
    else:
        print("Test 2 Passed")

    for k in items:
        q.enqueue(k)   
      
    items2 = []
    
    while not q.isEmpty():
        items2.append(q.dequeue())  
        
    if items2 != items:
        print("Test 3 Failed")
    else:
        print("Test 3 Passed")
    
    try:
        q.dequeue()
        print("Test 4 Failed")
        
    except RuntimeError:
        print("Test 4 Passed")
    except:
        print("Test 4 Failed")

    try:
        q.front()
        print("Test 5 Failed")
        
    except RuntimeError:
        print("Test 5 Passed")
    except:
        print("Test 5 Failed")  
        
if __name__=="__main__":
    main()