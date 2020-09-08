import os
import shutil
from sys import platform

def copyFileToWorkDirectory(filePath):
    workingDirectory = os.getcwd()
    total, used, free = shutil.disk_usage(workingDirectory)
    # Check if the file source is exist
    if not os.path.isfile(filePath):
        print("The file", filePath, "isn't exist, please try again")
        return
    # Check if there is enough free space on dest
    if (os.path.getsize(filePath) > free):
        print("There is no free space to copy this file")
        return
    else:
        # Check what is the running platform to know the system command to use
        runningPlatform = platform
        if runningPlatform == "linux" or runningPlatform == "linux2" or runningPlatform == "darwin":
            fileName = filePath.rsplit('/', 1)
            os.system('cp ' + filePath + ' ' + workingDirectory)
        elif runningPlatform == "win32":
            fileName = filePath.rsplit('\\', 1)
            os.system('copy ' + filePath + ' ' + workingDirectory)
        # Check if file copy successfully
        if (os.path.isfile(workingDirectory + '/' + fileName[1])):
            print("The file: ", fileName[1], "was copy successfully to:", workingDirectory)
        else:
            print("Can't copy the file to", workingDirectory)
        return
