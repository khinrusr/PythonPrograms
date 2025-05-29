info={
    "name" : "Rushi",
    "sub" : ["java","js","python"],
    "topics" : ("str","int","float"),
    "age" : 23,
    "marks" : 97.99,
    13:78,
    8.00:87,
    "is_adult":True
}

print(info)
print(type(info))   #'dict'

print(info["name"],info["age"])

info["age"]=25

print(info)

info["height"]=6.0
print(info)

null_dict={}

#nested dict

infoDist={
    "name":"rushi",
    "age":23,
    "score":{
        "math":23,
        "chem":25,
        "phy":{
            "ph1":34,
            "ph4":77,
            "current":{
                "test":78
            }
        }
    }
}

print(infoDist)
print(infoDist["score"]["phy"]["current"]["test"])

print(infoDist.keys())
print(type(infoDist.keys()))
print(list(infoDist.keys()))
print(list(infoDist["score"].keys()))

print(len(infoDist))
print(len(infoDist.keys()))

print(infoDist.values())
print(type(infoDist.values()))
print(list(infoDist.values()))

print(infoDist.items()) #dict_items([('name', 'rushi'), ('age', 23), ('score', {'math': 23, 'chem': 25, 'phy': {'ph1': 34, 'ph4': 77, 'current': {'test': 78}}})])
 

print(infoDist["name"])  #will work
print(infoDist.get("name"))  #will work

#non existing key
# print(infoDist["name11"])  #will give error
print(infoDist.get("name11"))  #will give None

infoDist.update({"city":"nashik","road":"tapovan"})
print(infoDist)

new_infoDist ={"river":"gadawari"}
infoDist.update(new_infoDist)
print(infoDist)

new_infoDist ={"name":"mau"}
infoDist.update(new_infoDist)  #if given existing key then it will update the existing key's value
print(infoDist)



#Set

nums={1,2,3,4,5,6,7,8,9,0}
set2={1,2,3,3,3,3} #this output will be {1,2,3} because its has unique value
tup=(1,2,3,4)
str_Set={"test","test1",tup,True}
null_set=set()

print(nums,set2,null_set,str_Set)
print(type(nums),type(set2),type(null_set),type(str_Set))
print(len(nums),len(set2),len(str_Set))
list1=list(str_Set)
print(list1)



set={1,2,3,4,5,6,7,8,9}

set.add(25)
set.add((25,1,2,3,44,33,22,11))
print(set)

set.remove(1)
print(set)

set11={"hello","test","python","java"}
print(set11.pop())

set22={1,2,3,4,5,6,7,8}

set33={1,2,33,44,5,6,77,88,99}

print(set22.union(set33)) #combines both set

print(set22.intersection(set33)) #gives common values