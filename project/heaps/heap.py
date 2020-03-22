class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def _make_heap(self, depth):
        self.tree_size = 2 ** (depth + 1) - 1
        self.HeapArray = [None for _ in range(self.tree_size)]

    def _sieving_array_up(self, element_index):
        while True:
            left_or_right = element_index % 2
            parent_index = (element_index - (2 - left_or_right)) // 2
            element_key = self.HeapArray[element_index]
            parent_key = self.HeapArray[parent_index]

            if parent_index < 0 or parent_key > self.HeapArray[element_index]:
                return element_index
            else:
                self.HeapArray[parent_index] = element_key
                self.HeapArray[element_index] = parent_key
                element_index = parent_index

    def _insert_new_element(self, new_key):
        for index, key in enumerate(self.HeapArray):
            if key is None:
                self.HeapArray[index] = new_key
                return index

    def Add(self, key):
        key_index = self._insert_new_element(key)

        if key_index is not None:
            return self._sieving_array_up(key_index)

        return False  # если куча вся заполнена

    def MakeHeap(self, array, depth):
        self._make_heap(depth)
        for key in array:
            self.Add(key)

    def _get_last_element(self):
        previous_element = None

        for index, element in enumerate(self.HeapArray):
            if element is None:
                self.HeapArray[index - 1] = None
                if index != 1:  # noqa
                    return previous_element
                return

            previous_element = element

        self.HeapArray[-1] = None

        return element  # noqa

    def _get_max_child(self, element_index):
        children = list()

        for number in range(1, 3):
            index = 2 * element_index + number

            try:
                children.append((self.HeapArray[index] or -1, index))
            except IndexError:
                return

        children = sorted(children, key=lambda child: child[0], reverse=True)

        return children[0]

    def _compare_with_children(self, element_index, element_key):
        max_child = self._get_max_child(element_index)

        if max_child is None:
            return
        elif (
            self.HeapArray[max_child[1]] is not None
            and self.HeapArray[max_child[1]] > self.HeapArray[element_index]
        ):
            child_key = self.HeapArray[max_child[1]]
            self.HeapArray[max_child[1]] = element_key
            self.HeapArray[element_index] = child_key

            return max_child[1]

    def _sieving_array_down(self):
        self.HeapArray[0] = self._get_last_element()
        element_index = 0

        while element_index is not None:
            element_key = self.HeapArray[element_index]
            element_index = self._compare_with_children(element_index, element_key)

    def GetMax(self):
        if self.HeapArray[0] is None:
            maximum = -1  # если куча пуста
        else:
            maximum = self.HeapArray[0]
            self._sieving_array_down()

        return maximum
