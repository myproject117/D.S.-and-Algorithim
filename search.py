# Binary Search using Iteration..

# def BinarySearch(A,n,key):
#     l=0
#     h=n-1
#     while(l<=h):
#         mid=(l+h)//2
#         if (key==A[mid]):
#             return mid
#         elif (key<A[mid]):
#             h=mid-1
#         else:
#             l=mid+1
#     return -1
# L=[1,4,5,6,7,9]
# t=len(L)
# print(BinarySearch(L,t,6))








# Binary Search using Recursion

# def RBinarySearch(A,l,h,key):
#     # l=0
#     # h=n-1
#     if(l==h):
#         if(A[l]==key):
#             return l
#         else:
#             return 0
#     else:
#         mid=((l+h)//2)
#         if (A[mid]==key):
#             return mid
#         elif (key<A[mid]):
#             return RBinarySearch(A,l,mid-1,key)
#         else:
#             return RBinarySearch(A,mid+1,h,key)
