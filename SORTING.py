# SORTING (Insertion Sort)

# L=[11,4,5,20,2,1,9,10,8,3,7]
# # L1=[]
# N=len(L)
# for i in range(1,N):
#     var=L[i]
#     j=i
#     while (j>0 and L[j-1] > var):
#         L[j]=L[j-1]
#         j-=1
#     L[j]=var
# print(L)



# Multiply a factor to a sequence..

# def contains(factor,sequence):
#     for item in range(len(sequence)):
#         sequence[item]*=factor
#     return sequence
#
# A=contains(5,[1,2,3,4,5])
# print(A)



# NESTED Recursion

# def fun(n):
#     if (n>100):
#         return n-10
#     else:
#         return fun(fun(n+11))
#
# A=fun(200)
# print(A)



# Factorial using Recursion..

# def fun_add(n):
#     if n==1:
#         return 1
#     else:
#         return n+fun_add(n-1)
#
# A=fun_add(5)
# print(A)






# General form of Insertion,but not support in Python

# def insrt(index,x):
#     L=[1,2,3,4,5]
#     length=len(L)
#     i=length
#     while(index<i):
#         length += 1
#         L[i]=L[i-1]
#         i-=1
#     L[index]=x
#
#     print("List is:",L)
#     print("Length is:",length)
# insrt(3,15)





# Insertion of an item in a Sorted List..
#
# def insrt(L,value):
#    for i in range(len(L)):
#         if L[i]>value:
#             j=i
#             break
#    L= L[:j] + [value] + L[j:]    # Insertion using Slicing..
#    return L
#
# L=[1,2,4,5,6]
# n=3
# A=insrt(L,n)
# print(A)



# Insert in a Random List..

# def insrt(L,index,value):
#     L=L[:index] + [value] + L[index:]
#     return L
# Lst=[1,5,6,4,8]
# print(Lst)
# i=2
# n=20
# A=insrt(Lst,i,n)
# print(A)




# def Del(index,L):
#     l=len(L)
#     x=L[index]
#     i=index
#     while(i<l-1):
#         L[i]=L[i+1]
#         i+=1
#     l-=1
#     return L
# Lst=[1,2,7,5,9,4]
# print(Lst)
# n=3
# print(Del(n,Lst))






# Delete single or multiple elements from a list

# L=[1,2,4,5,6,7,8]
# index_list=[3]
# outputp=(map(int,index_list))
# print(outputp)
# s=[j for i,j in enumerate(L) if i not in index_list]
#
# print(s)

# a=['5']
# print(''.join(a))








# Swapping one or multiple element in a List..

# def Swap(A,x,y):
#     A[x],A[y]=A[y],A[x]  # Here access the the list using indexes..
#     # temp=x
#     # x=y
#     # y=temp
#     return A
#
# def SqSwap(x,L):
#     i=0
#     while(i<len(L)):
#         if (L[i]==x):
#             Swap(L,i,0)   # Here pass the List and swapping indexes
#             return i
#         i+=1
#     return -1
# Lst=[10,14,12,15,16,20]
# n=30
# print(SqSwap(n,Lst))
# print(Lst)
















# Merging two Sorted List of random Length..

# def Merging1(A,B):
#     i=0; j=0; k=0
#     C=[0]*16
#     l1=len(A); l2=len(B)
#     while(i<l1 and j<l2):
#         if(A[i]<B[j]):
#             C[k]=A[i]
#             i += 1; k += 1
#         elif(A[i]>B[j]):
#             C[k]=B[j]
#             j += 1; k += 1
#         else:
#             C[k] = A[i]
#             i += 1; k += 1
#     while(i<l1):
#         C[k]=A[i]
#         i += 1; k += 1
#     while (j < l2):
#         C[k] = B[j]
#         j += 1; k += 1
#     return C
# L1=[1,2,4,5,6,7,9,13,17,20]
# L2=[4,7,9,10,11,13]
# print(Merging1(L1,L2))




# def Merging2(A,l,mid,h):
#     i=l
#     j=mid+1
#     k=0
#     L=[0]*6
#     while(i<=mid and j<=h):
#         if(A[i]<A[j]):
#             L[k]=A[i]
#             i+=1
#             k+=1
#         else:
#             L[k]=A[j]
#             j+=1
#             k+=1
#     while(i<=mid):
#         L[k]=A[i]
#         i+=1
#         k+=1
#     while(j<=h):
#         L[k]=A[j]
#         j+=1
#         k+=1
#     return L
#
# A=[2,4,6,8,9,10]
# l=0
# h=len(A)-1
# mid=(l+h)//2
# print(Merging2(A,l,mid,h))


