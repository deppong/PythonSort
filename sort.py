import os
import shutil

# initializations of different filetypes and their groupings
pwd = os.getcwd()
files = []
fTypes = ["images", "video", "text", "pdf", "software", "compressed", "random"]
images = [".png", ".jpg", ".jpeg"]
video = [".mp4", ".mov", ".webm"]
data = [".dat", ".tmp", ".dll"]
text = ".txt"
pdf = ".pdf"
software = [".exe", ".lnk", ".msi", ".jar" ".bat"]
compressed = [".zip", ".7zip", ".rar", ".7z"]

# store all files to a list
for fName in os.listdir(pwd):
    path = os.path.join(pwd, fName)
    if os.path.isdir(path):
        continue
    else:
        files.append(path)

# create folders for each filetype unless it already exists
for fType in fTypes:
    if os.path.isdir("./" + fType):
        continue
    else:
        os.mkdir("./" + fType)

# put every file into each folder by checking it's file extension
for file in files:
    destination = ""

    for end in images:
        if file.endswith(end):
            destination='./images'
            shutil.move(file, destination)
            break
        
    for end in data:
        if file.endswith(end):
            destination='./data'
            shutil.move(file, destination)
            break

    for end in video:
        if file.endswith(end):
            destination='./video'
            shutil.move(file, destination)
            break

    for end in software:
        if file.endswith(end):
            destination='./software'
            shutil.move(file, destination)
            break

    for end in compressed:
        if file.endswith(end):
            destination='./compressed'
            shutil.move(file, destination)
            break

    if file.endswith(text):
        destination='./text'
        shutil.move(file, destination)
        break

    if file.endswith(pdf):
        destination='./pdf'
        shutil.move(file, destination)
        break

    # if there was no match and it's not a python file put it in the random folder
    if destination == "":
        if file.endswith("py"):
            continue
        else:
            shutil.move(file, './random')
