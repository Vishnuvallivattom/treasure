class node:
    def __init__(loyd,u):
        loyd.data=u
        loyd.next=None
def sum_all():
    t=a
    s=0
    while(t!=None):
        s=s+t.data
        t=t.next
    print(s)
def display(a):
    t=a
    while(t!=None):
        print(t.data)
        t=t.next
a=node(10)
a.next=node(20)
a.next.next=node(30)
display(a)
sum_all()
