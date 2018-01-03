'''
Author: Alfred Chan
Final python project
Student Grade System
1/1/18
'''

'''
IMPORTANT:
Put me in python's site packages or the import of this file will not work. 
'''

adminDict= {'python':'hello'}
studentDict={'joe': [89],'amanda':[90],'jam':[100]}
userDict={}
import statistics 

def main():
    while 1 is 1:
        adminPage()
    
def adminPage():
    username='null'
    password='null'
    tryAgain,pointer=0,0
    
    username=input('Username:')
    password=input('Password:')
    userDict[username]=password
    
    for pointer in adminDict:
           if pointer in userDict:
               print ('We found a match!')
               print ('Welcome', username,':3')
               tryAgain=1
               
    if tryAgain is 1:
       welcomePage()
    else:
        print('Invalid Password, will detonate in 5 seconds!')
    
def welcomePage():
    a = 0
    looper=1 #resets loop
    
    while looper is 1: #Will infinitely run until option 4 is typed in
        print('Welcome to Grade Central')
        print(' [1]-Enter Grades','\n',
              '[2]-Remove Student','\n',
              '[3]-Student Average Grades','\n',
              '[4]-Exit')
        
        try:
            a=int(input('What do you want to do today?'))
        except TypeError as t:
            print(str(t))
            print('Please only enter a number.')
        except Exception as e:
            print(str(e))

        if a < 1 or a > 4 :
            print('Those numbers are not valid, please enter another number.')

        elif a is 1:
            addGrade()

        elif a is 2:
            removeStudent()

        elif a is 3:
            avgGrade()

        elif a is 4:
            looper=exitGrade(looper)
            
    #END

        
# Asks for the name of student and appends a new grade
def addGrade():
    #local variables
    name = ''
    grade = 0

    #inputs
    name=input('Student Name:')
    try:
        grade=int(input('Grade:')) #casts input to integer

        print('adding grade...') #print

        #appends the grade to the key(student)
        studentDict[name].append(grade)

    except Exception as e:
        print('Error in addGrade()')
    
    print(studentDict)
    #END

# Asks for the student's name to remove from the system
def removeStudent():
    #local variable
    name=''

    #catches any invalid inputs such as numbers,mispelled names, nonexistent names
    try:    
        #takes input of student's name to remove
        name=input('What student to remove?')

        #deletes student's name from the dictionary
        del studentDict[name]
        print('removing student...')
    except Exception as e:
        print('Error in removeStudent()')

    #prints the dictionary
    print(studentDict)
    #END

#Will grab the average grade for each student
def avgGrade():
    #local variable
    name=''
    avg=0
    counter=0

    List=studentDict.values()

    for counter in studentDict: 
        avg = statistics.mean(studentDict[counter])
        name = counter
        print(name,':',avg)
    #END

#Will set the loop to false 
def exitGrade(data):
    data=0
    return data
    #END



    
