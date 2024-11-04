class Queue:
    def __init__(self):
        self.elements = []
    def enqueue(self,val):
        self.elements.append(val)
    def dequeue(self):
        return self.elements.pop(0)
    def empty(self):
        return len(self.elements) == 0
        
    
class Stack:
    def __init__(self):
        self.elements = []
    def push(self,val):
        self.elements.append(val)
    def pop(self):
        if len(self.elements) == 0:
            return None
        
        else:
            return self.elements.pop()
    def empty(self):
        return len(self.elements) == 0    
    


    
s = Stack()
q = Queue()
result = "true"
while True:
    val = input("word: ").lower().strip()

    if val == "":
        print("please enter a valid word")
        continue

    for i in val:
        if i.isdigit():
            print("please enter a valid word")
            break

    else:
         break
    
    


for i in val:
    q.enqueue(i)
    s.push(i)
    

while not s.empty() and not q.empty():
    if s.pop() != q.dequeue():
        result = "false"
        break
    


    

if result == "false":
    print(f"{val} isn't a palindrome")
else:
    print(f"{val} is a palindrome")
    


