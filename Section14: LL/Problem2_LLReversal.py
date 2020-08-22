#reverse in place (i.e. o(1) space)
from SinglyLL import Node

def reverse(head):
    current = head
    prev = None
    nxt = None

    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
print (a.next.value)
print (b.next.value)
print (c.next.value)

reverse(a)
print (d.next.value)
print (c.next.value)
print (b.next.value)

