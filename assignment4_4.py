class Node:
    def __init__ (self,info,n):
        self.info = info
        self.next = n
    
class LinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0
    def addToHead(self,val):
        n = Node(val,None)
        if self.size == 0:
            n = Node(val,None)
            self.head = n
            self.tail = n
            self.size+=1
        else:
            n = Node(val,self.head)
            self.head = n
            self.size +=1
    def addToTail(self,val):
        if self.size == 0:
            n = Node(val,None)
            self.head = n
            self.tail = n
            self.size +=1
        else:
            n = Node(val,None)
            self.tail.next = n
            self.tail = n
            self.size+=1
    def deleteHead(self):
        if self.size == 0:
            return None
        if self.size == 1:
            val = self.head.info
            self.head = None
            self.tail = None
            self.size = 0
            return val
        else:
            val = self.head.info
            self.head = self.head.next
            self.size -=1
            return val
            


    def deleteTail(self):
        if self.size == 0:
            return None
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            val = self.tail.info
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
            self.size -=1
            return val
    def printll(self):
        temp = self.head
        while temp != None:
            print(temp.info,"->",end="")
            temp = temp.next
        print()

    def deleteAtLocation(self):
        while True:
            try:
                location = int(input("Location: "))
                break
            except ValueError:
                print("location must be an integer please try again")
        if self.size == 0:
            print("empty list")
            return
        elif location < 0:
            print("invalid location must be 0 and higher")
            return
        elif location == 0:
            self.deleteHead()
            self.printll()
            return 
        else:
            current_location = 0
            temp = self.head

            while current_location < location-1 and temp.next != None:
                temp = temp.next
                current_location +=1
            if temp.next != None:
                temp.next = temp.next.next
                self.printll()
            else:
                print("invalid location too large")
                return
                
            




        
            

ll = LinkedList()

ll.deleteHead()
ll.deleteTail()

