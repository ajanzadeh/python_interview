class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        print("selfdata",data)


    def insert(self,data):

        if self.data:
            print("debug",self.data)
            if self.data < data:
              if self.right == None:
                 self.right = Node(data)
              else:
                  self.right.insert(data)
            elif self.data > data:
              if self.left == None:
                  self.left = Node(data)
              else:
                  self.left.insert(data)


        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

root = Node(10)
root.insert(9)
root.insert(8)
# root.insert(1)
# root.insert(20)
root.PrintTree()
