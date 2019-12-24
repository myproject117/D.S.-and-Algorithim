# Line 1-to-50,defines Queue structure.. Which directly used in next applications..

# Structure to Store Queue data in a Node (Linked format)
class NodeQ:
    def __init__(self,data):
        self.data=data
        self.next=None

# Pointers to Traverse through Nodes to store data at desired position..
class Queue:
    def __init__(self):
        self.R=None
        self.F=None

    # def isFull(self):
    #     return self.T==None

    # Function to check the Queue is Empty or Not....
    def isEmpty(self):
        return self.F==None

    # Function to Insert element in the Queue
    def Enquque(self,x):
        T = NodeQ(x)        ##############################
        T.next=None
        if (self.F==None):
            self.F=self.R= T    ##############################
            return
        self.R.next = T
        self.R = T

    # Function to retrieve or delete elements from Queue..
    def Dequeue(self):
        x=(-1)
        if self.isEmpty():
            print('Queue is empty')
        P=self.F
        self.F=P.next
        x=P.data
        del P
        if self.F==None:
            self.R=None
        return x

    # Function to Display the Queue after insertion..
    def DisplayQueue(self):
        temp=self.F
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next

# Class for defining the Node to store data of Tree. As every node stored in a Linked format..
class NodeTree:
    def __init__(self,data):
        self.lchild=None
        self.data=data
        self.rchild=None


# Class for defining the Structure of Tree....

# class Tree:
#     def __init__(self):
#         self.root=None
#     def Insert(self,x):
#         R=NodeTree(x)
#         R.lchild=R.rchild=None
#         # self.root=R
#         P=Queue()
#         P.Enquque(R)
#         while(not P.isEmpty()):
#             M=NodeTree(P.Dequeue())
#             x=int(input('Enter the left child'))
#             if(x!=0):
#                 T=NodeTree(x)
#                 T.lchild=T.rchild=None
#                 M.lchild=T
#                 P.Enquque(T)
#
#             y=int(input('Enter the right child'))
#             if(y!=0):
#                 T=NodeTree(y)
#                 T.lchild=T.rchild=None
#                 M.rchild=T
#                 P.Enquque(T)


# Function to return PreOrder Traversal sequence of a Tree..

def Preorder(root):
    # Recursive Method (for Preorder Traversal)

    if (root):
        print(root.data,end=' ')
        Preorder(root.lchild)
        Preorder(root.rchild)
    return



    # Iterative Method-1 (for Preorder Traversal)

    # if (root == None):
    #     return
    #
    # nodeStack = []
    # nodeStack.append(root)
    # while (len(nodeStack) > 0):
    #     node = nodeStack.pop()
    #     print(node.data,end=' ')
    #
    #     if node.rchild is not None:
    #         nodeStack.append(node.rchild)
    #
    #     if node.lchild is not None:
    #         nodeStack.append(node.lchild)



    # Iterative Method-2 (for Preorder Traversal)

    # c=root
    # stack=[]
    # while(c is not None or stack):
    #     if(c is not None):
    #         print(c.data,end=' ')
    #         stack.append(c)
    #         c=c.lchild
    #     else:
    #         c=stack.pop()
    #         c=c.rchild


def Inorder(root):
    # Recursive Method.

    if(root):
        Inorder(root.lchild)
        print(root.data,end=' ')
        Inorder(root.rchild)
    return


    # Iterative Method
    # c=root
    # stack=[]
    # while(c is not None or stack):
    #     if (c is not None):
    #         stack.append(c)
    #         c=c.lchild
    #     else:
    #         c=stack.pop()
    #         print(c.data,end=' ')
    #         c=c.rchild



# PostOrder Traversal of Tree..

def Postorder(root):
    # Recursive Method

    if(root):
        Postorder(root.lchild)
        Postorder(root.rchild)
        print(root.data,end=' ')
    return




    # Iterative Method-1(Using Single Stack)

    # c = root
    # stack = []
    # while (c is not None or stack):
    #     if (c is not None):
    #         print(c.data, end=' ')
    #         stack.append(c)
    #         c = c.rchild
    #     else:
    #         c = stack.pop()
    #         c = c.lchild




    # Iterative Method-2   (Using Double-Stack)

    # if root is None:
    #     return
    # c=root
    # s1=[]
    # s2=[]
    # s1.append(c)
    # while s1:
    #     p=s1.pop()
    #     s2.append(p)
    #     if p.lchild:
    #         s1.append(p.lchild)
    #     if p.rchild:
    #         s1.append(p.rchild)
    # while s2:
    #     node=s2.pop()
    #     print(node.data,end=' ')



    # Iterative Method-3  (Using Double-Stack)

    # s=[]
    # def peek(s):
    #     if len(s)>0:
    #         return s[-1]
    #     else:
    #         return 0
    # while(True):
    #     while(root):
    #         if(root.rchild):
    #             s.append(root.rchild)
    #         s.append(root)
    #         root=root.lchild
    #     root=s.pop()
    #
    #     if(root.rchild and root.rchild==peek(s)):
    #         s.pop()
    #         s.append(root)
    #         root=root.rchild
    #     else:
    #         print(root.data,end=' ')
    #         root=None
    #
    #     if(len(s)<=0):
    #         break





    # s=[]
    # while(True):
    #     while(root):
    #         s.append(root.data)
    #         root=root.lchild
    #     root=s.pop()
    #     if(root.data>0):
    #         s.append(-root.data)
    #         root=root.rchild
    #     else:
    #         print(root.data,end=' ')
    #         root=None
    #
    #     if(len(s)<=0):
    #         break



