# f=open("/Users/rushikeshkhinde/Desktop/pythonworkspace/PythonPrograms/demo.txt","r")
# # data=f.read() #read entire file
# # data=f.read(5) # first 5 char 
# line1=f.readline()  #read line by line
# print(line1)
# line2=f.readline()  #read line by line
# print(line2)
# f.close()

#Write to the file 

# file=open("/Users/rushikeshkhinde/Desktop/pythonworkspace/PythonPrograms/demo.txt","w")
# file.write("This the next line")  #overrite the data with new data

# file=open("/Users/rushikeshkhinde/Desktop/pythonworkspace/PythonPrograms/demo.txt","a")
# file.write("c ")  #appends at the end


#with sysntax
# with open("/Users/rushikeshkhinde/Desktop/pythonworkspace/PythonPrograms/demo.txt","r") as f:
#     d=f.read()
#     print(d)
#     f.close() #no need of this with will auto close the file


    # deleting the File
# import os
# os.remove("/Users/rushikeshkhinde/Desktop/pythonworkspace/PythonPrograms/demo.txt")