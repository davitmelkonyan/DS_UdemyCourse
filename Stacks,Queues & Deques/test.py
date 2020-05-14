from Stack import myStack
s = myStack()
print (s.isEmpty())
s.push(1)
s.push("two")
print (s.peek())
s.push(True)
print (s.size())
print (s.isEmpty())
print (s.pop())
print (s.pop())
print (s.pop())
print (s.isEmpty())
print(" ")
from Queues import Queue
q = Queue()
print (q.size())
print (q.isEmpty())
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(" ")
from Deque import myDeque
d = myDeque()
d.addFront('1')
d.addRear('2')
print (d.size())
print (d.removeFront()+' '+ d.removeRear())
print (d.size())
print (d.isEmpty())
