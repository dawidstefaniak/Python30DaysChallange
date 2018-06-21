import sys

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

    def levelOrder(self, root):
        if root is None: return
        queue = []
        queue.append(root)

        while queue:
            print(queue[0].data, end=" ")
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)