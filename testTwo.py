#https://stackoverflow.com/questions/960733/python-creating-a-dictionary-of-lists

import requests
import glob, os
from collections import defaultdict

#check if the department is in the list or not
#if not create one new, if there is, check if the class is in the list or not, if not add new, if already add to the repeated list
def addClass(majorName, fullName, className):
    if fullName[:2] in className[majorName]:
        if int(fullName[3:]) in className[majorName][fullName[:2]]:
            #print("Repeated! ",fullName)
            repeatedClass.append(fullName)
        else:
            className[majorName][fullName[:2]].append(int(fullName[3:]))
    else:
        try:
            className[majorName][fullName[:2]].append(int(fullName[3:]))
        except:
            print("fail")



PATH = "test2.html"
r = requests.get("http://catalog.whitworth.edu/undergraduate/mathcomputerscience/#majors_optionstext")

#write the html file
#this file is currently used for debugging only and have no impact to the application
f = open(PATH, "w")
f.write(r.text)

#print(r.text)#print to the console for debugging

#whitworth string stores the whole html file
whitworth = r.text

#should be thee start location of the major
startLoc = whitworth.find('"sc_courselist"')
#end location of the same major in the same major
endLoc = whitworth.find('"sc_courselist"', startLoc+1)

#location for the class name
classNameLoc = whitworth.find('onclick="return showCourse(this,', startLoc, endLoc)
#location for the major name
majorNameLoc = whitworth.find('"majors_optionstext">Requirements for a', startLoc, endLoc)

className = defaultdict(lambda: defaultdict(list))

repeatedClass = []
majorName = ""


while startLoc != -1:
    classNameLoc = whitworth.find('onclick="return showCourse(this,', startLoc, endLoc)
    #location for the major name
    majorNameLoc = whitworth.find('name="majors_optionstext">Requirements for a', startLoc, endLoc)

    #print (startLoc," Before")
    #print the name of the major, end when find the '<'
    if ( majorNameLoc != -1):
        print(whitworth[majorNameLoc+45:whitworth.find('<', majorNameLoc+45)])
        majorName = whitworth[majorNameLoc+45:whitworth.find('<', majorNameLoc+45)]
        while classNameLoc != -1 :

            #print(whitworth[classNameLoc+34:classNameLoc+40])#the full name
            fullName = whitworth[classNameLoc+34:classNameLoc+40]#the full name
            classNameLoc = whitworth.find('onclick="return showCourse(this,', classNameLoc+3, endLoc)#find the location for the next class name

            #check if the department is in the list or not
            #if not create one new, if there is, check if the class is in the list or not, if not add new, if already add to the repeated list
            addClass(majorName, fullName, className)

            

        #print (startLoc)
    startLoc = whitworth.find('"sc_courselist"', endLoc)
    #end location of the same major in the same major
    endLoc = whitworth.find('"sc_courselist"', startLoc+1)

print(className)
for x in className:
    print(x)
    for y in className[x]:
        #print(y)
        for z in className[x][y]:
            print(y,z)
#print(repeatedClass)
