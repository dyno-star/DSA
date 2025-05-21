class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            pre = None
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        return temp.value
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head.next
            self.head = temp
            
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        else:
            return False
        
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value) 
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        
        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
    

# Testing the LinkedList
my_linked_list = LinkedList()
my_linked_list.append(2)
my_linked_list.append(23)
my_linked_list.append(12) 
my_linked_list.prepend(1)
my_linked_list.insert(3,74)
my_linked_list.pop_first()
my_linked_list.set_value(1, 4)
my_linked_list.remove(2)
my_linked_list.reverse()
my_linked_list.print_list() 


# Uncomment to test pop
# my_linked_list.pop()  # This should remove 2
# my_linked_list.print_list()  # Expected Output after pop: 1 4