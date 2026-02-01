from array import *

val=array('i',[1,2,3,4,5,6,7,8,9])
for i in range(0,len(val)):
   print(val[i],end=" ")
print("\n")

for x in val:
   print(x,end =", ")
print("\n")

val.reverse()
for i in range(0,len(val)):
   print(val[i],end =" ,")


#insert new elements in an array
newval=array('i',[1,2,3,5,5,6,7,20])
for i in range(0,len(newval)):
   print(newval[i],end=" ")
print("\n")

newval.insert(2,50)

# #insert in last element
newval.append(200)

#modified and append
newval[2]=500

#copy array
copyArray=array(val.typecode,(x*3 for x in val))

#delete some of the index value using pop
copyArray.pop(3)

#delete last elements using pop without giving index
copyArray.pop()

# #delete specific fix elements using remove,eleemnts 15 removed
copyArray.remove(15)

for i in range(0,len(copyArray)):
   print(copyArray[i],end = " ")
print("\n")

#slicing properties used in array

val=array('i',[1,2,3,4,5,6,7])

#only print those numbers startting from index 2 and ended from 5 , index 5 is exluded
newval=val[2:5]
for i in range(0,len(newval)):
    print(newval[i],end =" ")
print("\n")

#only print elements starting from index 2 and last 3 elements not included
newval=val[2:-3]
for i in range(0,len(newval)):
    print(newval[i],end =" ")
print("\n")

#reverse elemets in an array
newval=val[::-1]
for i in range(0,len(newval)):
    print(newval[i],end =" ")
print("\n")


#finding the index of elemensts in an array

arr=array('i',[1,2,3,4,5,6])
val=arr.index(3)
print(val)