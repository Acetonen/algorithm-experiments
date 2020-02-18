class Deque:
    def __init__(self):
        self.queue = list()

    def addFront(self, item):
        self.queue = [item] + self.queue

    def addTail(self, item):
        self.queue.append(item)

    def removeFront(self):
        head = self.queue[0] if self.queue else None
        self.queue = self.queue[1:]

        return head

    def removeTail(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)


def rotate_queue_left(queue, number):
    if queue.size():
        for _ in range(number):
            queue.addFront(queue.removeTail())

    return queue


def rotate_queue_right(queue, number):
    if queue.size():
        for _ in range(number):
            queue.addTail(queue.removeFront())

    return queue


def check_palindrome(string):
    deque = Deque()
    for char in string:
        deque.addTail(char)

    for _ in range(deque.size()//2):
        if deque.removeFront() != deque.removeTail():
            return False

    return True

