
# BUBBLE_SORTING Technique (Compare every two element and if 1st is greater than 2nd then SWAP..)
# N-element takes (N-1) phases..In Each phase one element Sorted..

# Sorting the elements from Last.. Like Bubble.
# def BubbleSort(L,n):
#
#     def swap(L,i,j):
#         L[i],L[j]=L[j],L[i]   # [4,1,6,7,9,6,10,25],
#     for i in range(n):        #                [4,1,6,7,6,9,10,25],
#         flag=0                #                               [4,1,6,6,7,9,10,25]..
#         j=0
#         while(j<n-1-i):
#             if(L[j]>L[j+1]):
#                 swap(L,j,j+1)
#                 flag=1
#             j+=1
#         if(flag==0):
#             break
#     return L
# L=[4,6,1,7,9,25,6,10]
# n=len(L)
# print('Given Dta:',L)
# print('Sorted Data:',BubbleSort(L,n))






# Insertion Sorting..(Insert element at sorted position)

# def InsertionSort(L,n):
#     for i in range(1,n):
#         j=i-1
#         x=L[i]
#         while(j>=0 and L[j]>x):
#             L[j+1]=L[j]
#             j-=1
#         L[j+1]=x
#     return L
# L=[4,6,1,7,9,25,6,10]
# n=len(L)
# print(InsertionSort(L,n))





# SElection SOrting...(Select a position and find the smallest-element for that position..)

# def SelectionSort(L,n):
#     for i in range(n-1):
#         k=i
#         for j in range(i,n):
#             if(L[j]<L[k]):
#                 k=j
#         L[i],L[k]=L[k],L[i]
#     return L
# L=[4,6,1,7,9,25,6,10]
# n=len(L)
# print(SelectionSort(L,n))


# Quick Sort-->(Method-1) Time = O(n logn)  and  Space = O(log n)

# Quick-Sorting and Partioning..
# Selecting an Element and finding the sorted-position for it.. (Opposite to Selection Sort)

def Partioning(L,l,h):
    pivot=L[h]
    i=(l-1)
    for j in range(l,h):
        if L[j]<pivot:   # Check if element is less than pivot,if so increase i and swap..
            i=i+1        # otherwise move to next element to check..
            L[i],L[j]=L[j],L[i]
    L[i+1],L[h]=L[h],L[i+1]
    return (i+1)

def QuickSort(L,l,h):
    if l<h:                 # Sorted Array
        P=Partioning(L,l,h) # Partioning at ->> Any end ->> Time-> O(n**2) (Worst Case)
        QuickSort(L,l,P-1)  # Partioning at->> Middle ->> Time-> O(nlogn) (Best Case)
        QuickSort(L,P+1,h)  # Un-Sorted Array

L=[50,10,60,30,80,90]       # Partioning at ->> Any end ->> Time->O(nlogn) (Bestt Case)
N=len(L)                    # Partioning at ->> Middle ->> Time->O(n**2) (Worst Case)
QuickSort(L,0,N-1)
print('Sorted array:')
# for i in range(N):
#     print(L[i],end=" ")

print(L)





# QuickSort-->Iteration method-2.. Time = O(n**2 log n)  Space = O(log n)

# Here "Pivot" is taken at Beginning.
# 'i' strts from 'low' and 'j' from 'high'. j-decrease and i-increase if i-value < Pivot and j-value > Pivot
# They stop if i-value > Pivot and j-value < Pivot.. Then swap between j and Pivot..
# def Swap(L,a,b):
#     L[a],L[b]=L[b],L[a]
# def Partioningg(L,l,h):
#     pivot=L[l]
#     i=l+1
#     j=h
#     while(i<=j):
#         while(L[i]<pivot or L[j]>pivot):
#             if(L[i]<pivot):
#                 i+=1
#             if(L[j]>pivot):
#                 j-=1
#         if(i<=j):
#             Swap(L,i,j)
#             i+=1
#             j-=1
#         else:
#             break
#     Swap(L,l,j)
#     return j
# def Quicksort(L,l,h):
#     if(l<h):
#         P=Partioningg(L,l,h)
#         Quicksort(L,l,P-1)
#         Quicksort(L,P+1,h)
#
# L=[10,40,60,29,12,35,76]
# N=len(L)
# Quicksort(L,0,N-1)
# print(L)




# First way of Merge-Sorting..

