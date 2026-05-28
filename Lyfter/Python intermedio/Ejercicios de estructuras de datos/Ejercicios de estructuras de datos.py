#Ejercicio 1
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def is_empty(self):
        return self.top is None    

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        popped_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return popped_value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.value
    
    def get_size(self):
        return self.size
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print("Top element:", stack.peek())  
    print("Stack size:", stack.get_size())  
    print("Popped element:", stack.pop())  
    print("Top element after pop:", stack.peek())  
    print("Stack size after pop:", stack.get_size())
    
#Ejercicio 2
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
        
    def is_empty(self):
        return self.count == 0
    
    def push_left(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node
        self.count += 1

    def push_right(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.count += 1

    def pop_left(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        popped_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        return popped_value

    def pop_right(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        popped_value = self.rear.value
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            current = self.front
            while current.next != self.rear:
                current = current.next
            current.next = None
            self.rear = current
        self.count -= 1
        return popped_value
    
if __name__ == "__main__":
    deque = Deque()
    deque.push_left(10)
    deque.push_right(20)
    deque.push_left(5)
    
    print("Popped from left:", deque.pop_left())  
    print("Popped from right:", deque.pop_right())  
    print("Popped from left again:", deque.pop_left())
    
#Ejercicio 3
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value
        
def print_in_order(node):
        if node is not None:
            print_in_order(node.left)
            print(node.val, end=' ')
            print_in_order(node.right)

if __name__ == "__main__":
        root = Node(4)
        left_child = Node(8)
        right_child = Node(23)
        
        root.left = left_child
        root.right = right_child
        
        root.left.left = Node(6)
        root.left.right = Node(3)
        
        print("In-order traversal of the binary tree:")
        print_in_order(root)
        print()          
