#Percobaan 2
from collections import deque

queue = deque([1,2,3,4,5])
print("Antrian Sekarang : ",queue)

queue.append(6)
print("Antrian Masuk : ",6)
print("Antrian Sekarang : ",queue)

queue.append(7)
print("Antrian masuk : ",7)
print("Tumpukan sekarang : ",queue)

out = queue.popleft()
print("Antrian keluar : ",out)
print("Antrian sekarang : ",queue)