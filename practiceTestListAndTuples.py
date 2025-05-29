# user enter three fav movie name and create its list

list=[input("Enter Fav First Movie : "),input("Enter Fav Second Movie : "),input("Enter Fav Second Movie : ")]
print(list)

#list contains palindrom of elements

list1=[1,2,3,2,1]
list2=[1,"abc","abc",1]

list1Copy=list1.copy()
list1Copy.reverse()

# if(list1==list.reverse()):
#     print("List is Palindrom")    #this will not work
# else:
#     print("List is Not Palindrom")


if(list1==list1Copy):
    print("List is Palindrom")
else:
    print("List is Not Palindrom")

list2Copy=list2.copy()
list2Copy.reverse()

# if(list2==list2.reverse()):
#     print("List is Palindrom")     #this will not work
# else:
#     print("List is Not Palindrom")


if(list2==list2Copy):
    print("List is Palindrom")
else:
    print("List is Not Palindrom")