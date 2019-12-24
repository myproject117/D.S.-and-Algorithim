# Create a Matrix

# R=int(input("Enter no of rows"))
# C=int(input("Enter no of coloumns"))
# m=[]
# print('Enter values row wise')
# for i in range(R):
#     a=[]
#     for j in range(C):
#         a.append(int(input()))
#     m.append(a)
#
# for i in range(R):
#     for j in range(C):
#         print(m[i][j],end='   ')
#     print()





# Breadth First Search or Traversal(BFS) and Depth First Search(DFS) or Traversal Of a GRAPH......

# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph=defaultdict(list)
#     def insert(self,u,v):
#         self.graph[u].append(v)
#
#     def BFS(self,a):
#         visited=[False] * (len(self.graph)+1)
#         q=[]
#         q.append(a)
#         visited[a]=True
#         while(q):
#             s=q.pop(0)
#             print(s,end=' ')
#             for i in self.graph[s]:
#                 if (visited[i]==False):
#                     q.append(i)
#                     visited[i]=True
#
#     def DFSUtil(self,b,visit):
#         visit[b] = True
#         print(b,end=" ")
#         for j in self.graph[b]:
#             if (visit[j] == False):
#                 self.DFSUtil(j,visit)
#
#     def DFS(self,b):
#         visit = [False] * (len(self.graph)+1)
#         self.DFSUtil(b,visit)
#
#
# A=Graph()
# A.insert(1,2)
# A.insert(1,3)
# A.insert(2,4)
# A.insert(2,5)
# A.insert(3,3)
# A.insert(4,4)
# A.insert(5,6)
# A.insert(5,7)
# A.insert(6,6)
# A.insert(7,7)
#
# print('Breadth First Search/Traverse:')
# A.BFS(1)
# print()
# print('Depth First Search/Traverse:')
# A.DFS(1)









# Finding islands from a Graph using  Depth First Search (DFS) Algorithim..
# The graph is Input as a Matrix

# Princeple of DFS is "if aingle path is available then move ,
# till path become unavailable.. Then Explore other path of visited Node in Return time.."
# Here we use priceple of co-ordinate geometry, inorder to fird connections..

# class Graph:
#     def __init__(self, row, col, g):
#         self.ROW = row
#         self.COL = col
#         self.graph = g
#     def isSafe(self, i, j, visited):
#
#         return (i >= 0 and i < self.ROW and
#                 j >= 0 and j < self.COL and
#                 not visited[i][j] and self.graph[i][j])
#     def DFS(self, i, j, visited):
#         # These arrays are used to get row and
#         # column numbers of 8 neighbours
#         # of a given cell
#         rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
#         colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
#
#         visited[i][j] = True
#
#         for k in range(8):
#             if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
#                 self.DFS(i + rowNbr[k], j + colNbr[k], visited)
#     def countIslands(self):
#         visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
#         count = 0
#         for i in range(self.ROW):
#             for j in range(self.COL):
#                 if visited[i][j] == False and self.graph[i][j] == 1:
#                     self.DFS(i, j, visited)
#                     count += 1
#         return count
# graph = [[1, 1, 0, 0, 0],
#          [0, 1, 0, 0, 1],
#          [1, 0, 0, 1, 1],
#          [0, 0, 0, 0, 0],
#          [1, 0, 1, 0, 1]]
# row = len(graph)
# col = len(graph[0])
# g = Graph(row, col, graph)
# print("Number of islands is:")
# print(g.countIslands())
















# Creating a Binary Search Tree...
# Insertion in a BST

# class Node:                 # BST always Linked'ly Represented ...
#     def __init__(self,data):
#         self.left=None
#         self.data=data
#         self.right=None
#
# def insert(node,root):
#     if(root is None):
#         root=node
#     elif(node.data==root.data):
#         print(str(node.data) +' '+'is already present.Sequence is:')
#         return root
#     else:
#         if (node.data<root.data):
#             if(root.left is None):
#                 root.left=node
#             else:
#                 root.left=insert(node,root.left)
#         else:
#             if(root.right is None):
#                 root.right=node
#             else:
#                 root.right=insert(node,root.right)
#     return root
# def Inorder(root):
#     if (root):
#         Inorder(root.left)
#         print(root.data, end=' ')
#         Inorder(root.right)
#     return
# def Preorder(root):
#     if(root):
#         print(root.data,end=' ')
#         Preorder(root.left)
#         Preorder(root.right)
#     return
#
#
# # # Searching in BST...
#
# def BST_Search(key,root):
#     if (root is None or key is root.data):
#         return root
#     elif(key<root.data):
#         return BST_Search(key,root.left)
#     else:
#         return BST_Search(key,root.right)
#
# root=Node(30)
#
# insert(Node(20),root)
# insert(Node(25),root)
# insert(Node(40),root)
# insert(Node(35),root)
# insert(Node(10),root)
# insert(Node(50),root)
# insert(Node(90),root)
# print('Inorder Sorted Travrsal of BST:')
# Inorder(root)
# print()
# print('Preorder Traversal of BST:')
# Preorder(root)
# print()
# P=BST_Search(47,root)
# if P:
#     print("Found"+" "+str(P.data)+" "+"in sequence..")
# else:
#     print('Data not in sequence')




