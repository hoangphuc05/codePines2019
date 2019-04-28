#https://stackoverflow.com/questions/24656138/python-tkinter-attach-scrollbar-to-listbox-as-opposed-to-window

import requests
import glob, os
from collections import defaultdict
from tkinter import *
from tkinter.messagebox import*





className = defaultdict(lambda: defaultdict(list))
currentMajor = ""
currentGroup = 0
PATH = "database.txt"
#def readFile(classList, PATH = "database.txt"):
with open(PATH) as f:
    for line in f:
        #print(line)
        if line[:5] == "major":
            currentMajor = line[6:line.find('/')]
        #    print(currentMajor)
        
        elif line[:6] == "course":
            currentGroup = int(line[7:])
        #    print(currentGroup)
        elif line[:3] == "end":
            currentMajor = ""
        elif line[:10] == "suggested:":
            currentGroup = -1
        else:
            #print(line[:line.find('/')])
            className[currentMajor][currentGroup].append(line[:line.find('/')])

tkOption = []

for x in className:
    tkOption.append(x)
    print(list(className.keys()).index(x),x)

master = Tk()
master.title("Choose Majors")
master.minsize(500, 100)

master.columnconfigure(0, weight =1)
master.columnconfigure(1, weight =1)

major1 = StringVar(master)
major1.set(tkOption[0])
major2 = StringVar(master)
major2.set(tkOption[0])

choice1=""
choice2=""

fname = "backGround.gif"
bg_image = PhotoImage(file=fname)
# get the width and height of the image
w = bg_image.width()
h = bg_image.height()

panel = Label(master, image = bg_image)
panel.pack(side='top', fill='both', expand='yes')

l1 = OptionMenu(panel, major1, *tkOption)
#l1.grid(row=0, column=0)
l1.pack(side="left",anchor="nw")
l2 = OptionMenu(panel, major2, *tkOption)
l2.pack(side="right",anchor="ne")
#l2.grid(row=0, column=1)

def show():
    global choice1 
    choice1 = major1.get()
    global choice2
    choice2 = major2.get()
    master.destroy()
    

button = Button(panel, text="Show", command = show)
button.pack(side="bottom")

mainloop()
print("a",choice1)
print("b",choice2)

firstChoice = int(list(className.keys()).index(choice1))
secondChoice = int(list(className.keys()).index(choice2))


allClass = []
recommend = []

#for x in className[list(className)[firstChoice]]:
#print(className[list(className)[firstChoice]])

#while 

#print ("test print")
#print("First Major", className[list(className)[firstChoice]])
#print("second Major",className[list(className)[secondChoice]])
#print("All lasses:",allClass)

for classes in className[list(className)[firstChoice]][-1]:
    if classes in recommend:
        pass
    else:
        recommend.append(classes)
del className[list(className)[firstChoice]][-1]
for classes in className[list(className)[secondChoice]][-1]:
    if classes in recommend:
        pass
    else:
        recommend.append(classes)
del className[list(className)[secondChoice]][-1]


for classes in className[list(className)[firstChoice]][0]:
    if classes in allClass:
        pass
    else:
        allClass.append(classes)
del className[list(className)[firstChoice]][0]
for classes in className[list(className)[secondChoice]][0]:
    if classes in allClass:
        pass
    else:
        allClass.append(classes)
del className[list(className)[secondChoice]][0]

#print(allClass)
foundFlag = False
removeCount = 0

#print("First Major", className[list(className)[firstChoice]])
#print("second Major",className[list(className)[secondChoice]])
#print("All classes:",allClass)
#print("")

while className[list(className)[firstChoice]]:
    for group1 in list(className[list(className)[firstChoice]].keys()):
        for classes in className[list(className)[firstChoice]][group1]:
            if classes in allClass:
                className[list(className)[firstChoice]][group1].remove(classes)
            else:
                for group2 in list(className[list(className)[secondChoice]].keys()):
                    for otherClass in className[list(className)[secondChoice]][group2]:
                        if otherClass in allClass:
                            className[list(className)[secondChoice]][group2].remove(otherClass)
                        elif classes == otherClass and removeCount < group1 and removeCount < group2:
                            if classes in allClass:
                                className[list(className)[firstChoice]][group1].remove(classes)
                            else:
                                foundFlag = True
                                removeCount += 1
                                allClass.append(classes)
                                className[list(className)[firstChoice]][group1].remove(classes)
                                className[list(className)[secondChoice]][group2].remove(otherClass)
                    if foundFlag == True:
                        if ((group2-10)//10) == 0:
                            
                            #print(foundFlag,"Deleting", className[list(className)[secondChoice]][group2])
                            del className[list(className)[secondChoice]][group2]
                        else:
                            className[list(className)[secondChoice]][group2 - 10] = className[list(className)[secondChoice]][group2]
                            #print(foundFlag,"Decreasing", className[list(className)[secondChoice]][group2])
                            del className[list(className)[secondChoice]][group2]
                    foundFlag = False

        if foundFlag == False:
            allClass.append(className[list(className)[firstChoice]][group1][0])
            className[list(className)[firstChoice]][group1].remove(className[list(className)[firstChoice]][group1][0])
        if ((group1-10)//10) == 0:
            del className[list(className)[firstChoice]][group1]
        else:
            className[list(className)[firstChoice]][group1-10] = className[list(className)[firstChoice]][group1]
            del className[list(className)[firstChoice]][group1]

        foundFlag = False

#print("Second major",className[list(className)[secondChoice]])
while className[list(className)[secondChoice]]:
    #print("Second major",className[list(className)[secondChoice]])

    for group2 in list(className[list(className)[secondChoice]].keys()):
        allClass.append(className[list(className)[secondChoice]][group2][0])
        className[list(className)[secondChoice]][group2].remove(className[list(className)[secondChoice]][group2][0])
        #print("Second majorrrrr",className[list(className)[secondChoice]])
        if ((group2-10)//10) == 0:
            del className[list(className)[secondChoice]][group2]
        else:
            className[list(className)[secondChoice]][group2-10] = className[list(className)[secondChoice]][group2]
            del className[list(className)[secondChoice]][group2]

#print("Second major",className[list(className)[secondChoice]])
allClass.sort()
print(allClass)
#className = defaultdict(lambda: defaultdict(list))

main = Tk()
frame = Frame(main)
frame.pack()
main.title("Class list")

fname = "backGround.gif"
bg_image = PhotoImage(file=fname)
# get the width and height of the image
w = bg_image.width()
h = bg_image.height()

panel = Label(main, image = bg_image)
panel.pack(side='top', fill='both', expand='yes')


listNodes = Listbox(panel, width=20, height=20, font=("Helvetica", 12))
#listNodes.pack(side="left", fill="y")

scrollbar = Scrollbar(panel, orient="vertical")
scrollbar.config(command=listNodes.yview)
#scrollbar.pack(side="right", fill="y")
#listbox = Listbox(main, width = 50, height = 20, yscrollcommand=scrollbar.set)
#listbox.pack()

listNodes.config(yscrollcommand=scrollbar.set, width = 25)

for classes in allClass:
    listNodes.insert(END, classes)

def exit():
    main.destroy()

button = Button(panel, text="Exit", command = exit)
button.pack(side = "bottom")
listNodes.pack(side="left", anchor="w", fill="both", pady=25)
scrollbar.pack(side="right", fill="y")
mainloop()


