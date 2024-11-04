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
def balanced_paranthesis():

    pairs = {"(":")",
              
             "[":"]",

             "{":"}"}

    expression = input("Expression: ")
    for paranthesis in expression:

        if paranthesis in pairs:
            s.elements.append(paranthesis)

        elif paranthesis in pairs.values():

            if len(s.elements)<=0:
                return False
            
            pair = s.pop()

            if pairs[pair] == paranthesis:
                continue
            else:
                return False
    
            
    if len(s.elements)==0:
        return True    
    
    return False         
            
       
print(balanced_paranthesis())







