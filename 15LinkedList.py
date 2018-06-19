class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data)
            current = current.next

    def insert(self,head,data):
        current = head
        if current is None:
            head = Node(data)
        elif current.next is None:
            current.next = Node(data)
        else:
            self.insert(current.next,data)
        return head


    # Complete this method


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head);