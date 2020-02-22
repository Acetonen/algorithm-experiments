class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        head = self.queue[0] if self.queue else None
        self.queue = self.queue[1:]

        return head

    def size(self):
        return len(self.queue)


def rotate_queue(queue, number):
    if queue.size():
        for _ in range(number):
            queue.enqueue(queue.dequeue())

    return queue


class QueueFromTwoStack:
    def __init__(self, stack_one, stack_two):
        self.stack_one = stack_one
        self.stack_two = stack_two
        self._check_stack_two()

    def _refill_stack_two(self):
        for _ in range(self.stack_one.size()):
            item = self.stack_one.pop()
            if item:
                self.stack_two.push(item)

    def _check_stack_two(self):
        if self.stack_two.size() == 0:
            self._refill_stack_two()

    def enqueue(self, item):
        self.stack_one.push(item)

    def dequeue(self):
        head = self.stack_two.pop()
        self._check_stack_two()

        return head

    def size(self):
        return self.stack_one.size() + self.stack_two.size()
