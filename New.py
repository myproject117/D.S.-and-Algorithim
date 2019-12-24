# Find The Missing Elements in an Un-Sorted List using HASH_TABLE......

# A=[3,7,12,9,6,1,4,2,10]
# l=1
# h=12
# n=len(A)
# H=[0]*13  # HashTable,which has indexes/length of Highest value in the given List...
# i=0
# while(i<n):
#     H[A[i]]+=1
#     i+=1
# print(H)
# j=1
# while(j<=len(H)-1):
#     if(H[j]==0):
#         print(j,end=', ')
#     j+=1





# Find The Missing Elements in a Sorted List using HASH_TABLE......

# A=[3,6,8,8,10,12,15,15,15,20]
# l=1
# h=12
# n=len(A)
# H=[0]*21  # HashTable,which has indexes/length of Highest value in the given List...
# i=0
# while(i<n):
#     H[A[i]]+=1
#     i+=1
# print('Hash Table:',H)
# j=1
# while(j<=len(H)-1):
#     if(H[j]>1):
#         print('{} appears {} times'.format(j,H[j]))
#     j+=1




# Find Repetation of Elements..

# A=[1,2,2,3,4,2,3,4,1,7,9,7]
# B={}
# for i in range(len(A)):
#     if (A[i] in B):
#         B[A[i]]+=1
#     else:
#         B[A[i]]=0
# print(B)





# A='madqm'
# P=A[::-1]
# if(P==A):
#     print("pallendrom")
# else:
#     print('Not a pallendrom')




# Matrix Operation

# L=[0]*5
# n=5
# def set(L,i,j,x):
#     if (i==j):
#         L[i-1]=x
#
# def get(L,i,j):
#     if (i==j):
#         return L[i-1]
#     else:
#         return 0
#
# def display(L):
#     for i in range(n):
#         for j in range(n):
#             if (i==j):
#                 print(L[i],end=' ')
#             else:
#                 print('0',end=' ')
#         print()
# for i in range(n):
#     set(L,int(input('Enter i')),int(input('Enter j')),int(input('Enter value')))
# print(get(L,2,2))
# print(display(L))




# POLYNOMIAL

# coeff=[]
# expo=[]
# for i in range(4):
#     A = int(input('Enter'+' '+str(i+1)+'st coefficient'))
#     B = int(input('Enter' +' '+str(i + 1)+'st exponent'))
#     coeff.append(A)
#     expo.append(B)
# sum=''
# for j in range(4):
#    sum+='%dx^%d+'%(coeff[j],expo[j])
#
# print()
# print(sum[:(len(sum)-1)])







# POLYNOMIAL Addition

# co1=[3,2,5]; co2=[6,5,8,2,7]
# exp1=[4,2,0]; exp2=[4,3,2,1,0]
#
# sum1=''
# for i in range(len(co1)):
#     sum1+='%dx^%d+'%(co1[i],exp1[i])
# sum2=''
# for j in range(len(co2)):
#     sum2+='%dx^%d+'%(co2[j],exp2[j])
#
# print("Pol1:",sum1[:(len(sum1)-1)])
# print("Pol2:",sum2[:(len(sum2)-1)])
#
# sum = ''
# i=0
# j=0
# while(i<len(exp1) and (j<len(exp2))):
#     if (exp1[i]==exp2[j]):
#         cor=co1[i]+co2[j]
#         sum+='%dx^%d+' %(cor,exp1[i])
#         i+=1
#         j+=1
#     elif (exp1[i]>exp2[j]):
#         sum += '%dx^%d+' % (co1[i], exp1[i])
#         i+=1
#     else:
#         sum += '%dx^%d+' % (co2[j], exp2[j])
#         j+=1
#
# print("Addition:",sum[:(len(sum)-1)])




#
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class LinkedList:
#     def __init__(self):
#         self.head=None
#
#     def PrintList(self):
#         temp=self.head
#         while(temp):
#             print (temp.data,end=' ')
#             temp=temp.next
#
# llist=LinkedList()
#
# llist.head=Node(10)
# second=Node(20)
# third=Node(30)

# llist.head.next=second
# second.next=third
#
# llist.PrintList()






# Checking  Span

# A=[100,80,60,70,60,75,85]
# n=len(A)
# B=[]
# for i in range(n):
#     j=i-1
#     c=1
#     while (j>=0 and A[i]>=A[j]):
#         c+=1
#         j-=1
#     B.append(c)
# print(B)





