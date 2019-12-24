# ARRAY OPERATIONS


# Find maximum value of a List/Arrya
# def max(A):
#     x=A[0]
#     i=0
#     while(i<len(A)):
#         if(A[i]>x):
#             x=A[i]
#         i+=1
#     return x


# Find minimum value of a List/Arrya
# def min(A):
#     x=A[0]
#     i=0
#     while(i<len(A)):
#         if(A[i]<x):
#             x=A[i]
#         i+=1
#     return x

# Get the element at a particular Index in a LIst...
# def get(index,A):
#     if(index>=0 & index<len(A)):
#         return A[index]


# Set an element at a particular Index in a LIst..
# def set(index,value,A):
#     if(index>=0 & index<len(A)):
#         A[index]=value
#         return A
# # Find sum of values in a List..
# def sum(A):
#     i=0
#     temp=0
#     while(i<=len(A)-1):
#         temp=temp+A[i]
#         i+=1
#     return temp

# Find average of List...
# def average(A):
#     i=0
#     temp=0
#     while(i<=len(A)-1):
#         temp=temp+A[i]
#         i+=1
#     return temp//len(A)


# Reverse a List and Checking a string is Pallendrome or not
# def Reverse(A):
    # i=0
    # j=len(A)-1
    # while(i<=j):
    #     temp=A[i]
    #     A[i]=A[j]
    #     A[j]=temp
    #     i+=1
    #     j-=1
    # i=len(A)-1
    # j=0
    # B=[0]*len(A)   # Declare a fix size of Blank List, but fille with Zeros...
#     while(i>=0):
#         B[j]=A[i]
#         j+=1
#         i-=1
#     p=0
#     while(p<len(B)-1):
#         if(A[p]==B[p]):
#             p+=1
#         else:
#             return 'Not a Pallendrom'
#
#     return 'Is a Pallendrome'




# def check_sorted(A):
#     i=0
#     while(i<len(A)-1):
#         if(A[i]<A[i+1]):
#             i+=1
#         else:
#             return 'Not sorted'
#     return 'Sorted'




# Sort List element,Negative elements at left and Positive elements at right side..
def Rearrange(A):
    l=0
    h=len(A)-1
    while(l<h):
        while(A[l]<0):
            l+=1
        while(A[h]>=0):
            h-=1
        if(l<h):
            temp=A[l]  # Swapping negative and positive elements..
            A[l]=A[h]
            A[h]=temp
    return A
L=[1,-2,3,4,-6,7,-5,10,-17,-25,18,-61]
print(Rearrange(L))


# L=[1,2,4,5,9]
# l=[0]*len(L)
# print(l)