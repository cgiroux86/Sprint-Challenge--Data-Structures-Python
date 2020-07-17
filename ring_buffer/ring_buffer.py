class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.tracker = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            if self.tracker == len(self.data) - 1:
                self.data[self.tracker] = item
                self.tracker = 0

            else:
                self.data[self.tracker] = item
                self.tracker += 1

    def get(self):
        lst = []
        for d in self.data:
            lst.append(d)
        return lst
# class Node:
#     def __init__(self, value):
#         self.next = None
#         self.prev = None
#         self.value = value


# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.head = None
#         self.tail = None
#         self.size = 0
#         self.tracker = None

#     def append(self, item):
#         new_node = Node(item)
#         if self.size < self.capacity:
#             if not self.head:
#                 self.head = new_node
#                 self.tail = new_node
#                 self.tracker = new_node
#                 self.size += 1
#             else:
#                 if self.head is self.tail:
#                     self.head.next = new_node
#                     new_node.prev = self.head
#                     self.tail = new_node
#                 self.tail.next = new_node
#                 new_node.prev = self.tail
#                 self.tail = new_node
#                 self.size += 1
#         else:
#             if self.tracker is self.head:
#                 self.tracker = self.tracker.next
#                 new_node.next = self.head.next
#                 self.head.next.prev = new_node
#                 self.head = new_node
#             elif self.tracker is self.tail:
#                 self.tail.prev.next = new_node
#                 new_node.prev = self.tail.prev
#                 self.tail = new_node
#                 self.tracker = self.head
#             else:
#                 curr = self.head
#                 while curr and curr != self.tracker:
#                     curr = curr.next
#                 if curr.prev is self.head:
#                     self.tracker = curr.next
#                     self.head.next = new_node
#                     new_node.prev = self.head
#                     new_node.next = curr.next
#                     curr = new_node
#                 curr.prev.next = new_node
#                 curr.next.prev = new_node
#                 new_node.prev = curr.prev
#                 new_node.next = curr.next
#                 curr = new_node
#                 self.tracker = curr.next

#     def print_list(self):
#         curr = self.head
#         lst = []
#         while curr:
#             lst.append(curr.value)
#             curr = curr.next
#         print(lst)

#     def get(self):
#         curr = self.head
#         lst = []
#         while curr:
#             lst.append(curr.value)
#             curr = curr.next
#         return lst


a = RingBuffer(5)
# a.append('a')
# a.append('b')
# a.append('c')
# a.append('d')
# a.append('e')
# a.append('f')
for r in range(50):
    a.append(r)
a.get()
