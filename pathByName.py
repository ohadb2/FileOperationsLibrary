import os
import defaultPath as dp
import numpy as np


def getPathByName(fileName, pathToSearch="None"):
    print("Starting to search... Please wait...")
    # Setting numpy array to saving file paths
    filePaths = np.array([])

    # If user not send any path to search, program will call to function that will set default path per Operation System
    if pathToSearch == "None":
        pathToSearch = dp.setDefualtPath()

    for root, dirs, files in os.walk(pathToSearch):
        for name in files:
            if name == fileName:
                filePaths = np.append(filePaths, (os.path.abspath(os.path.join(root, name))))

    return filePaths
