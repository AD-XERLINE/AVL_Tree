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
        self.num = 0

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
            self.num += 1

        else:
            h = height(self.root)
            max_node = pow(2,h+1)-1
            current = self.root
            if self.num+1 > max_node:
                while(current.left != None):
                    current = current.left
                current.left = Node(val)
                self.num+=1
            elif self.num+1 == max_node:
                while(current.right != None):
                    current = current.right
                current.right = Node(val)
                self.num+=1

            else:
                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)
                else:
                    insert_subtree(current.right,self.num - pow(2,h),val)
                self.num+=1

                    
def insert_subtree(r,num,val):
    if r != None:
        h = height(r)
        max_node = pow(2,h+1)-1
        current = r
        if num+1 > max_node:
            while(current.left != None):
                current = current.left
            current.left = Node(val)
            return

        elif num+1 == max_node:
            while(current.right != None):
                current = current.right
            current.right = Node(val)
            return

        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
            insert_subtree(current.left,num - round(pow(2,h)/2),val)
        else:
            insert_subtree(current.right,num - pow(2,h),val)

    else:
        return


def height(root):
    if root == None:
        return -1

    else:
        left = height(root.left)
        right = height(root.right)
        if left>right:
            return left + 1

        else:
            return right + 1

def treeyarb(root):
    # print(root)
    if root.left.data == 0:
        treeyarb(root.left)
        if root.right.data == 0:
            treeyarb(root.right)
        return

    if root.right.data == 0:
        treeyarb(root.right)
        if root.left.data == 0:
            treeyarb(root.left)
        return
    
    if root.left.data <= root.right.data:
        root.data = root.left.data
        root.left.data = 0
        root.right.data = root.right.data - root.data

    elif root.right.data <= root.left.data:
        root.data = root.right.data
        root.right.data = 0
        root.left.data = root.left.data - root.data

def sum(root):
    if(root == None):
        return 0
    return (int(sum(root.left)) + int(root.data) + int(sum(root.right)))

def printTree(node, level = 0):
    # SUM = int(node.root)
    if node != None:
        printTree(node.right, level + 1)
        # SUM+=int(node.right)
        print('     ' * level, node)
        printTree(node.left, level + 1)
        # SUM+=int(node.left)

T = BinarySearchTree()
inp = input('Enter Input : ').split('/')
ENode = int(inp[0])
data = list(map(int,(inp[1].split())))
L = len(data)
NodeB = (ENode//2) + 1 

if L+NodeB-1 > ENode:
    print("Incorrect Input")
else:
    for i in range(ENode):
        if i+1 < NodeB:
            T.insert(0)
        else:
            T.insert(data[i- ENode])
    # print(NodeB)
    # for i in range(ENode):
    
    while(T.root.data == 0):
        treeyarb(T.root)
        # printTree(T.root)
    print(sum(T.root))