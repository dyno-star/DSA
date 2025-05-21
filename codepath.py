class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
def delete_item(head, item):
    if not head:
        return None
    
    current = head
    while current.next:
        if current.next.value == item:
            current.next = current.next.next
        current = current.next
    return head
slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle
# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))
# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))