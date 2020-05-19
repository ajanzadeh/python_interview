class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        print("selfdata::::",data)


    def insert(self,data):
            if self.data < data:
              if self.right == None:
                 print("DEBUG: Adding right (empty)", data)
                 self.right = Node(data)
              else:
                  self.right.insert(data)
            elif self.data > data:
              if self.left == None:
                  print("DEBUG: Adding left (empty)", data)
                  self.left = Node(data)
              else:
                  self.left.insert(data)


    def printValue(self):
        print(self.data)


    def printTree(self):
        print(self.data)
        if self.left:
            self.left.printValue()
         if self.right:
            self.right.printValue()
        print(">>>>>>>>>>>>>>>>>")
        if self.left:
            self.left.printTree()

        if self.right:
            self.right.printTree()

root = Node(0)
root.insert()
# root.insert(1)
# root.insert(20)
root.insert(20)

root.insert(1)
# root.insert(1)
# root.insert(20)
root.insert(2)

root.printTree()
