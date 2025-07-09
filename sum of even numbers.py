class node:
    def __init__(loyd,u):
        loyd.data=u
        loyd.next=None
def sum_all():
    t=a
    s=0
    while(t!=None):
        if(t.data%2==0): 
            s=s+t.data
            t=t.next
        else:
            t=t.next
    print("even is",s)
def display(a):
    t=a
    while(t!=None):
        print(t.data)
        t=t.next
a=node(15)
a.next=node(20)
a.next.next=node(30)
display(a)
sum_all()
