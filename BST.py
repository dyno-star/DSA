class Node:
    def __init__(self, value):
        self.value = value
        self.left= None
        self.right   = None

class BST:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if  temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True
        return False
    def BFS(self):
        if not self.root:
            return []
        queue = []
        result = []
        queue.append(self.root)
        while len(queue) > 0:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
    
    def dfs_pre_order(self):
        if not self.root:
            return []
        result = []
        def traverse(current):
            result.append(current.value)
            if current.left:
                traverse(current.left)
            if current.right:
                traverse(current.right)
        traverse(self.root)
        return result
    
    def dfs_post_order(self):
        if not self.root:
            return []
        result = []
        def traverse(current):
            if current.left:
                traverse(current.left)
            if current.right:
                traverse(current.right)
            result.append(current.value)
        traverse(self.root)
        return result
    
    def dfs_in_order(self):
        if not self.root:
            return []
        result = []
        
        def traverse(current):
            if current.left:
                traverse(current.left)
            result.append(current.value)
            if current.right:
                traverse(current.right)
        traverse(self.root)
        return result
            

            
tree = BST()
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)
#print(tree.BFS())
print(tree.dfs_post_order())

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)
print(tree.contains(4))