# i=1
# while i<=5:
#     print('rushi')
#     i+=1

# while i<=5:
#     print('rushi',i)
#     i+=1

# j=5
# while j>=1:
#     print(j)
#     j-=1


#print num from 1 to 100 

# num = 1
# while num<= 100:
#     print(num)
#     num+=1

#print number from 100 to 1

# num1 = 100
# while num1>=1:
#     print(num1)
#     num1-=1

#print the multiplecation for table n 
# n = int(input("Number : "))
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1

# print the list using the list 
# list=[1,4,9,16,25,36,49,64,81,100]
# i=0
# print(list[i])
# while i<len(list):
#     print(list[i])
#     i+=1

# search number x in the tuple 
tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the number : "))
i=0
while i<len(tup):
    if(x==tup[i]):
        print("index :",i,"number :",tup[i])
    i+=1