def Mergesort(A):
    if (len(A)>1):
        mid=(len(A))//2
        L=A[:mid]
        R=A[mid:]
        Mergesort(L)
        Mergesort(R)
        i=j=k=0
        while(i<len(L) and j<len(R)):
            if(L[i]<R[j]):
                A[k]=L[i]
                i+=1
            else:
                A[k]=R[j]
                j+=1
            k+=1

        while(i<len(L)):
            A[k]=L[i]
            i+=1
            k+=1
        while (j < len(R)):
            A[k] = R[j]
            j += 1
            k += 1
L=[2,5,1,3,10,7,8]
print('Given List:')
print(L)
Mergesort(L)
print("Merge Sorted List:")
print(L)







# Second method of MergeSort

def Merging2(A,l,mid,h):
    i=l
    j=mid+1
    k=0
    L=[0]*6
    while(i<=mid and j<=h):
        if(A[i]<A[j]):
            L[k]=A[i]
            i+=1
            k+=1
        else:
            L[k]=A[j]
            j+=1
            k+=1
    while(i<=mid):
        L[k]=A[i]
        i+=1
        k+=1
    while(j<=h):
        L[k]=A[j]
        j+=1
        k+=1
    return L

def Mergesort(A):
    p=2
    i=0
    while(p<=len(A)):
        while(i+p-1<len(A)):
            l=i
            h=i+p-1
            mid=(l+h)//2
            i=i+p
            T=Merging2(A, l, mid, h)
        p=p*2
    # if((p//2)<len(A)):
    #     Merging2(A,0,p//2,len(A)-1)
    return

A=[2,5,1,4,3,8,7,10]
print(Mergesort(A))
# print(A)













# import sys
# data=[]
# for k in range(21):
#     a=len(data)
#     b=sys.getsizeof(data)
#     print("Length:{0:3d};Size in Bytes:{1:4d}".format(a,b))
#     data.append(None)
# import array




# import ctypes

# class DynamicArray:
#     def __init__ (self):
#         # Create an empty array.
#         self._n = 0            # count actual elements
#         self._capacity = 1     # default array capacity
#         self._A = self._make_array(self._capacity)  # low-level array
#
#     def __len__(self): # Return nimber element stored in the array
#         return self._n
#
#     def getitem(self, k):
#         # Return element at index k.
#         if not 0 <= k < self._n:
#             raise IndexError('invalid index' )
#         return self._A[k]      # Retrieve from array..
#
#     def append(self, obj):
#         # ”””Add object to end of the array.”””
#         if self._n == self._capacity:  # not enough room
#             self._resize(2*self._capacity)  # so double capacity
#             self._A[self._n] = obj
#             self._n += 1
#
#     def _resize(self, c):  # nonpublic utitity
#         # ”””Resize internal array to capacity c.”””
#         B = self._make_array(c)      # new (bigger) array
#         for k in range(self._n):     # for each existing value
#             B[k] = self._A[k]
#         self._A = B                  # use the bigger array
#         self._capacity = c
#
#     def _make_array(self, c):  # nonpublic utitity
#         # ”””Return new array with capacity c.”””
#         return (c * ctypes.py_object)()  # see ctypes documentation
#
# P=DynamicArray()
# P.append(10)
# print(P)








#
# class GameEntry:
#     #Represents one entry of a list of high scores.
#
#     def __init__ (self, name, score,n):
#         self._name = name
#         self._score = score
#         self._n=n
#
#     def __len__(self):
#         return self._n
#
#     def get_name(self):
#         return self._name
#
#     def get_score(self):
#         return self._score
#
#     def __str__ (self):
#         return ('{0}, {1}'.format(self._name, self._score))
# A=GameEntry('Vikash',100,10)
# print(A.get_name())
# print(A.get_score())
# print(len(A))



# A=[[" "]*6 for j in range(3)]
# print(A)

# Z=list(map(lambda x:x**2,[1,2,3,4,5]))
# def fun(x):
#     if x%2==0:
#         return x
#
# p=[2,4,5,6,8,10]
# X=filter(fun,p)
# print(Z)
# print(list(X))



# def fun(L):
#     sum=0
#     for i in range(len(L)):
#         for j in range(len(L[i])):
#             sum+=L[i][j]
#     return sum
#
# L=[[1,2,3,4],[5,6,7,8]]
# print(fun(L))

# L=[[1,2,3,4],[5,6,7,8]]
# A=[sum(val for i in L for val in i)]
# print(A,end=' ')