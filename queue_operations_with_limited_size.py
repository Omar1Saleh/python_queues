class Queue:

    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max = max_size
        self.end = -1
        self.start = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_full(self):
        if (self.end + 1 == self.start) or (self.end + 1 == self.max and self.start == 0):
            return True
        else:
            return False

    def is_empty(self):
        if self.end == -1 and self.start == -1:
            return True

    def enqueue(self, value):
        if self.is_full():
            return 'The queue is full!', value, 'cant be inserted.'
        else:
            if self.end + 1 == self.max:
                self.end = 0
            else:
                self.end += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.end] = value
            return value, 'is inserted!'

    def dequeue(self):
        if self.is_empty():
            return 'This queue is empty!'
        else:
            first_element = self.items[self.start]
            start = self.start
            if self.start == self.end:
                self.start = -1
                self.end = -1
            elif self.start + 1 == self.max:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_element

    def peek(self):
        if self.is_empty():
            return 'empty queue!'
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.max *[None]
        self.end=-1
        self.start=-1

custome_queue = Queue(6)
print(custome_queue.is_empty())
print(custome_queue.enqueue(1))
print(custome_queue.enqueue(2))
print(custome_queue.enqueue(3))
print(custome_queue.dequeue())
print(custome_queue)
print(custome_queue.is_full())
print(custome_queue.peek())
custome_queue.delete()
print(custome_queue.peek())