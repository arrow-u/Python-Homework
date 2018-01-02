#Input and Statistics
#Input for users
'''
name = input ('What is your name? ')
print('Your name is', name)
'''

import statistics

exList = [1,2,3,4,5,6,7,9 ,9]
x =  statistics.mean(exList)
print ('mean:',x)

x = statistics.median(exList)
print ('median:',x)

x = statistics.mode(exList)
print ('median:', x)

x = statistics.stdev(exList)
print ('standard deviation:', x)

x = statistics.variance(exList)
print ('variance:',x)

#import syntax
'''
The 'as" will allow you to shorten the name of each function. 
'''
import statistics as s
from statistics import mean as m ,stdev as s #allows you to only import that funtion

#you will be able to call statistics as s so you don't have to keep typing "statistics"

print('This is with imported syntax using mean:',m(exList))
print('This is with imported syntax using stdev:',s(exList))

'''
The "*" means you will import EVERYTHING from that package.
Keep in mind you will forfeit your ability to shorten the functions. 
'''

#Making Module (You made the module in "exampleModule.py"

import exampleModule

exampleModule.exampleFunc('test')

#errorHandling - Try and except
#Basically for trying errors and seeing what to fall back on if it does go wrong.

#Exception 
try:
    print('Running the try....')
    print(5+'5')
    
except Exception as e:
    print(str(e)) 
        
print('continuing the code')

#TypeError (also keep in mind you can run multiple excepts)
try:
    print('Running the try for any kind of error....')
    import mars #this module does not exist
    print('5'+z) # z is not defined
    
except TypeError as t:
    print('TypeError triggered')
    print(str(t)) #str = string, this is here to print out what is causing the error. 

except NameError as n:
    print('NameError triggered')
    print(str(n))

except Exception as e:
    print('General Exception')
    print(str(e))


#Input Errors
try:
    name=input('What is your name?')
    print(str(name))
    
except TypeError as t:
    print('TypeError triggered')
    print(str(t)) #str = string, this is here to print out what is causing the error. 

except NameError as n:
    print('NameError triggered')
    print(str(n))

except Exception as e:
    print('General Exception')
    print(str(e))



 
