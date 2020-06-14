from SinglyLL import Node

def nth_To_Last_Node(n, head):
    left  = head
    right = head
    #right pointer set at n nodes away from head
    for i in range(n-1):
        if not right.next:
            raise LookupError('Error: n is larger than the linked list.') #edge case
        right = right.next
    while right.next:
        left  = left.next
        right = right.next
    return left

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

class TestNLast(object):
    def test(self,sol):
        assert_equal(sol(2,a),d)
        print ('ALL TEST CASES PASSED')
        
t = TestNLast()
t.test(nth_To_Last_Node)