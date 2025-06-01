# def sum(a,b):
#     s=a+b
#     return s
# print(sum(4,8))

#print the lenght of the list
# def print_list(a):
#     print(len(a))

# print_list([1,2,3,4,5,6,7,8])

#print the list of element in single line 
def print_list(a=[1,2,3,4,5,6,7,8]):
    for el in a:
        print(el,end=" ")

print_list()