class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.value
    
    def peek(self):
        if self.front is None:
            return None
        return self.front.value
    
    def is_empty(self):
        return self.front is None
    
    def show(self):
        current = self.front
        while current:
            print(current.value, end=' ')
            current = current.next
        print("None")
        
list_queue = Queue()
list_queue.enqueue(1)
list_queue.enqueue(2)
list_queue.enqueue(3)
list_queue.show()  
print(list_queue.dequeue())  