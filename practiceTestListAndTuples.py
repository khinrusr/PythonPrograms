# user enter three fav movie name and create its list

list3=[input("Enter Fav First Movie : "),input("Enter Fav Second Movie : "),input("Enter Fav Second Movie : ")]
print(list3)

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


#count the no. of students with 'A' grade in the tuple

tup=("C","D","A","A","B","B","A")
print(tup.count("A"))

# store the abpve value in list and sort them from "A" to "D"

listSort=list(tup)
listSort.sort()
print(listSort)