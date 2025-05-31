# list=[1,2,3,4,5,6,7,8,9,0]

# for val in list:
#     print(val)
# else:
#     print("loop ended")

# str="Rushikesh"
# ele=input("Input the element : ")
# for val in str:
#     if(val==ele):
#         print("K is found")
#         break
#     print(val)
# else:
#     print("Element not found")


# print the element for the following list using for 
# list=[1,4,9,16,25,36,49,64,81,100]

# for el in list:
#     print(el)


# search for a element in tup
tup=(1,4,9,16,25,36,49,64,81,100)
ele=int(input("Input the element : "))
idx=0
for val in tup:
    if(val==ele):
        print(val,"is found at index",idx)
        break
    idx+=1
    print(val)
else:
    print("Element not found")