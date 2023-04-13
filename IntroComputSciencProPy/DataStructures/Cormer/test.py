import stack
import queue

"""s1 = stack.Stack()
s1.push(15)
s1.push(6)
s1.push(2)
s1.push(9)
print(s1)
a= s1.pop()
print(a)
s1.pop()
print(s1)"""

q1 = queue.Queue()
print(q1)
q1.enqueue(4)
q1.enqueue(3)
q1.enqueue(2)
q1.enqueue(1)
print(q1)
q1.dequeue()
print(q1)
q1.dequeue()
print(q1)
