import time
import KopiecMAx as k
import kolejkaNaLiscie as pq
import Unorderedlist as l
import random as r
import matplotlib.pyplot as plt

print("Test wydajnosci dla kolejki piorytetowej na liscie")

timePQ = []
timePQx = []
qp = pq.ListProrityQueue()
for i in range (10,17):
    n = 2**i
    timePQx.append(n)
    start = time.time()
    for j in range(2**i):
        x = r.random()
        qp.enqueue(j)
    for z in range(2**i):
        qp.dequeue()
    end = time.time()
    assert qp.isEmpty() == True
    timePQ.append(end - start)

x = timePQx
y = timePQ
plt.loglog(x,y, basex = 2, basey = 2, color = "black")
print(timePQ)

print("Test wydajnosci dla kolejki piorytetowej na kopcu max")

timeMax = []
timeMaxX = []
kopiec = k.MaxHeap()
for i in range (10,17):
    n = 2**i
    timeMaxX.append(n)
    start = time.time()
    for j in range(2**i):
        x = r.random()
        kopiec.enqueue(x)
    for z in range(2**i):
        kopiec.dequeue()
    end = time.time()
    timeMax.append(end - start)

print(timeMax)

x = timeMaxX
y = timeMax
plt.loglog(x,y, basex = 2, basey = 2, color = "cyan")


print("Test wydajnosci dla kolejki piorytetowej na liscie z dowiazaniami")

timeLinked = []
timeLinkedx = []
linkedlist = l.NodeList()
for i in range (10,17):
    n = 2**i
    timeLinkedx.append(n)
    
    start = time.time()
    for j in range(2**i):
        x = r.random()
        linkedlist.add(x)
    for z in range(2**i):
        linkedlist.getMax()
    end = time.time()
    timeLinked.append(end - start)

print(timeLinked)


x = timeLinkedx
y = timeLinked
plt.loglog(x,y, basex = 2, basey = 2, color = "magenta")
plt.show()




















