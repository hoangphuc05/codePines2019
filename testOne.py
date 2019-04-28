import requests
import glob, os
from collections import defaultdict
from functools import partial

PATH = "test.html"
r = requests.get("http://catalog.whitworth.edu/undergraduate/mathcomputerscience/")


f = open(PATH, "w")
f.write(r.text)

whitworth = r.text
loc = whitworth.find('"courseblock"')

className = defaultdict(lambda: defaultdict(list))


while loc != -1:
    print(whitworth[loc+50:loc+56])
    fullName = whitworth[loc+50:loc+56]
    print(fullName[:2])
    print(fullName[3:])
    loc = whitworth.find('"courseblock"', loc+1)

    if fullName[:2] in className:
        if int(fullName[3:]) in className[fullName[:2]]:
            print("Repeated!")
        else:
            className["Major 1"][fullName[:2]].append(int(fullName[3:]))
    else:
        try:
            className["Major 1"][fullName[:2]].append(int(fullName[3:]))
        except:
            print("fail")


print(className.items())


