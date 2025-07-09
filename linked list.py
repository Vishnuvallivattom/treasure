class node:
    def __init__(self,u):
        self.data=u
        self.next=None
def midn():
    c=0
    t=a
    while(t!=None):
        c=c+1
        t=t.next
    print("count is",c)
    t=a
    for i in range(c//2):
        t=t.next
        print("middle is",t.data)

a=node(15)
a.next=node(20)
a.next.next=node(30)
midn()

