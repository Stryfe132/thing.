import random

mydict = {'len()': "Returns the length of an object as an integer",
          'append': "Updates the list by adding objects to the list.",
          'def': "defines your own function",
          'int()' : "Return an integer object constructed from a number or string x, or return 0 if no arguments are given.",
          'input()' : "Allows for a user to enter a word",
          'tuples' : "A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets."
          }


def ShowTerms():
    terms = mydict.keys()
    print ("Here Are The List  Of Terms Currently Available:")
    print (terms)
    print (input("Press any key to contnue..."))
    AskUser()
    
def ABCOrder():
    for key in sorted(mydict.keys()):
        print ("%s: %s" % (key, mydict[key]))
    
def enteryourword():
      definition = input("What Definition Would you Like To See?:")
      print ("Here is the definition for", definition)
      print (mydict[definition])
      return

def randomizer():
    print (random.choice(list(mydict.items())))


def AskUser():
    while True:
        try:
            choice = int(input(
                "Do you want to: \n(1) Get a Random Definition From the List \n(2) Enter Your Own word \n(3) Show list in ABC Order \n(4) Show List of Terms"
                ))
        except ValueError:
            print ("Please input a number")
            continue
        if 0 < choice < 5:
        	thisdict = { 1 : randomizer, 2 : enteryourword, 3 : ABCOrder, 4 : ShowTerms}
        	thisdict[choice]()
        	break
        else:
          print ("That is not between 1 and 3! Try Again:")
          print ("you entered: {} ".format(choice))
        
    
AskUser()

