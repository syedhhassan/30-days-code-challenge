def empty(qu):
    if qu==[]:
        return True
    else:
        return False

def enqueue(q,i):
    q.append(i)
    if len(q)==1:
        fr=rr=0
    else:
        rr=len(q)-1

def dequeue(q):
    if empty(q):
        return 'Underflow'
    else:
        i=q.pop()

def peek(q):
    if empty(q):
        return 'Underflow'
    else:
        fr=0
    return q[fr]

def display(q):
    if empty(q):
        print('Queue Empty')
    elif len(q)==1:
        print(q[0])
    else:
        fr=0
        rr=len(q)-1
        print(q[fr])
        for a in range(1,rr+1):
            print(q[a])
    
q=[]
fr=None
while True:
    print('Queue Operations')
    print('1.Enqueue')
    print('2.Dequeue')
    print('3.Peek')
    print('4.Display')
    print('5.Exit')
    c=int(input('Enter your choice: '))
    
    if c==1:
        i=int(input('Enter item: '))
        enqueue(q,i)
    
    elif c==2:
        i=dequeue(q)
        if i=='Underflow':
            print('Queue empty')
        else:
            print('Dequeued item is',i)
    
    elif c==3:
        i=peek(q)
        if i=='Underflow':
            print('Queue empty')
        else:
            print(i)
    
    elif c==4:
        display(q)
    
    elif c==5:
        break 

    else:
        print('Invalid Choice')