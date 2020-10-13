import os
import defaultPath as dp

def getNumFilesWithExt(fileExt, pathToSearch="None"):
    print("Counting files... Please wait...")
    count = 0
    # If user not send any path to search, program will call to function that will set default path per Operation System
    if pathToSearch == "None":
        pathToSearch = dp.setDefualtPath()

    for root, dirs, files in os.walk(pathToSearch):
        for file in files:
            if file.endswith(fileExt.upper()) or file.endswith(fileExt.lower()):
                count += 1

    return count