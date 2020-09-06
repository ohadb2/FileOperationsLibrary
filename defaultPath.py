from sys import platform

def setDefualtPath():
    runningPlatform = platform
    if runningPlatform == "linux" or runningPlatform == "linux2" or runningPlatform == "darwin":
        pathToSearch = '/'
    elif runningPlatform == "win32":
        pathToSearch = 'c:\\'
    return pathToSearch
