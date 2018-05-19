## fake os why not I'm bored

import time
import random
import winsound
import os

file=open("Files","r")
files=[]
optfile=["Folder: FakeOs32","Pic1 (389KB)","Pic2 (164KB)","Pic3 (35KB)","Halo 3 - Complete Soundtrack (@.^$B)","Folder: Studies (1.24GB","[DATA CORRUPT] (0.00B)"]
inside=file.readlines()
file.close()
filecontents=[]
for x in inside:
    x=x.rstrip('\n')
    filecontents.append(str(x))
for x in optfile:
    if x in filecontents:
        files.append(x)

if "Folder: FakeOs32" in files:
    corrupt = False
else:
    corrupt = True
    print("[MAJOR ERROR]")
    print("FAKEOS32 MISSING")
    print("RECALIBRATING SYSTEM...")

class app:

    def __init__(self,name,pos,last):
        self.name = name
        self.enabled = True
        self.pos=pos
        self.last = last

    def setlogo(self,l1,l2,l3):
        self.line1=l1
        self.line2=l2
        self.line3=l3

    def logo(self,line):
        if self.last == False:
            endn = '      '
        else:
            endn = '\n'
        if self.enabled == True:
            if line == 1:
                print(self.line1,end=endn)
            if line == 2:
                print(self.line2,end=endn)
            if line == 3:
                print(self.line3,end=endn)
            if line == 4:
                namer=self.name
                while len(namer)!=7:
                    namer=namer+" "
                print(namer,end=endn)

    def function(self,use):
        if use == self.name:
            appfunction(self.name)

def newline(news,tim):
    for x in range(news):
        print()
        if tim!=0:
            time.sleep(tim)

def appfunction(app):
    app=app.capitalize()
    if app == "Bong":
        print("Loading Bong Internet Search Engine...")
        rwait(1,2)
        print("[ERROR: CON. DOWN MINIGAME ERROR]")
        print("Internet connection required.")
        time.sleep(1)
        print("Try:")
        time.sleep(0.3)
        print("¤ Checking network cables")
        time.sleep(0.3)
        print("¤ Topping up your Dial-Up Modem")
        time.sleep(0.3)
        print("¤ Turning on you Dial-Up Modem")
        time.sleep(0.3)
        print("¤ Purchasing a High-Speed, 20KB/s FakeSoft® 112k Modem")
        time.sleep(5)
    elif app == "Fsn":
        print("Welcome to the FakeSoft® Social Network™.")
        time.sleep(2)
        print("Unfortunately, it seems a connection cannot be made.")
        time.sleep(3)
        print("This could be due to:")
        time.sleep(0.2)
        print("¤ Network errors")
        time.sleep(0.2)
        print("¤ Lack of funds on your Dial-Up Modem")
        time.sleep(0.2)
        print("¤ Your Dial-Up Modem being disabled")
        time.sleep(0.2)
        print("¤ Your current modem not being a FakeSoft® High-Speed 20KB/s")
        print("  FakeSoft® 112k Modem or a newer model",end='')
        time.sleep(5)
        print(", which is required")
        time.sleep(0.04)
        print("  for the usage of FakeSoft® Social Network™ as stated in,")
        time.sleep(0.04)
        print("  and agreed upon by the current user, the FakeSoft®")
        time.sleep(0.04)
        print("  Software and Hardware Operations Agreement. Usage of")
        time.sleep(0.04)
        print("  the FakeSoft® Social Network™ without strict adhereance")
        time.sleep(0.04)
        print("  to the FakeSoft® Social Network™ Software and Hardware")
        time.sleep(0.04)
        print("  Agreement could result in permanent termination of your")
        time.sleep(0.04)
        print("  connection and/or FakeSoft® Social Network™ Account")
        time.sleep(0.04)
        print("  and/or your FakeSoft® Operating System and accompanying")
        time.sleep(0.04)
        print("  Personal Computer device, regardless of manufacturer or")
        time.sleep(0.04)
        print("  legal/moral/ethical issues. Any removed data will be stored")
        time.sleep(0.04)
        print("  by FakeSoft®, including FakeSoft® Social Network™ Account")
        time.sleep(0.04)
        print("  details (username and password), recently sent emails,")
        time.sleep(0.04)
        print("  all existing files on this device, and any other data that")
        time.sleep(0.04)
        print("  the FakeSoft® Corporation deems fit. Your compliance with")
        time.sleep(0.04)
        print("  these events is non-negotiable. See FakeSoft® Social")
        time.sleep(0.04)
        print("  Network Software and Hardware Agreement for more details,")
        time.sleep(0.04)
        print("  or the FakeSoft® General Usage Agreement for all details.")
    elif app == "Files":
        print("Accessing Files...")
        time.sleep(3)
        for x in filecontents:
            print(x)
        chooser=True
        while chooser == True:
            filechoose = input("Choose a file to modify (type 'quit' to exit): ")
            if filechoose == "quit":
                break
            while filechoose not in filecontents:
                filechoose = input("Choose a file to modify: ")
            print("[ERROR: MODIFICATION UNAVAILABLE]")
            delet = input("Do you want to delete "+filechoose+"? (y/n): ")
            if delet == "y":
                file=open("Files","r")
                reader=file.readlines()
                file.close()
                file=open("Files","w")
                for line in reader:
                    if line != filechoose:
                        file.write(line)
                        print(line)
                print("File deleted.")
                file.close()

    else:
        print()
        print("App unrecognised.")
        print()
        time.sleep(2)


    home(user)

