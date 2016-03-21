import sys
import random

Hstate = 0
foeHP = 5
HP = 25
fight = 0
encounter = 0
bossHP=30

def win():
    global Hstate
    if(foeHP == 0 or foeHP<=0):
        print("YOU DEFEATED THE ORC! \n")
       
        print("You moved to the next room.")
        Hstate=Hstate+1
        print("You are in: " and Hstate)
        room() 

def finalwin():
    global Hstate
    global bossHP
    if(bossHP == 0 or bossHP<=0):
        print("YOU DEFEATED THE ORC BOSS! \n")
       
        print("You have finished the dungeon. Congradulations\n\n\n")

        print ("PLAY AGAIN\n\n\n\n")

        start()
        



def lose():
    global Hstate
    if(HP == 0 or HP<=0):
        print("YOU HAVE BEEN DEFEATED! \n")
    
        print(Hstate + "This was your position \n")

        print("You lost, you have been return to the beginning of the dungeon.")

        start()
        Hstate=0

def finallose():
    if(HP == 0 or HP<=0):
        print("YOU HAVE BEEN DEFEATED! \n")
    
        print(Hstate + "This was your position \n")

        print("You lost, you have been return to the beginning of the dungeon.")

        start()
        Hstate=0



def reset():
    global fight 
    fight = random.randrange(0, 10)
    global encounter
    encounter = 0

def boss():

    global fight 
    global HP
    global bossHP
    global encounter
    global player

        
    if(character == 0):
        
        print("-----------------------------------------------------------\n\n")
        print("The chief has appeard in front of you, will you fight or run?")
    
    player=input("You must fight! \n\n")
    if(player == "Fight"):
        
        roll=random.randrange(0, 5)
        roll2=random.randrange(0, 5)

            
        if(roll>roll2):
            print("YOU HIT THE ORC!")
            print("You hit: ")
            print(roll)
            print("Your foe hit: " )
            print(roll2)
            print("\n")
            bossHP = bossHP - roll
            print("Your HP: ")
            print(HP)
            print("The enemies HP: ")
            print(bossHP)
            print("\n")

            finalwin()
            
                        

        elif(roll<roll2):
            print("THE ORC HIT YOU!")
            print("You hit: \n")
            print(roll)
            print("Your foe hit: ")
            print(roll2)

            HP = HP - roll2
            print("Your HP: \n")
            print(HP)
            print("The enemies HP: ")
            print(bossHP)
            print("\n")

            finallose()

        else:
            print("The attack parried")

    else:
        print("-----------------------------------------------------------\n\n")
        print("A Human has appeard in front of you, will you fight or run?")
        player=input("You must fight! ('Fight') ")
        


    if(player == "Fight"):
            
        roll=random.randrange(0, 5)
        roll2=random.randrange(0, 5)


        if(roll>roll2):
            print("YOU HIT THE HUMAN!")
            print("You hit: ")
            print(roll)
            print("Your foe hit: " )
            print(roll2)
          
            bossHP = bossHP - roll
            print("Your HP: ")
            print(HP)
            print("The enemies HP: ")
            print(bossHP)
            print("\n")

            win()
                    
                            

        elif(roll<roll2):
            print("THE HUMAN HIT YOU!")
            print("You hit: ")
            print(roll)
            print("Your foe hit: ")
            print(roll2)
           
            HP = HP - roll2
            print("Your HP: ")
            print(HP)
            print("The enemies HP: ")
            print(bossHP)
            print("\n")

            lose()

        else:
            print("The attack parried")


    else:
        print("You successfully escaped! \n")
        print("Your position: " and Hstate)
        room()







