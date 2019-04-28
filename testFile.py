import requests
import glob, os
from collections import defaultdict





className = defaultdict(lambda: defaultdict(list))
currentMajor = ""
currentGroup = 0
PATH = "math_computer.txt"
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
        elif line[:10] == "suggested":
            currentGroup = -1
        else:
            print(line[:line.find('/')])
            className[currentMajor][currentGroup].append(line[:line.find('/')])


for x in className:
    print(list(className.keys()).index(x),x)


firstChoice = int(input("Choose 1st major to compare"))
secondChoice = int(input("Choose 2nd major to compare"))


allClass = []
recommend = []

#for x in className[list(className)[firstChoice]]:
print(className[list(className)[firstChoice]])

#while 

print ("test print")
print("First Major", className[list(className)[firstChoice]])
print("second Major",className[list(className)[secondChoice]])
print("All lasses:",allClass)

for classes in className[list(className)[firstChoice]][-1]:
    if classes in recommend:
        print("")
    else:
        recommend.append(classes)
del className[list(className)[firstChoice]][-1]
for classes in className[list(className)[secondChoice]][-1]:
    if classes in recommend:
        print("")
    else:
        recommend.append(classes)
del className[list(className)[secondChoice]][-1]


for classes in className[list(className)[firstChoice]][0]:
    if classes in allClass:
        print("")
    else:
        allClass.append(classes)
del className[list(className)[firstChoice]][0]
for classes in className[list(className)[secondChoice]][0]:
    if classes in allClass:
        print("")
    else:
        allClass.append(classes)
del className[list(className)[secondChoice]][0]

print(allClass)
foundFlag = False
removeCount = 0

print("First Major", className[list(className)[firstChoice]])
print("second Major",className[list(className)[secondChoice]])
print("All lasses:",allClass)
print("")

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
                            
                            print(foundFlag,"Deleting", className[list(className)[secondChoice]][group2])
                            del className[list(className)[secondChoice]][group2]
                        else:
                            className[list(className)[secondChoice]][group2 - 10] = className[list(className)[secondChoice]][group2]
                            print(foundFlag,"Decreasing", className[list(className)[secondChoice]][group2])
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

print("Second major",className[list(className)[secondChoice]])
while className[list(className)[secondChoice]]:
    print("Second major",className[list(className)[secondChoice]])

    for group2 in list(className[list(className)[secondChoice]].keys()):
        allClass.append(className[list(className)[secondChoice]][group2][0])
        className[list(className)[secondChoice]][group2].remove(className[list(className)[secondChoice]][group2][0])
        print("Second majorrrrr",className[list(className)[secondChoice]])
        if ((group2-10)//10) == 0:
            del className[list(className)[secondChoice]][group2]
        else:
            className[list(className)[secondChoice]][group2-10] = className[list(className)[secondChoice]][group2]
            del className[list(className)[secondChoice]][group2]

print("Second major",className[list(className)[secondChoice]])

print(allClass)
#className = defaultdict(lambda: defaultdict(list))