def appprint():
    for x in range(6):
        Bong.logo(x+1)
        FSN.logo(x+1)
        Files.logo(x+1)
        Email.logo(x+1)
        Usage.logo(x+1)
        Quit.logo(x+1)

def corrupter(string):
    first=list(string)
    random.shuffle(first)
    stringout = ''.join(first)
    return stringout

Bong = app("Bong",1,False)
Bong.setlogo("┌──┐   ","├──┴┐  ","└───┘  ")
if corrupt == True:
    first = corrupter("┌──┐   ")
    secnd = corrupter("├──┴┐  ")
    third = corrupter("└───┘  ")
    Bong.setlogo(first,secnd,third)

FSN = app("FSN",2,False)
FSN.setlogo("╔═══   ","╠══    ","╝      ")
if corrupt == True:
    first = corrupter("╔═══   ")
    secnd = corrupter("╠══    ")
    third = corrupter("╝      ")
    FSN.setlogo(first,secnd,third)

Files = app("Files",3,False)
Files.setlogo("┌─┐___ ","│     │","└─────┘")
if corrupt == True:
    first = corrupter("┌─┐___ ")
    secnd = corrupter("│     │")
    third = corrupter("└─────┘")
    Files.setlogo(first,secnd,third)

Email = app("Email",4,False)
Email.setlogo("  / __/"," / _/  ","/___/  ")
if corrupt == True:
    first = corrupter("  / __/")
    secnd = corrupter(" / _/  ")
    third = corrupter("/___/  ")
    Email.setlogo(first,secnd,third)

Usage = app("Usage",5,False)
Usage.setlogo("   ║   ","   ║   ","   ■   ")
if corrupt == True:
    first = corrupter("   ║   ")
    secnd = corrupter("   ║   ")
    third = corrupter("   ■   ")
    Usage.setlogo(first,secnd,third)

Quit = app("Quit",6,True)
Quit.setlogo("/¯¯¯¯¯\\","|  Q  |","\_____/")
if corrupt == True:
    first = corrupter("/¯¯¯¯¯\\")
    secnd = corrupter("|  Q  |")
    third = corrupter("\_____/")
    Quit.setlogo(first,secnd,third)

def rwait(a,b):
    wait=random.randint(a,b)
    time.sleep(wait)

print("Init bootup sequence.",end='')
for x in range(random.randint(1,10)):
    rwait(0,2)
    print('.',end='')
print('.')

winsound.PlaySound('load.wav',winsound.SND_ASYNC)

