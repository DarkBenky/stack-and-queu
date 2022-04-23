class stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def print(self):
        print (self.items)

class queue():
    def __init__(self):
        self.items = []
    def push(self, item):
        return self.items.insert(0, item)
    def pop(self):
        return self.items.pop()
    def print(self):
        print (self.items)
    
   
stack = stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.print()
stack.pop()
stack.print()
print("--------------------------------------------------------")
queue = queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
queue.print()
queue.pop()
queue.print()
