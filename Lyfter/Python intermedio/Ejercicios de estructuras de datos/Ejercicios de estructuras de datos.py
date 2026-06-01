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
    
    def print_stack(self):
        current = self.top
        while current:
            print(current.value, end=' ')
            current = current.next
        print()
        
if __name__ == "__main__":    
    stack = Stack()    
stack.push(5)
stack.push(7)
stack.push(8)
        
stack.print_stack()

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
    
    def print_deque(self):
        current = self.front
        while current:
            print(current.value, end=' ')
            current = current.next
        print()
    
if __name__ == "__main__":
    deque = Deque()
    deque.push_left(17)
    deque.push_right(24)
    deque.push_left(5)
    deque.print_deque()
    
#Ejercicio 3
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return node

    def _print_recursive(self, node):
        if node:
            self._print_recursive(node.left)
            print(node.value)
            self._print_recursive(node.right)
    
    def inorder_traversal(self):
        return self._inorder_recursive(self.root)
    
    def _inorder_recursive(self, node):
        result = []
        if node:
            result.extend(self._inorder_recursive(node.left))
            result.append(node.value)
            result.extend(self._inorder_recursive(node.right))
        return result 
    
    def print_tree(self):
        self._print_recursive(self.root)

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(14)
    tree.insert(7)
    tree.insert(23)
    tree.insert(6)
    tree.insert(34)
    
    tree.print_tree()

