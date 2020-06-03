#Given 1st node, find if LL contains a "cycle"
from SinglyLL import Node

def cycle_check(node):
    marker1 = node
    marker2 = node
    while marker2 != None and marker2.next != None:
        marker1 = marker1.next
        marker2 = marker2.next.next
        if(marker2 == marker1):
            return True
    return False

from nose.tools import assert_equal
#with Cycle
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = a

#without Cycle
x = Node(1)
y = Node(2)
z = Node(3)
x.next = y
y.next = z

class TestCycleCheck(object):
    def test(self,sol):
        assert_equal (sol(a),True)
        assert_equal (sol(x),False)
        print ("Tests passed")

t = TestCycleCheck()
t.test(cycle_check)