import pygame
pygame.init()
screenwidth=800
screenheight=800
screen=pygame.display.set_mode((screenwidth,screenheight))
#ive tried to use pygame but its not working so i give up



cat_attributes = {
    "intelligence": 10,
    "energy": 50,
    "weight": 30,
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name:")
colour=input("Enter Colour:")
speccount=0
able=True


# start the while loop
while True:
    # Finish the string below
    if cat_attributes['energy'] <= 10:
        able=False
        newchoice=input("Your cat is tired and can no longer play!(^-.-^)zzz... What would you like to do instead?(2) Train your cat(3) Feed your cat(4) Let your cat sleep(5)See your cat's stats OR X TO EXIT :")
        if newchoice == '2':
            cat_attributes["intelligence"]=cat_attributes["intelligence"]+10
            cat_attributes["energy"]=cat_attributes["energy"]-5
            print("Your cat has trained!(^O-O^)[^]")
            pass
        elif newchoice == '3':
            cat_attributes["energy"]=cat_attributes["energy"]+10
            cat_attributes["weight"]=cat_attributes["weight"]+5
            print("Your cat has eaten! (^>.<^)/^/<3")
        elif newchoice=="4":
            cat_attributes["energy"]=cat_attributes["energy"]+10
            print("Your cat has had a nice nap!(^>_>^)/^/...")
        elif newchoice == '5':
            print("Intelligence:",cat_attributes["intelligence"],
                  "Energy:",cat_attributes["energy"],
                  "Weight:",cat_attributes["weight"])
        elif newchoice == "X":
            break
        else:
            pass
    else:
        option = input("What would you like to do? (1) Play with your cat(2) Train your cat(3) Feed your cat(4) Let your cat sleep(5)See your cat's stats, OR X TO EXIT : ")
        if option == '1'and able==True :
            cat_attributes["energy"]=cat_attributes["energy"]-10
            cat_attributes["weight"]=cat_attributes["weight"]-2
            print("Your cat has played!(^.,.^)/^/<3")
            speccount=speccount+1
            pass
        elif option == '2':
            cat_attributes["intelligence"]=cat_attributes["intelligence"]+10
            cat_attributes["energy"]=cat_attributes["energy"]-5
            print("Your cat has trained!(^O-O^)[^]")
            pass
        elif option == '3':
            cat_attributes["energy"]=cat_attributes["energy"]+10
            cat_attributes["weight"]=cat_attributes["weight"]+5
            print("Your cat has eaten! (^>.<^)/^/<3")
        elif option=="4":
            cat_attributes["energy"]=cat_attributes["energy"]+10
            print("Your cat has had a nice nap!(^>_>^)/^/...")
        elif option == '5':
            print("Intelligence:",cat_attributes["intelligence"],
                  "Energy:",cat_attributes["energy"],
                  "Weight:",cat_attributes["weight"])
        elif option=="X":
            break
    
        else:
           pass

    # finish off the if statements below
    
        
        
    # elif ...
    