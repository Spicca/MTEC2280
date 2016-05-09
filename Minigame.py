import sys
import random
import serial

ser = serial.Serial("/dev/cu.usbmodem1421", 9600)
print(ser.name)

Hstate = 0


def win():
    global Hstate
    if(foeHP == 0 or foeHP<=0):
        print("YOU DEFEATED THE ORC! \n")
       
        print("You moved to the next room.")
        Hstate=Hstate+1
        print("You are in: " and Hstate)
        room() 
        

def lose():
    global Hstate
    if(HP == 0 or HP<=0):
        print("YOU HAVE BEEN DEFEATED! \n")
    
        print(Hstate + "This was your position \n")

        print("You lost, you have been return to the beginning of the dungeon.")

        start()
        Hstate=0


def start(): 
    global Hstate
    print("WELCOME TO THE MINIGAME \n Follow the given instructions to make it to the end of the map. \n There is 5 rooms to complete \n But be weary of time! \n enjoy! \n\n\n\n")
    Hstate=Hstate+1

def minigame1():
	global Hstate
	if(Hstate==1):
		print("Create a blackout by covering the light sensor!")
		Hstate=Hstate+1
def minigame2():
	global Hstate
	if(Hstate==2):
		print("Quickly enter the number of LED's that displayed!")
		Hstate=Hstate+1
def minigame3():
	global Hstate
	if(Hstate==3):
		print("Guess the distance between the Arduino and the wall (millimeters)")
		Hstate=Hstate+1
def minigame4():
	global Hstate
	if(Hstate==4):
		print("Make it hot!")
		Hstate=Hstate+1
def minigame5():
	global Hstate
	if(Hstate==5):
		print("Find and press the button that will save you!")
		Hstate=Hstate+1


while(True):

	start()
	if(ser.inWaiting() > 0):
		s = ser.readline()
		s = s.strip()
		s = s.decode("utf-8")
		minigame1()
		if(s == "Complete 1"):
			print(s)
			print("Well Done")
			minigame2()
		elif(s == "Complete 2"):
			print(s)
			print("Well Done")
			minigame3()
		elif(s == "Complete 3"):
			print(s)
			print("Well Done")
			minigame4()
		elif(s == "Complete 4"):
			print(s)
			print("Well Done") 
			minigame5()  
		else:
			print(s)
			print("Well Done")
			message = "0" + "\n"
			message = message.encode()
			ser.write(message)

ser.close()










    
    

               

   