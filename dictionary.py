import random
import time

mydict = {'len()': "Returns the length of an object as an integer",
          'append': "Updates the list by adding objects to the list.",
          'def': "defines a function",
          'int()' : "Return an integer object constructed from a number or string x, or return 0 if no arguments are given.",
          'input()' : "Allows for a user to enter a word",
          'tuples' : "A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets."
          }

def ABCOrder1():
    ABCOrder2()
    time.sleep(1.5)
    print (input("Press any key to continue..."))
    AskUser()

def ABCOrder2():
    for key in sorted(mydict.keys()):
        print ("%s: %s" % (key, mydict[key]))


def ShowTerms():
    terms = mydict.keys()
    print ("Here Are The List  Of Terms Currently Available:")
    print (terms)
    time.sleep(1.5)
    print (input("Press any key to continue..."))
    AskUser()
        
def enteryourword():
      definition = input("What Definition Would you Like To See?:")
      print ("Here is the definition for" + definition + ":")
      print (mydict[definition])
      time.sleep(1.5)
      print (input("Press any key to continue..."))
      AskUser()
      
def randomizer():
    print (random.choice(list(mydict.items())))
    time.sleep(1.5)
    print (input("Press any key to continue..."))
    AskUser()

def ExitProgram():
    raise SystemExit

def AskUser():
    while True:
        try:
            choice = int(input(
                "Do you want to: \n(1) Get a Random Definition From the List \n(2) Enter Your Own word \n(3) Show list in ABC Order \n(4) Show List of Terms \n(5) Exit the Program"
                ))
        except ValueError:
            print ("Please input a number")
            continue
        if 0 < choice < 6:
        	thisdict = { 1 : randomizer, 2 : enteryourword, 3 : ABCOrder1, 4 : ShowTerms, 5 : ExitProgram}
        	thisdict[choice]()
        	break
        else:
          print ("That is not between 1 and 5! Try Again:")
          print ("you entered: {} ".format(choice))
          time.sleep(1.5)
        
    
AskUser()

