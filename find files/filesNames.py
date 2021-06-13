import os

path = "C:/Users/mrwan/Downloads/unity project"

txt = open("files.txt", "w")

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".cginc"):
        	txt.write(file + " linguist-detectable=false" + "\n")