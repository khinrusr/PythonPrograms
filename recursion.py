# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# print(show(5))


#factorial
def factorial(n):
    if (n==0 or n==1):
        return 1
    return n * factorial(n-1)

print(factorial(9))