def fighter():
    global fight 
    global HP
    global foeHP
    global encounter


    
    while(encounter == fight):
        
        if(character == 0):
            print("-----------------------------------------------------------\n\n")
            print("An orc has appeard in front of you, will you fight or run?")
            player=input("Fight or Run: \n\n")
        


            if(player == "Fight"):
        
                roll=random.randrange(0, 5)
                roll2=random.randrange(0, 5)

            
                if(roll>roll2):
                    print("YOU HIT THE ORC!")
                    print("You hit: ")
                    print(roll)
                    print("Your foe hit: " )
                    print(roll2)
                    print("\n")
                    foeHP = foeHP - roll
                    print("Your HP: ")
                    print(HP)
                    print("The enemies HP: ")
                    print(foeHP)
                    print("\n")

    
                    win()
                
                        

                elif(roll<roll2):
                    print("THE ORC HIT YOU!")
                    print("You hit: \n")
                    print(roll)
                    print("Your foe hit: ")
                    print(roll2)
                
                    HP = HP - roll2
                    print("Your HP: \n")
                    print(HP)
                    print("The enemies HP: ")
                    print(foeHP)
                    print("\n")

                    lose()

                else:
                    print("The attack parried")
            else:
                print("You successfully escaped! \n")
                print("Your position: " and Hstate)
                room()

        else:
            print("-----------------------------------------------------------\n\n")
            print("A Human has appeard in front of you, will you fight or run?")
            player=input("Fight or Run: ")
        


            if(player == "Fight"):
        
                roll=random.randrange(0, 5)
                roll2=random.randrange(0, 5)

            
                if(roll>roll2):
                    print("YOU HIT THE HUMAN!")
                    print("You hit: ")
                    print(roll)
                    print("Your foe hit: " )
                    print(roll2)
                  
                    foeHP = foeHP - roll
                    print("Your HP: ")
                    print(HP)
                    print("The enemies HP: ")
                    print(foeHP)
                    print("\n")
    
                    win()
                
                        

                elif(roll<roll2):
                    print("THE HUMAN HIT YOU!")
                    print("You hit: ")
                    print(roll)
                    print("Your foe hit: ")
                    print(roll2)
                   
                    HP = HP - roll2
                    print("Your HP: ")
                    print(HP)
                    print("The enemies HP: ")
                    print(foeHP)
                    print("\n")

                    lose()

                else:
                    print("The attack parried")


            else:
                print("You successfully escaped! \n")
                print("Your position: " and Hstate)
                room()

def start(): 
    global character
    global Hstate
    print("WELCOME TO DUNGEON RAID \n Follow the given instructions to make it to the end of the map. \n There is 8 rooms to raid \n But be weary of foes! \n enjoy! \n\n\n\n")

    character = input("Choose your character ('Orc' or 'Human'): ")

    if(character == "Orc"):
        character == 1
    else:
        character == 0


    print("\n\n\nYou have entered the dungeon do you wish to continue?")

    answer= input("'Yes' or 'No': " )
    Hstate=2
    while(answer == "Yes"):
        if(Hstate == 2):
            print("\nYou find yourself on a frozen lake, with corpses under the ice, and a large demon incased in lce overlooking you")
            room()
            reset()
            fighter()
            Hstate = Hstate+1
        elif(Hstate == 3):
            print("You enter a mouintian side, wHere a three head wyvern flies by")
            room()
            reset()
            fighter()
            Hstate=Hstate+1
        elif(Hstate == 4):
            print("You see a boat, near a boiling hot lake with people being pulled in as they scream for help")
            room()
            reset()
            fighter()
            Hstate=Hstate+1
        elif(Hstate == 5):
            print("after crossing the lake, you go over a steep hill, and see people left heavy bags of gold over the hill as they strugle to let go of the gold")
            room()
            reset()
            fighter()
            Hstate=Hstate+1
        elif(Hstate == 6):
            print("going down the hill you see a pit of dead bodys, and infront of you lies a three headed dog guarding a door")
            room()
            reset()
            fighter()
            Hstate=Hstate+1
        elif(Hstate == 7):
            print("You open the door, and find a large room, warm with a sweet smell, with men lying with women immobleized, you see a door far away, but the women will not let you leave")
            room()
            reset()
            fighter()
            Hstate=Hstate+1
        elif(Hstate == 8):
            print("You see nothing, you feel no wind, it's a white room, that goes on forever")
            room()
            reset()
            fighter()
            Hstate=Hstate+1
        elif(Hstate == 9):
            print("You come out of a bed of dirt, you are greeted with the frozen eyes of many people, and they all scream the samething, TRAITOR!")
            room()
            boss()
       
        else:
            start()

    
        
    
def room():
    answer=int
    global HP
    global Hstate
    global poison
    global potion

    print("You have entered the next room, would you like to look around? \n\n")

    answer= input("0 for yes | 1 for no: " )
    if(answer == 0):
        potion=random.randrange(0,4)
        poison=random.randrange(0,4)
        if(potion==0):
            print("\nThere is a potion on the floor, you feel revived\n\n")
            HP=HP+20
            reset()
            fighter()
            
                        
        elif(poison==1):
            print("\nThere is a poison on the floor, you feel sick\n\n")
            reset()
            fighter()
            
        else:
            answer=1
            print("\nThere is nothing in this room, you move on.\n\n")
    else:
        start()






answer=int
answer= input("\n\n\n\nStart? (0): ")
print("\n\n\n\n\n")



if(answer == 0):
    start()









    
    

               

   
