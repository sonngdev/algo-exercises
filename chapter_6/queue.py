class EmptyException(Exception):
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def enqueue(self, item):
        if (self._size == len(self._data)):
            self._resize()

        index_to_queue = (self._front + self._size) % len(self._data)
        self._data[index_to_queue] = item
        self._size += 1

    def dequeue(self):
        if (self.is_empty()):
            raise EmptyException('Queue is empty')
        item = self.first()
        self._data[self._front] = None # garbage-collect old item
        self._size -= 1
        self._front = (self._front + 1) % len(self._data)
        return item

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.size == 0:
            raise EmptyException('Queue is empty')
        return self._data[self._front]

    def __len__(self):
        return self._size

    def _resize(self):
        new_data = [None] * (len(self._data) * 2)

        copy_ops = self._size
        for i in range(0, copy_ops):
            index_to_copy = (self._front + i) % len(self._data)
            new_data[i] = self._data[index_to_copy]

        self._data = new_data
        self._front = 0


if __name__ == "__main__":
    queue = ArrayQueue()
    assert(len(queue) == 0)
    assert(queue.is_empty())

    queue.enqueue(12)
    assert(not queue.is_empty())
    assert(len(queue) == 1)
    assert(queue.first() == 12)
    assert(len(queue) == 1)

    item = queue.dequeue()
    assert(item == 12)
    assert(len(queue) == 0)
    assert(queue.is_empty())
