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
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def closestValue(r,value,T,S):
    if r is None :
        return "Closest value of " + str(value) + " : " + str(T)

# ใช้ else ดักดีกว่า
    if r.data == value:
        T = r.data
        return "Closest value of " + str(value) + " : " + str(T)
        # print(r)
        # return closestValue(r,value,T)
    elif r.data == value+1:
        T = r.data
        S = True
    elif r.data == value-1 and S == False:
        T = r.data
        # print("-")
        S = True
    elif (S == False):
        # print(r.data)
        if (T.data > r.data and value < r.data):
            # print(r.data)
            T.data = r.data
            # print(T)
        elif (T.data < r.data and value > r.data):
            T.data = r.data

    if r.data < value:
        return closestValue(r.right,value,T,S)
    
    if r.data > value:
        return closestValue(r.left,value,T,S)
    
    return "Closest value of " + str(value) + " : " + str(T)

Section = False
tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split(" "):
    tree.create(int(e))
    printTree90(tree.root)
    print("--------------------------------------------------")

# print(int(data[1])-1)
print(closestValue(tree.root,int(data[1]),tree.root,Section))