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

def search(r,key,temp):

    if r is None :
        return "Not Found Data"

    if r.data == key:
        temp +='*'
        return temp

    if r.data < key:
        temp += 'R'
        # print(temp)
        return search(r.right,key,temp)
    
    if r.data > key:
        temp += 'L'
        return search(r.left,key,temp)
    
    return temp

tree = BinarySearchTree()
temp =''
data = input("Enter Input : ").split(" ")
for e in data:
    tree.create(int(e))
    print(search(tree.root,int(e),temp))

# printTree90(tree.root)