#implementations in stack

def empty(s):
    if s==[]:
        return True
    else:
        return False

def push(s,i):
    s.append(i)
    top=len(s)-1

def pop(s):
    if empty(s):
        return 'Underflow'
    else:
        i=s.pop()
        if len(s)==0:
            top=None
        else:
            top=len(s)-1
        return i

def peek(s):
    if empty(s):
        return 'Underflow'
    else:
        top=len(s)-1
        return s[top]

def display(s):
    if empty(s):
        print('Stack Empty')
    else:
        top=len(s)-1
        print(s[top])
        for f in range(top-1,-1,-1):
            print(s[f])

st=[]
top=None
while True:
    print('Implementations in Stack')
    print('1.Push')
    print('2.Pop')
    print('3.Peek')
    print('4.Display')
    print('5.Peek')
    c=int(input('Enter your choice: '))
    
    if c==1:
        i=int(input('Enter item: '))
        push(st,i)
    
    elif c==2:
        i=pop(st)
        if i=='Underflow':
            print('Stack Empty')
        else:
            print('Popped item is',i)
    
    elif c==3:
        i=peek(st)
        if i=='Underflow':
            print('Stack Empty')
        else:
            print('Topmost item is',i)
    
    elif c==4:
        display(st)
    
    elif c==5:
        break
    
    else:
        print('Invalid Choice')