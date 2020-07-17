class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            return self.right.contains(target)
        else:
            return True

    def iter_print(self):
        stack = [self]
        while stack:
            n = stack.pop()
            if n.right:
                stack.append(n.right)
                print('right', n.right.value)
            if n.left:
                stack.append(n.left)
                print('left', n.left.value)

    def in_order(self):
        stack = []
        curr = self
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack:
                break
            curr = stack.pop()
            print('value', curr.value)
            curr = curr.right

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        print(fn(self.value))
        if self.right:
            self.right.for_each(fn)

    def invert(self, node):
        if self.left:
            self.left.invert(self.left)
            r = self.right
            self.right = self.left
            self.left = r
        if self.right:
            self.right.invert(self.right)
            l = self.left
            self.left = self.right
            self.right = l
