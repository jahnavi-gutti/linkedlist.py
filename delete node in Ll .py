class node:
    def __init__(self,data):
        self.data=data 
        self.next=None

def takeinput():
        inputlist=[int(ele) for ele in input().split()]
        head=None
        tail=None
        for  currdata in inputlist:
            if currdata==-1:
                break
            newnode=node(currdata)
            if head is None:
                head=newnode
                tail=newnode
            else:
                tail.next=newnode
                tail=newnode
        return head
def length(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count
def delete(head,i):
    if i<=0 or i>length(head):
        return head
    count=0
    prev=None
    curr=head
    while count<i:
        prev=curr
        curr=curr.next
        count=count+1
    prev.next=curr.next
    del curr
    
        
    
    
def printll(head):
    while head is not None:
        print(str(head.data) +"->",end=" ")
        head=head.next
    print("none")
    return
head=takeinput()
printll(head)
delete(head,2)
printll(head)
"""
1 2 5 7 8 -1
1-> 2-> 5-> 7-> 8-> none
1-> 2-> 7-> 8-> none"""