# Pair of element from sequence  A,B , such A+b < Target < A+B
# Former is Nearest Lesser pair and after is nearest Greater pair..

# def find(A,B,T):
#     G=[]
#     L=[]
#     for i in A:
#         for j in B:
#             p=i+j
#             if(p>T):
#                 G.append(p)
#             else:
#                 L.append(p)
#     g=min(G)
#     l=max(L)
#     for i in A:
#         for j in B:
#             q=i+j
#             if(q==g):
#                 print("Nearest greater pair:",i,j)
#             elif(q==l):
#                 print("Nearest lesser pair:",i,j)
#             else:
#                 pass
# A=[-1,3,8,2,9,5]
# B=[4,1,2,10,5,20]
# target=24
# find(A,B,target)


# Finding,the difference of each element of a sequence over each element other
# that makes them closer to Target ..
# So,if Target=24, then close to 23 or 25 is acceptable..

# def fun(A,B,T):
#     for i in B:
#         p=(T-1)-i
#         q=T-i
#         r=(T+1)-i
#         if p in A:
#             print(" "+str(i)+"      "+str(p)+" "+"->->"+" "+str(i+p))
#         if q in A:
#             print(" "+str(i)+"      "+str(q)+" "+"->->"+" "+str(i+q))
#         if r in A:
#             print(" "+str(i)+"      "+str(r)+" "+"->->"+" "+str(i+r))
#
#
# A=[22,3,20,2,19,5]
# B=[4,1,2,10,5,20]
# target=24
# print("B-seq  A-seq   Target")
# fun(A,B,target)











# Time Adjustment
# Enter Time in 12-hour format and get in 24-Hour Format..

# def fun(seq):
#     if "PM" in seq or "pm" in seq:
#         if(int(seq[:2])==12):
#             return seq[:8]
#         elif(int(seq[:2]) in range(1,12)):
#             p=int(seq[:2])+12
#             s=str(p)+seq[2:5]
#             return s
#         else:
#             return seq[:8]
#     elif "AM" in seq or "am" in seq:
#         if (int(seq[:2]) == 12):
#             k="00"+seq[2:5]
#             return k
#         elif(int(seq[:2]) in range(1,12)):
#             return seq[:5]
#         else:
#             return seq[:6]
#     else:
#         return seq[:5]
# print("Enter time in 12-Hour format with AM or PM and get time in 24-Hour format")
# print("--------------------------------------------------------------------------")
# seq=input("Enter time in 'HH:MM PM/AM' format:")
# if(int(seq[:2])<=23 and int(seq[3:5])<=59):
#     A=fun(seq)
#     print("Time in 24-Hour Format is:",A)
# else:
#     print('Invalid Time')








# Rotation of Single or Multiple Sequences..
# Enter how many sequences, you want to rotate as "Test Case is"
# Then provide no of element for each sequence and no of rotation want to perform.
# Enter the element of every sequence..(Enter value..)
# Check your element inserted and rotation provided
# Finally get the result..


# def fun(seq,L,j):
#     n=len(seq)
#     k=[]
#     if n==2:
#         for i in range(seq[0]):
#             p=int(input("Enter value"+" "+str(i+1)+" "+":"))
#             k.append(p)
#         L.append(seq[1])
#         print("Sequence and Rotation for case"+" "+str(j+1)+" "+"is:",k,",",seq[1])
#         return k
#
# a = int(input("Enter nuber of testcase:"))
# p=[]
# if(a==1):
#     print("Test case is:"+str(a))
#     print("------------------------------")
#     for i in range(2):
#         if i == 0:
#             m = int(input("Enter length of list:"))
#             p.append(m)
#         else:
#             n = int(input("Enter number of rotation:"))
#             p.append(n)
# elif(a>1):
#     print("Test case is:"+str(a))
#     print("-------------------------------")
#     for i in range(a):
#         for j in range(2):
#             if j == 0:
#                 m = int(input("Length of list for test" + " " + str(i+1) + " " + ":"))
#                 p.append(m)
#             else:
#                 n = int(input("Rotation of list for test" + " " + str(i+1) + " " + ":"))
#                 p.append(n)
# else:
#     pass
# import time
# l=len(p)
# y=0
# z=2
# T=[];L=[]
# for j in range(l//2):
#     A=fun(p[y:z],L,j)
#     T.append(A)
#     y+=2
#     z+=2
# print("Wait for 5 sec..")
# time.sleep(5)
# print("Here the result..")
# print()
# print("Input:")
# print("-----------------------------")
# for i in range(len(T)):
#     print(T[i],",", L[i])
# print()
# print("Output:")
# print("-----------------------------")
# for j in range(len(T)):
#     print(T[j][L[j]:] + T[j][:L[j]])








