class Node : 
    def __init__(self, data) :
        self.data = data
        self.next = None

class Queue :
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
    
    def enqueue(self, data):
        node = Node(data)
        if self.tail == None :
            self.head = self.tail = node
        else :
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def dequeue(self):
        if self.head == None :
            return None
        else :
            node = self.head
            self.head = self.head.next
            self.size -= 1
            return node.data
    
    def peek(self):
        if self.head == None :
            return None
        else :
            return self.head.data
    
    def printQueue(self):
        node = self.head
        while node != None :
            print(node.data, end = " ")
            node = node.next
        print()

MyQ = Queue()
MyQ.enqueue(1)
MyQ.enqueue(2)
MyQ.enqueue(3)
MyQ.printQueue()
