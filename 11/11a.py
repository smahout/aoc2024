class double_linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = dll_node(value, self.tail, None)
        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def __iter__(self):
        if self.head is not None:
            next = self.head
            yield next
            while next.next is not None:
                next = next.next
                yield next


class dll_node:
    def __init__(self, value, previous, next):
        self.previous = previous
        self.next = next
        self.value = value

        if self.previous is not None:
            self.previous.next = self
        if self.next is not None:
            self.next.previous = self

    def __str__(self):
        return f"Node(previous={self.previous is not None},next={self.next is not None},value={self.value}"

    def set_next(self, dll, next):
        if next.next is None:  # We are the tail
            dll.tail = next
        else:
            next.previous = self
        self.next = next

    def set_previous(self, dll, previous):
        if previous.previous is None:  # We are the head
            dll.head = previous
        else:
            previous.next = self
        self.previous = previous


def blink(all_stones: double_linkedlist):
    current_stones = [stone for stone in all_stones]
    for stone in current_stones:
        if stone.value == 0:
            stone.value = 1
            continue
        if len(str(stone.value)) % 2 == 0:
            left = int(str(stone.value)[:int(len(str(stone.value)) / 2)])
            right = int(str(stone.value)[int(len(str(stone.value)) / 2):])

            left_stone = dll_node(left, stone.previous, None)
            right_stone = dll_node(right, None, stone.next)
            left_stone.set_next(all_stones, right_stone)
            right_stone.set_previous(all_stones, left_stone)
            continue
        stone.value = stone.value * 2024


dll = double_linkedlist()
[dll.append(int(stone)) for stone in open("big.txt").read().strip().split()]

for i in range(25):
    print(
        f"Blinking for the {i + 1}{'st' if i + 1 == 1 else 'nd' if i + 1 == 2 else 'rd' if i + 1 == 3 else 'th'} time")
    blink(dll)

count = 0
for d in dll:
    count += 1
print(count)
