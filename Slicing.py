str="rushikesh"
a=str[1:5]
print(a)
print(str[3:],str[2:len(str)])
print(str[2:len(str[5])]) #nothing will print str[5]this will give char
print(str[-3:6])#nothing will print 

print(str[:6])   #[0:6]

# print(str[6:2]) does not work

#negative slicking -ve index

str = "rushikesh"
print(str[-6:-1]) #hikes    