# The LevelOrder Traversal or Level by level traversal of the Tree...

def LevelOrder(root):
    stack=[]
    stack.append(root.data)
    # print(root.data)
    Q=Queue()
    Q.Enquque(root)
    while(not Q.isEmpty()):
        root=Q.Dequeue()
        # print(root.data,end=' ')
        if(root.lchild):
            stack.append(root.lchild.data)
            Q.Enquque(root.lchild)

        if(root.rchild):
            stack.append(root.rchild.data)
            Q.Enquque(root.rchild)

    for i in stack:
        print(i,end=' ')



# Count Number nodes in the Tree...

def CountNodes(root):
    # result=0
    if(root):
        x=CountNodes(root.lchild)
        y=CountNodes(root.rchild)
        # result+=x+y+1
        return x+y+1
    return 0


# Count Nodes having Two childs only...
def CountNodeOfTwoChild(root):
    if(root):
        x=CountNodeOfTwoChild(root.lchild)
        y=CountNodeOfTwoChild(root.rchild)
        if(root.lchild and root.rchild):
            return x+y+1
        else:
            return x+y
    return 0


# Finding HEIGHT of Tree...
def HeightOfTree(root):
    if(root):
        x = HeightOfTree(root.lchild)
        y = HeightOfTree(root.rchild)
        if(x>y):
            return x+1
        else:
            return y+1
    return 0

# Count only leaf of Child Nodes..

def CountLeafNode(root):
    if(root):
        x=CountLeafNode(root.lchild)
        y=CountLeafNode(root.rchild)
        if(root.lchild or root.rchild):
            return x+y
        else:
            return x+y+1
    return 0

# Count those Nodes having one or two leaf or descendants..

def CountNodeOfOneOrTwoLeaf(root):
    if(root):
        x=CountNodeOfOneOrTwoLeaf(root.lchild)
        y=CountNodeOfOneOrTwoLeaf(root.rchild)
        if(root.lchild or root.rchild):
            return x+y+1
        else:
            return x+y
    return 0


# Create TREE by Inserting Values..

if __name__=="__main__":  # Main Function
    k=int(input("Enter ROOT value of Tree or 0 for None:"))
    root=NodeTree(k)
    # root.lchild=root.rchild=None
    P=Queue()
    P.Enquque(root)
    while(not P.isEmpty()):
        M=P.Dequeue()
        x=int(input('Enter the left child of'+" "+str(M.data)+" "+"or 0 for None:"))
        if(x!=0):
            T=NodeTree(x)
            T.lchild=T.rchild=None
            M.lchild=T
            P.Enquque(T)

        y=int(input('Enter the right child'+" "+str(M.data)+" "+"or 0 for None :"))
        if(y!=0):
            T=NodeTree(y)
            T.lchild=T.rchild=None
            M.rchild=T
            P.Enquque(T)
    print()
    print("Diffrerent methods of Tree Traversing:")
    print("---------------------------------------")
    print('Preorder Traversing:')
    Preorder(root);print();print()
    print('Inorder Traversing:')
    Inorder(root);print();print()
    print('Postorder Traversing:')
    Postorder(root);print();print()
    print('Levelorder Traversing:')
    LevelOrder(root);print();print()
    print("Some more information:")
    print("-----------------------")
    print('Total number Nodes in the Tree is:',CountNodes(root))
    print('Number of Nodes having Two childs is:',CountNodeOfTwoChild(root))
    print('Height of the Tree is:',HeightOfTree(root))
    print("Number of Leaf Node is:",CountLeafNode(root))
    print('Number Nodes having One or Two leaf:',CountNodeOfOneOrTwoLeaf(root))




# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
#
# def printInorder(root):
#     if root:
#         printInorder(root.left)
#         print(root.val,end=' ')
#         printInorder(root.right)
#
#
# def printPostorder(root):
#     if root:
#         printPostorder(root.left)
#         printPostorder(root.right)
#         print(root.val,end=' ')
#
#
# def printPreorder(root):
#     if root:
#         print(root.val,end=' ')
#         printPreorder(root.left)
#         printPreorder(root.right)
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# print("Preorder traversal of binary tree is")
# print(Preorder(root)
#
# print("\nInorder traversal of binary tree is")
# print(Inorder(root))
#
# print("\nPostorder traversal of binary tree is")
# print(Postorder(root))











