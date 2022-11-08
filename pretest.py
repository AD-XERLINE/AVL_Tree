class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.level = None

    def __str__(self):
        return str(self.data)

class BST:
    class Queue:
        def __init__(self,item = None):
            if item == None:
                self.item = []
            else:
                self.item = item

        def enQueue(self,data):
            self.item.append(data)
        
        def deQueue(self):
            self.item.pop(0)
        
        def isEmpty(self):
            return self.item == []


    def __init__(self):
        self.root = None
        self.num = 0

    def inser(self,root,data):
        if root == None:
            self.root = Node(data)
            self.num += 1
            return
        else:
            current = root
            if data > current.data :
                if current.right == None:
                    current.right = Node(data)
                    self.num += 1
                else:
                    return self.inser(current.right,data)
            elif data < current.data :
                if current.left == None:
                    current.left = Node(data)
                    self.num += 1
                else:
                    return self.inser(current.left,data)

    def MAX(self):
        t = self.root
        while t.right != None:
            t = t.right
        return t.data

    def MIN(self):
        t = self.root
        while t.left != None:
            t = t.left
        return t.data

    def breadth(self,node):
            q = [node]
            while len(q) != 0 :
                temp = q.pop(0)
                print(temp,end=' ')
                if temp.left != None :
                    q.append(temp.left)
                if temp.right != None :
                    q.append(temp.right)
        
def printtree(root,level = 0):
    if root != None:
        printtree(root.right,level + 1)
        print('    '*level,root.data)
        printtree(root.left,level + 1)

def father(r,key,temp):
    if r is None :
        return "Not Found Data"

    if r.data == key and temp == r:
        return "None Because " +str(key)+" is Root"
    
    if r.data == key:
        return temp

    if r.data < key:
        return father(r.right,key,r.data)
    
    if r.data > key:
        return father(r.left,key,r.data)
    return r

Se = ''
def inoder(root):
    global Se
    if root != None:
        inoder(root.left)
        Se += str(root.data) + ' '
        inoder(root.right)

def CV(root,key,T,S):
    if root == None:
        return print(key,T)

    if root.data == key:
        return print(key,T)
    elif root.data == key+1:
        T = root.data
        S = True
    elif root.data == key-1 and S == False:
        T.data = root.data

    if key > root.data:
        return CV(root.right,key,T,S)
    elif key < root.data:
        return CV(root.left,key,T,S)

    return T.data
    
T = BST()
S = False
inp = list(map(int,input("Enter input : ").split(' ')))
# print(inp)
for i in inp:
    T.inser(T.root,i)
printtree(T.root)

T.breadth(T.root)

# print(T.MAX())
# print(T.MIN())

# CV(T.root,5,T.root,S)

# inoder(T.root)
# print(Se)

# print(sum(T.root))