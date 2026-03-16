class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

print("До разворота:")
current = head
while current:
    print(current.data, end=" ")
    current = current.next

prev = None
current = head

while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

head = prev

print("\nПосле разворота:")
current = head
while current:
    print(current.data, end=" ")
    current = current.next