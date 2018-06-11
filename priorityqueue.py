import linkedlist

class PriorityQueue:
    def __init__(self):
        self.items = linkedlist.LinkedList()
    
    def enqueue(self, item, priority):
        ''' Enqueues the item, a, on the queue, q; complexity O(1). '''
        cursor = self.items
        crsr = cursor.front
        crsrnew = crsr
        crsrnxt = crsr.next
        #print(cursor.numItems, 'numitems')
        if cursor.numItems == 1:
            crsrnxt.priority = crsr.priority
        #if crsrnxt:
         #   print(crsrnxt.priority)    
        crsr.priority = priority
        #if crsrnxt:
         #   print(crsrnxt.priority)

        
        idx = 0
        while cursor is not None:
            if cursor.numItems == 0:
                #print('empty')
                self.items.insert(idx, item, priority)
                #print(crsr.priority)
                break
            elif crsrnxt is None:
                self.items.insert(idx, item, priority)
                #print('lastinsert', crsrnew.priority)
                while crsr:
                 #   print(crsr.priority)
                    if crsr.priority == -1000000:
                        crsr.priority = priority
                    crsr = crsr.next
                break
            elif crsr.priority >= crsrnxt.priority:
               # print('priority', crsr.priority, crsrnxt.priority)
                self.items.insert(idx, item, priority)
                break
            else:
                #print('move')
                crsrnew = crsrnew.next
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
    
    def __iter__(self):
        for item in self.items:
            yield item

def print_queue(pq):
    for item in pq:
        print(item, end=' ')
    print()
    
def main():
    q = PriorityQueue()
    q.enqueue('S', 10)
    print_queue(q)
    
    q.enqueue('t', 2)
    q.enqueue('T', 9)
    print_queue(q)
    q.enqueue('g', 8)
    print_queue(q)
    q.enqueue('i', 7)
    print_queue(q)  
    q.enqueue('n', 6)
    print_queue(q)
    q.enqueue('r', 5)
    q.enqueue('e', 4)
    q.enqueue('s', 3)
   
    print_queue(q)

        
if __name__=="__main__":
    main()