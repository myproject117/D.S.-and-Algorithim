# Heap Insertion,Deletion and Sorting..

# Function to insert element in a HEAP format. (Here it is "Max Heap")
# Max Heap -- Node or parent always greater than descendants or child ..

def heapInsert(L,N):
    i=N
    temp=L[i]
    while(i>1 and temp>L[i//2]):
        L[i]=L[i//2]
        i=i//2
    L[i]=temp

def swap(L,a,b):
    L[a],L[b]=L[b],L[a]


# Function to delete from last element of sequence..

def heapDelete(L,N):
    for k in range(N-1,1,-1):
        x = L[1]
        L[1] = L[k]
        i = 1
        j = 2 * i
        while(j<k-1):
            if L[j+1]>L[j]:
                if L[1]<L[j+1]:
                    swap(L,1,j+1)
            elif L[1]<L[j]:
                swap(L,1,j)
            else:
                pass
            i=j
            j=2*j
        L[k]=x
    return L



if __name__=='__main__':
    L = [0,10, 20, 30, 25, 5, 40, 35] # start from "zero(0)",as travesing start from index-0,
    print('Given elements:')          # but we want index-1 element..
    print(L[1:])      # All element excluding index-0..
    N=len(L)
    for n in range(N):
        heapInsert(L,n)
    print('Converted to a Heap format:')
    print(L[1:])      # All element excluding index-0..
    t=len(L)
    heapDelete(L,t)
    print('Heap-Soted List after Deleting and Storing:')
    print(L[1:])      # All element excluding index-0..


# arr="stringcompare"
# ans=["" for _ in arr]
# print(ans)










# Insertion Sort using Linked List

# class Node:
#     def __init__(self,data):
#         self.prev=None
#         self.data=data
#         self.next=None
#
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.point=None
#         self.move=None
#     def insert(self,Data):
#         t=Node(Data)
#         if(self.head==None):
#             self.head=t
#             self.point=t
#             self.move=self.point
#         elif(self.point.data < t.data):
#             self.point.next=t
#             t.prev=self.point
#             self.point=t
#             self.move=self.point
#         elif(self.point.data > t.data):
#             while(self.move.data > t.data and self.move.prev != None):
#                 self.move=self.move.prev
#             if(self.move.prev != None):
#                 self.move.next.prev=t
#                 t.next=self.move.next
#                 self.move.next=t
#                 t.prev=self.move
#                 self.move=self.point
#             elif(self.move.data > t.data):
#                 self.head=t
#                 self.head.next=self.move
#                 self.move.prev=self.head
#                 self.head.prev=None
#                 self.move=self.point
#             else:
#                 pass
#     def printlist(self):
#         temp=self.head
#         while(temp):
#             print(temp.data,end=" ")
#             temp=temp.next
#
# A=LinkedList()
# A.insert(35)
# A.insert(45)
# A.insert(25)
# A.insert(75)
# A.insert(37)
# A.insert(20)
# A.printlist()


# M=int(input("Enter number of cases:"))
# N=2*M
# p=ord('a')
# B={}
# k=1
# while(k<N):
#     B[chr(p)]=input("No of elements for case:"+str(k-(k//2))+"::")
#     B[chr(p+1)]=input("Enter rotation for case:"+str(k-(k//2))+"::")
#     p+=2
#     k+=2
# # print(B)
# print("Inputs:")
# print("---------")
# p=ord('a')
# i=0
# print(M)
# while(i<N):
#     print(B[chr(p)],B[chr(p+1)])
#     p+=2
#     i+=2


# j=1
# for j in range(5):
#     print(j,end=" ")



# def fun(seq):
#
#
# l=len(B)
# y=0
# z=2
# T={}
# for j in range(l//2):
#     T[j+1]=fun(p[y:z])
#     y+=2
#     z+=2
# print(T[1])
# print([2])















