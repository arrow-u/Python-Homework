
#variables
x,y = 1 ,2
boolean=1
a,b ='Hello World','Double Quotes'
exampleList = [234,23,2,]

#functions
print(a+', '+b)
print('I am',5)
print('I\'m',5,'years old')
      
print('addition:',1+7)
print('subtraction:',1-7)
print('multiplcation:',1*7)
print('division:',1/7)
print(4**2)

#while loops
while boolean < 10:
    #boolean = boolean + 1
    print('boolean value:',boolean)
    boolean += 1
    
    '''
     multi line comment
    '''

    
#for loops
for x in exampleList:
    print(x)

#if else statements
if x>y:
    print('1 less than 2')
else:
    print('2 greather than 1')    

#writing to a file
writeMe = 'example text'

#1st param: name of file
#2nd param: intention, w = write, save = s append = a
saveFile = open ('exampleWrite.txt','w')
saveFile.write(writeMe)
saveFile.close()


#appending to a file
appendMe = 'random text'

saveFile= open('exampleFile.txt','a')
saveFile.write('\n') #Makes a new line everytime
saveFile.write(appendMe)
saveFile.close()

#reading from a file
readMe = open('exampleFile.txt','r').read();
split=readMe.split('\n')
print(split)

#readlines() will read each line in a file like split()



#Classes
class calc:

    def add(x,y):
        answer = x+y
        print(answer)
        
    def subtract(x,y):
        answer = x-y
        print(answer)

    def multiply(x,y):
        answer = x*y
        print(answer)

    def divide(x,y):
        answer = x/y
        print(answer)
    
        




    

                

