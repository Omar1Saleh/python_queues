from multiprocessing import Queue

custome_q = Queue(maxsize=3)
print(custome_q.empty())
custome_q.put(1)
custome_q.put(2)
custome_q.put(3)
print(custome_q.full())
print(custome_q.get())