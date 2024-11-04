
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
s = Stack()
message = input("Message: ")
if len(message)==1:
    print("there was no coded message")

for i in message:
    if i == "*":
        if len(s.elements) == 0:
            continue
        else:
            while s.elements:
                value = s.pop()
                print(value,end="")
            print(" ",end="")
                
            
    else:
        s.push(i)

if len(s.elements)>0:
    print("there was no coded message")
else:
    print()

        
