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

PATH = "test4.html"
path2 = "test41.html"
r = requests.get("http://catalog.whitworth.edu/undergraduate/mathcomputerscience/#majors_optionstext")
#write the html file
#this file is currently used for debugging only and have no impact to the application
f = open(PATH, "w")
f.write(r.text)

l = open(path2, "a+")

whitworth = r.text
i = 0
for line in whitworth.split("\n"):
    if '"sc_courselist"' in line and i == 0:
        #print(line)
        l.write(line+ "\n")

f2 = open("test411.html", 'a')
l.close()
l = open(path2, 'r')
content = l.readline()
print(content)
f2.write(content)

