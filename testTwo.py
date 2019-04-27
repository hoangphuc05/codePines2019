import requests
import glob, os
from collections import defaultdict

PATH = "test2.html"
r = requests.get("http://catalog.whitworth.edu/undergraduate/mathcomputerscience/#majors_optionstext")


f = open(PATH, "w")
f.write(r.text)

print(r.text)


