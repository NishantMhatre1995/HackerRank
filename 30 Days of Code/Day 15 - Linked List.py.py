class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        current = head
        nn = Node(data)
        if current == None:            
            return nn
        else:
            tn = current            
            while tn.next != None:
                tn = tn.next
            tn.next = nn
            return current
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);   1