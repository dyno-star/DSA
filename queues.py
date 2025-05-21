from collections import deque

q = deque()
q.append(4)
q.append(3)
q.append(2)
q.popleft()

print(q)