print("Loading OS...")
#░  #▓
def loadbar(le,ul):
    current=0
    prev=0
    while current+1<=le:
        rwait(0,ul)
        prev=current
        count=0
        for x in range(current):
            print('▓',end='')
            count=count+1
        meh=random.randint(1,3)
        if current+meh+1<=le:
            current=current+meh+1
        if current==prev:
            current=current+1
        smolcount=le-count
        for x in range(smolcount):
            print('░',end='')
        
        perc=float(count/le)
        perc=perc*100
        perc=round(perc,2)
        print("       ",str(perc)+"%")
        
    for x in range(le):
        print('▓',end='')
    print("       100.0%")
loadbar(25,2)

def logon():

    newline(50,0.02)

    winsound.PlaySound(None,winsound.SND_ASYNC)
    winsound.PlaySound('startup.wav',winsound.SND_ASYNC)

    if corrupt == False:
        print("▓▓▓▓▓▓▓▓    ▓▓▓    ▓▓    ▓▓ ▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓   ▓▓▓▓▓▓  ™")
        print("▓▓         ▓▓ ▓▓   ▓▓   ▓▓  ▓▓          ▓▓     ▓▓ ▓▓    ▓▓")
        print("▓▓        ▓▓   ▓▓  ▓▓  ▓▓   ▓▓          ▓▓     ▓▓ ▓▓")
        print("▓▓▓▓▓▓   ▓▓     ▓▓ ▓▓▓▓▓    ▓▓▓▓▓▓      ▓▓     ▓▓  ▓▓▓▓▓▓")
        print("▓▓       ▓▓▓▓▓▓▓▓▓ ▓▓  ▓▓   ▓▓          ▓▓     ▓▓       ▓▓")
        print("▓▓       ▓▓     ▓▓ ▓▓   ▓▓  ▓▓          ▓▓     ▓▓ ▓▓    ▓▓")
        print("▓▓       ▓▓     ▓▓ ▓▓    ▓▓ ▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓   ▓▓▓▓▓▓")
    if corrupt == True:
        print("fake os tm")
        for x in range(6):
            print()

    newline(10,0)
    print("[ERROR: LOGIN SCREEN SUBPROGRAM NOT DETECTED]")
    print("[LOGIN SCREEN REBUILD COMMENCING...]")
    newline(15,0)
    print("Welcome, user. Please input your credentials now:")
    user=input("Username: ")
    print("[ERROR: PASSWORD HIDE FAIL]")
    print("[ERROR: PASSWORD INPUT CANNOT INITIALISE]")
    time.sleep(1)
    print("Welcome,",user)
    time.sleep(2)

    return user

user=logon()

winsound.PlaySound(None,winsound.SND_ASYNC)


def home(user):

    newline(50,0.02)
    if corrupt == False:
        print("▓▓▓▓▓   ▓▓   ▓   ▓ ▓▓▓▓▓     ▓▓▓   ▓▓▓▓ ™")
        print("▓      ▓  ▓  ▓  ▓  ▓        ▓   ▓ ▓")
        print("▓▓▓▓  ▓    ▓ ▓▓▓   ▓▓▓▓     ▓   ▓  ▓▓▓▓")
        print("▓     ▓▓▓▓▓▓ ▓  ▓  ▓        ▓   ▓      ▓")
        print("▓     ▓    ▓ ▓   ▓ ▓▓▓▓▓     ▓▓▓   ▓▓▓▓")
    if corrupt == True:
        print(corrupter("▓▓▓▓▓   ▓▓   ▓   ▓ ▓▓▓▓▓     ▓▓▓   ▓▓▓▓ ™"))
        print(corrupter("▓      ▓  ▓  ▓  ▓  ▓        ▓   ▓ ▓"))
        print(corrupter("▓▓▓▓  ▓    ▓ ▓▓▓   ▓▓▓▓     ▓   ▓  ▓▓▓▓"))
        print(corrupter("▓     ▓▓▓▓▓▓ ▓  ▓  ▓        ▓   ▓      ▓"))
        print(corrupter("▓     ▓    ▓ ▓   ▓ ▓▓▓▓▓     ▓▓▓   ▓▓▓▓"))

    newline(5,0)
    
    appprint()

    newline(5,0)

    print("[ERROR: NO MOUSE INPUT DETECTED]")
    useapp = input("Please choose an application to use: ")

    appfunction(useapp)

    
home(user)
