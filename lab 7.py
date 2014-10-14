x = 1
while (x < 300):
    print x
    x = x + 2
    

myList = [1,2,3,4,5,6,7,8,9,10]
index = 0
while (index < len(myList)):
    print myList[index]
    index = index + 1
    
    
import random
rand = random.randint(0,50)
keepGoing = False
while (keepGoing == False):
    print 'guess a number from 0 to 50'
    userInput = int(raw_input())
    if userInput > rand:
        print 'too high'
    elif userInput < rand:
        print 'too low'
    elif userInput == rand:
        print 'correct!!'
        keepGoing = True