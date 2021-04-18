class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = self.items.reverse()
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "The elements is inserted at the end of list!"

    def dequeue(self):
        if self.is_empty():
            return 'The queue is empty!'
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return 'The queue is empty!'
        else:
            return self.items[0]

    def delete(self):
        if self.is_empty():
            return 'The queue is empty!'
        else:
            self.items = None


custome_queue = Queue()
print(custome_queue.is_empty())
print(custome_queue.dequeue())
custome_queue.enqueue(1)
custome_queue.enqueue(2)
custome_queue.enqueue(3)
custome_queue.dequeue()
print(custome_queue)
