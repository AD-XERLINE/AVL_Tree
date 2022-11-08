class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val >= current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def compare(a,b,Len):
    A = BinarySearchTree()
    A.create(str(initial_list[int(a)]))
    T = Bo(int(a))
    if T < Len:
        A.create(str(initial_list[T]))
        T = BT(int(a))
        if T < Len:
            A.create(str(initial_list[T]))
    SA = sum(A.root)

    B = BinarySearchTree()
    B.create(str(initial_list[int(b)]))
    T = Bo(int(b))
    if T < Len:
        B.create(str(initial_list[T]))
        T = BT(int(b))
        if T < Len:
            B.create(str(initial_list[T]))
    SB = sum(B.root)

    if SA < SB:
        print(a + '<' + b)
    elif SA > SB:
        # print("{0}>{1}".format(a,b))
        print(a + '>' + b)
    elif SA == SB:
        print(a+'='+b)
    
                
def printTree(node, level = 0):
    # SUM = int(node.root)
    if node != None:
        printTree(node.right, level + 1)
        # SUM+=int(node.right)
        print('     ' * level, node)
        printTree(node.left, level + 1)
        # SUM+=int(node.left)

def Bo(N):
    N = (N*2)+1
    return int(N)

def BT(N):
    N = (N*2)+2
    return int(N)

def sum(root):
    if(root == None):
        return 0
    return (int(sum(root.left)) + int(root.data) + int(sum(root.right)))

P = BinarySearchTree()
inp = input('Enter Input : ').split('/')
initial_list = list(map(int, inp[0].split()))
L = len(initial_list)
compare_list = inp[1].split(',')

for i in initial_list:
    P.create(i)

print(sum(P.root))

for i in range(len(compare_list)):
    compare(compare_list[i][:1],compare_list[i][2:],L)

