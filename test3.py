#https://stackoverflow.com/questions/960733/python-creating-a-dictionary-of-lists

import requests
import glob, os
from collections import defaultdict




def listClass(startLoc, whitworth, listStore):
    #startLoc = majorList[list(majorList)[firstChoice]]
    #endLoc = whitworth.find('"sc_courselist"', startLoc+1)
    endLoc = whitworth.find('"sc_courselist"', startLoc+1) 

    comment = ''
    commentLoc = whitworth.find('span class="courselistcomment"', startLoc) 
    #print (whitworth[commentLoc:commentLoc + 4])
    #while commentLoc != -1:
    #    comment.append(whitworth[commentLoc + 31:commentLoc + 35])
    #    commentLoc = whitworth.find('span class="courselistcomment"', commentLoc+1, endLoc)

    #print (comment)

    majorNameLoc = whitworth.find('name="majors_optionstext">Requirements for a', startLoc, endLoc)
    
    #print (whitworth[majorNameLoc+45:whitworth.find('<', majorNameLoc+45)])

    classNameLoc = whitworth.find('onclick="return showCourse(this,', startLoc, endLoc)
    #find and print the first comment
    commentLoc = whitworth.find('span class="courselistcomment"', startLoc, classNameLoc)

    courseGroup = 0
 
    #print("Locationnnnnn", commentLoc)
    if commentLoc != -1:
        comment = whitworth[commentLoc + 31:whitworth.find(" ", commentLoc+31)]
        #print(comment)
    else:
        commentLoc = startLoc

    #find the secind comment position
    commentLoc = whitworth.find('span class="courselistcomment"', commentLoc+1, endLoc)


    count = [0,0,0,0,0]
    changeFlag = False

    while classNameLoc != -1 :

        if classNameLoc > commentLoc and commentLoc != -1:
            changeFlag = True
            comment = whitworth[commentLoc + 31:whitworth.find(" ", commentLoc + 31)]
            #print(comment)
            commentLoc = whitworth.find('span class="courselistcomment"', commentLoc+1, endLoc)

        

        #print(whitworth[classNameLoc+34:classNameLoc+40])#the full name
        fullName = whitworth[classNameLoc+34:classNameLoc+40]#the full name
        #print(fullName)
        classNameLoc = whitworth.find('onclick="return showCourse(this,', classNameLoc+3, endLoc)#find the location for the next class name

        #check if the department is in the list or not
        #if not create one new, if there is, check if the class is in the list or not, if not add new, if already add to the repeated list
        #print(fullName)
        if (comment == "Core" and changeFlag == True):
            count[0] += 1 
            courseGroup = 0 
            changeFlag = False
        elif (comment == "One" and changeFlag == True): 
            count[1] += 1
            courseGroup = 10 + count[1]
            changeFlag = False
        elif (comment == "Two" and changeFlag == True): 
            count[2] += 1
            courseGroup = 20 + count[2]
            changeFlag = False
        elif (comment == "Three" and changeFlag == True):
            count[3] += 1 
            courseGroup = 30 + count[3]
            changeFlag = False
        elif (comment == "Four" and changeFlag == True): 
            count[4] += 1
            courseGroup = 40 + count [4]
            changeFlag = False

        listStore[courseGroup].append(fullName)

    #print (listStore)
        

    #for y in listStore:
    #    print(y)

PATH = "test3.html"
r = requests.get("http://catalog.whitworth.edu/undergraduate/mathcomputerscience/#majors_optionstext")

#write the html file
#this file is currently used for debugging only and have no impact to the application
f = open(PATH, "w")
f.write(r.text)

#whitworth string stores the whole html file
whitworth = r.text

#list all the course and ask to choose 
majorList = {}
#should be thee start location of the major
startLoc = whitworth.find('"sc_courselist"')
#end location of the same major in the same major
endLoc = whitworth.find('"sc_courselist"', startLoc+1)
#location for the major name
majorNameLoc = whitworth.find('"majors_optionstext">', startLoc, endLoc)
if (whitworth[majorNameLoc+45:majorNameLoc+46]) == '<':
    majorNameLoc = whitworth.find('"majors_optionstext">', majorNameLoc, endLoc)

firstMajor = defaultdict(list)
secondMajor = defaultdict(list)

while startLoc != -1:
    majorNameLoc = whitworth.find('name="majors_optionstext">', startLoc, endLoc)
    if majorNameLoc != -1:
        majorName = whitworth[majorNameLoc+45:whitworth.find('<', majorNameLoc+45)]
        majorList[majorName] = startLoc
    
    startLoc = whitworth.find('"sc_courselist"', endLoc)
    #end location of the same major in the same major
    endLoc = whitworth.find('"sc_courselist"', startLoc+1)

for i in range(len(majorList)):
    print(i, list(majorList)[i])
    #print("")
firstChoice = int(input("Choose 1st major to compare"))
secondChoice = int(input("Choose 2nd major to compare"))



listClass(majorList[list(majorList)[firstChoice]], whitworth, firstMajor)
listClass(majorList[list(majorList)[secondChoice]], whitworth, secondMajor)

allMajor = defaultdict(list)
allClass = []

toDel = -1

print ("test print")

print("First Major", firstMajor)
print("second Major",secondMajor)
print("All lasses:",allClass)
print("")
for classes in firstMajor[0]:
    if classes in allClass:
        print("")
    else:
        allClass.append(classes)
del firstMajor[0]
for classes in secondMajor[0]:
    if classes in allClass:
        print("")
    else:
        allClass.append(classes)
del secondMajor[0]


print(allClass)
foundFlag = False
removeCount = 0

print("First Major", firstMajor)
print("second Major",secondMajor)
print("All lasses:",allClass)
print("")

while firstMajor:
    for group1 in list(firstMajor.keys()):
        #print(firstMajor)
       # print("--------------")
        #print(group1)
        #print("++++++++++++++++++++")
        for classes in firstMajor[group1]:
            if classes in allClass:
                print(classes)
                firstMajor[group1].remove(classes)
            else:
                for group2 in list(secondMajor.keys()):
                    for otherClass in secondMajor[group2]:
                        if otherClass in allClass:
                            secondMajor[group2].remove(otherClass)
                        elif classes == otherClass and removeCount < group1 and removeCount < group2:
                            if classes in allClass:
                                firstMajor[group1].remove(classes)
                            else:
                                foundFlag = True
                                removeCount+=1
                                allClass.append(classes)
                                firstMajor[group1].remove(classes)
                                secondMajor[group2].remove(otherClass)
                            
                    
                    if ((group2-10)//10) == 0:
                        #print(firstMajor)
                        del secondMajor[int(group2)]
                    else:
                        secondMajor[group2 - 10] = secondMajor[group2]
                        del secondMajor[int(group2)]

        if foundFlag == False:

            allClass.append(firstMajor[group1][0])    
            firstMajor[group1].remove(firstMajor[group1][0])
        #delete the group of it is 1x
        if ((group1-10)//10) == 0:
            #print(firstMajor)
            del firstMajor[int(group1)]
        else:
            firstMajor[group1 - 10] = firstMajor[group1]
            del firstMajor[int(group1)]

        

        foundFlag = False

    print("First Major", firstMajor)
    print("second Major",secondMajor)
    print("All lasses:",allClass)
    print("")
        







#print(allClass)
print("--------")
print(secondMajor)
print("++++++++++")
print(allClass)



