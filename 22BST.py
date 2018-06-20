class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        leftcounter = 0
        rightcounter = 0
        if root.left is not None:
            leftcounter = 1 + self.getHeight(root.left)
        if root.right is not None:
            rightcounter = 1 + self.getHeight(root.right)
        if leftcounter >= rightcounter:
            return leftcounter
        else:
            return rightcounter


T = int(input())
myTree = Solution()
root=None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)