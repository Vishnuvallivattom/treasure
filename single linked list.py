class fogg:
    def __init__(loyd,u):
        loyd.data=u
        loyd.next=None
        loyd.prev=None
def display():
    t=a
    while(t!=None):
        print(t.data)
        t=t.next
a=fogg(10)
a.next=fogg(20)
a.next.next=fogg(30) 
display()
