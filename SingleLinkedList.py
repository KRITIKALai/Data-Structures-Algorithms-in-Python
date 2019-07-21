class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    
    def append(self, val):
        current = self.head
        obj = Element(val)
        
        if self.head:
            while current.next:
                current = current.next
            current.next = obj
        
        else:
            self.head = obj
            
    def insert(self, val, position):
        current = self.head
        next_current = current.next
        obj = Element(val)
        target = 0
        
        while target == position:
            current = current.next
            next_current = current.next
            target += 1
            
        current.next = obj
        obj.next = next_current
        
        
    def printLL(self):
        current = self.head
        
        while current.next:
            print(current.value, "  ", current)
            current = current.next
            
        print(current.value, "  ", current)
        
        
        
    