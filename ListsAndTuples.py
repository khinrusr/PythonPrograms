#list
marks=[84,78,90,85]
students=["rushi",'mohit','archana']
lists=["rushi",56,99.999]

print(marks,students,lists)
print(type(marks),type(students),type(lists))
print(len(marks),len(students),len(lists))


marks[2]=95
students[2]='Mau'
print(marks,students,lists)

lists[1]="archana"
print(lists)

# lists[3]="test"  #list assignment index out of range
# print(lists)

#Slicing in list

marks=[55,66,77,88,99,4,6,88,33]

print(marks[2:4])
print(marks[:3])
print(marks[2:])
print(marks[1:len(marks)])
print(marks[-3:-1])
print(marks[-4:-2])


#methods of list
list=[3,5,1,7,4,9]
list.append(111)
print(list) #add element at the end 
list.sort()
print(list) #sort in accending order
list.sort(reverse=True)
print(list) #soert in decending order 
list.reverse()
print(list)  #reverse the list
list.insert(3,564)
print(list)
