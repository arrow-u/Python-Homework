#Lists and Tuples
'''
Tuples are immutable and can never be changed once defined
'''
#Tuples
def example():
    return 15,19

a,b = example()

print(a)
print(b)

#Lists , FYI this is not an array, inherently python does not use arrays
#there is numpy array though
List=[1,2,3,4,5,6 ]
print('List:',List)
print("List's first 3rd number:", List[2])

#append
List.append(5) #adds 7 to the end of the list
print('List after append:', List)

#insert
List.insert(0,20) #adds 20 to a position on the list, in this case 0
print('List after insert:', List)

#remove
List.remove(20) #removes 20 if in the list, HOWEVER this will only remove the first instance of 20 and not ALL of them.  
print('List after remove:', List)

#index
print('Position of 5:', List.index(5)) #Gives position of 5 if in the List

#count
print("Number of 5's in List:", List.count(5)) #Gives the number of instances in List

#sort
List.sort() 
print("Sorted List:",List) #Sorts List from least to greatest

x=['Joe','Alfred','Sam','Jose','James','Batman']
print("Unsorted list of names:", x)

x.sort()
print("Sorted list of names:", x)

#reverse
x.reverse()
print('Reverse sort of names:',x)

