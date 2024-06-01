''' without class
l=[1,2,3]
def app(val):
    l.append(val)
def p():
    l.pop()
app(5)       #l=[1,2,3,5]
p()          #l=[1,2,3]
print(l)
'''

#with class
class stack:
    def __init__(self):
        self.l=[]
    def push(self,data):
        self.l.append(data)
    def pop(self):
        self.l.pop()   #self.l.pop(0) for queue
    def peek(self):
        print(self.l[-1])
s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
print(s.l)
s.peek()
        
              
    

