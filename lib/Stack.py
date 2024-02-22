class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.items = items

        self.limit = limit
        
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            return None

    def pop(self):
        if len(self.items) > 0:
            item = self.items[-1]
            self.items.pop()
            return item
        else:
            return None

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) < self.limit:
            return False
        else:
            return True

    def search(self, target):
        counter = 0
        for item in reversed(self.items):
            if item == target:
                return counter
            else:
                counter += 1
        return -1