# Closest(having minimum difference) element of an element, on Right side..
# A=[4,5,2,25,12,14,13,15]
# Q=0
# n=len(A)
# for i in range(n):
#     B=[]
#     for j in range(i+1,n):
#         if A[j]>A[i]:
#             p=A[j]-A[i]
#             B.append(p)
#     # print(B)
#     # print(Q)
#     if B:
#         Q = min(B)
#
#         S = A[i] + Q
#         print(str(A[i]) + "--->" + str(S))
#     else:
#         print(str(A[i]) + "--->" + str(-1))






# from queue import Queue,LifoQueue
# q=Queue(maxsize=5)
# L=LifoQueue(maxsize=5)
# print(L.qsize())
# L.put(1)
# L.put(1)
# L.put(1)
# L.put(1)
# L.put(1)
# while (not q.full()):

# print(L.qsize())
# print(L.full())
# print(q.empty())


# import collections
# def isEmpty(S):
#     if S:
#         return 0
#     else:
#         return 1
#
# def fun(A):
#     if isEmpty(A) :
#         return 0
#     else:
#         P=A.popleft()
#
#     R=fun(A)
#
#     if (P>R):
#         return P
#     else:
#         return R
#
# A=collections.deque([4,6,1,8,9,61,10,54,1])
# print('Max value is:',fun(A))



# def power(x,n):
#     if n==0:
#         return 1
#     else:
#         return x*power(x,n-1)
# p=power(5,4)
# print(p)

# Reversing a string using Head Recursion(Return time printing)..

# def Reverse(A):
#     if len(A)==0:
#         return 0
#     else:
#         temp=A[0]
#         Reverse(A[1:])
#         print(temp,end=' ')
# A=[4,3,6,2,1]
# Reverse(A)

# A='123456'
# def fun(A):
#     if len(A)==0:
#         return 0
#     else:
#         return ord(A[0])-ord('0')






# class NodeQ:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class Queue:
#     def __init__(self):
#         self.R=None
#         self.F=None
#
#     # def isFull(self):
#     #     return self.T==None
#
#     def isEmpty(self):
#         return self.F==None
#
#     def Enquque(self,x):
#         T = NodeQ(x)        ##############################
#         T.next=None
#         if (self.F==None):
#             self.F=self.R= T    ##############################
#             return
#         self.R.next = T
#         self.R = T
#     def Dequeue(self):
#         x=(-1)
#         if self.isEmpty():
#             print('Queue is empty')
#         P=self.F
#         self.F=P.next
#         x=P.data
#         del P
#         if self.F==None:    ##########################
#             self.R=None     ##########################
#         return x
#
#
#
# class NodeTree:
#     def __init__(self,data):
#         self.lchild=None
#         self.data=data
#         self.rchild=None
#
#


# Tree Traversing using  STACK..

# def Preorder(root):
#     if root is None:
#         return
#     R=root
#     nodeStack = []
#     nodeStack.append(R)
#     while (len(nodeStack)>0):
#         node = nodeStack.pop()
#         print(node.data, end=' ')
#         if node.rchild is not None:
#             nodeStack.append(node.rchild)
#         if node.lchild is not None:
#             nodeStack.append(node.lchild)

        # node = nodeStack.pop()
        # if(R!=None):
        #     print(R.data,end=' ')
        #     nodeStack.append(R)
        #     R=R.lchild
        # else:
        #     R=nodeStack.pop()
        #     R=R.rchild

        # if node.rchild != None:
        #     nodeStack.append(node.rchild)
        # if node.lchild != None:
        #     nodeStack.append(node.lchild)


            # def Inorder(root):
#     if(root):
#         Inorder(root.rchild)
#         print(root.data,end=' ')
#         Inorder(root.lchild)
#     return
# def Postorder(root):
#     if(root):
#         Postorder(root.rchild)
#         Postorder(root.lchild)
#         print(root.data,end=' ')
#     return

# A=NodeTree(10)
# A.lchild=A.rchild=None
# B=[]
# B.append(A)
# while(len(B)>0):
#     p=B.pop()
#     x=int(input('Enter left child'))
#     if(x!=0):
#         T=NodeTree(x)
#         # T.lchild=T.rchild=None
#         p.lchild=T
#         B.append(T)
#     y=int(input('Enter right child'))
#     if (y!=0):
#         T = NodeTree(y)
#         # T.lchild = T.rchild = None
#         p.rchild = T
#         B.append(T)
#
# print('Preorder Traversing')
# Preorder(A)
# print('Inorder Traversing')
# Inorder(A);print()
# print('Postorder Traversing')
# Postorder(A)



# class Minus:
#     def __init__(self,val):
#         self.val=val
#     def __neg__(self):
#         return self.val
# a=Minus(5)
# print(a.val)



