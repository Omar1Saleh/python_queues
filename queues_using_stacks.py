class Stack:
    def __init__(self):
        self.list = []

    def len(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if self.len() == 0:
            return None
        return self.list.pop()

class QueueInStack:
    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()

    def enqueue(self, item):
        self.instack.push(item)
        
    def dequeue(self):
        while self.instack.len():
            self.outstack.push(self.instack.pop())
        result = self.outstack.pop()
        while self.outstack.len():
            self.instack.push(self.outstack.pop())
        return result
    
custome_queue = QueueInStack()
custome_queue.enqueue(1)
custome_queue.enqueue(2)
custome_queue.enqueue(3)
print(custome_queue.dequeue())
