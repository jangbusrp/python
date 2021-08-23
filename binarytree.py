class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data) 
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    # def treeprint(self):
    #     if self.left:
    #         self.left.treeprint()
    #     print(self.data), 
    #     if self.right:
    #         self.right.treeprint()


    def treetraversal(self, root):
        tra = []
        if root:
            tra = self.treetraversal(root.left) 
            tra.append(root.data)
            tra = tra + self.treetraversal(root.right) 
        return tra


root = Node(20)
root.insert(12) 
root.insert(30)
root.insert(18) 
root.insert(50)  

print(root.treetraversal(root))      


print("hellp world")