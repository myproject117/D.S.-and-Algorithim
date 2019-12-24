# Method-1 (Time=>O(n), Space=> O(1)

# def Fibo(n):
#     n1,n2=0,1
#     count=0
#     if(n<=0):
#         print("Invalid input")
#     elif(n==1):
#         print(n1)
#     else:
#         while(count<n):
#             print(n1,end=" ")
#             n3=n1+n2
#             # Alter values
#             n1=n2
#             n2=n3
#             count+=1
# Fibo(10)




# Method-2 {Using Recursion and iteration} [Time=O(n),Space=O(n)]
def fibo(n):
    if(n<=1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
N=int(input("Enter no of elements:"))
if N<=0:
    print("Invald input! Enter positive value")
else:
    for i in range(N):
        print(fibo(i),end=" ")







# Method-3    {Using Recursion}        [ Time=>O(n),  Space=O(1) ]
# FIBONACCI sequence using Dynamic Programming and Memoigation

F={}
i=0
while(i<10):
    F[i]=(-1)
    i+=1
def fib(n):
    if (n<=1):
        F[n]=n
        return n
    else:
        if (F[n-2]==(-1)):
            F[n-2]=fib(n-2)           # MEMOISATION  --> Storing called value in a stack and using

        if (F[n-1]==(-1)):             # MEMOISATION  --> that value when called again directly..
            F[n-1]=fib(n-1)           # Avoiding calling of same value repeatedly.. So,Reduce ehe stack memory..

        return F[n-2]+F[n-1]
n=6
for i in range(n):
    print(fib(i),end=" ")
