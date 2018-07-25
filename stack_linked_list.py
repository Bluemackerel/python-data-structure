#making 


class Node():
    def __init__(self):
        self.next = None
        self.item = None


class Stack():
    def __init__(self):
        self._first = None
    
    def push(self,item):
        
        old_first = self._first
        self._first = Node()
        self._first.item = item
        self._first.next = old_first
    
    def pop(self):
        if self.isEmpty():
            raise "엠티엠티스택"
        item = self._first.item
        self._first = self._first.next
        return item


    def isEmpty(self):
        return self._first == None

def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    while not s.isEmpty():
        print(s.pop())
        
if __name__ == '__main__':
    main()