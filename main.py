import pathByName
import numFilesWithExt
import copyToWorkDirectory
import findDuplicates
import os

while 1:
    print("Please choose operation to run:")
    print("\t1. Find a file path by file name.")
    print("\t2. Count the number of files with a specific extension.")
    print("\t3. Find duplicate files.")
    print("\t4. Copy a specific file to the work directory")
    operationToRun = int(input("Please enter your choise: "))
    if (operationToRun not in range(1,5)):
        print("Please choose operation from the list (1-4)")
    else:
        if operationToRun == 1:
            fileName = input("Please enter file name to search: ")
            workingPath = input("Please enter path to search (Leave empty to search everywhere)")
            if not workingPath:
                print(pathByName.getPathByName(fileName))
                break
            else:
                print(pathByName.getPathByName(fileName, workingPath))
                break
        elif operationToRun == 2:
            fileExt = input("Please enter extension to search: ")
            workingPath = input("Please enter path to search (Leave empty to search everywhere)")
            if not workingPath:
                print("There is #", numFilesWithExt.getNumFilesWithExt(fileExt), "files ending with ", fileExt)
                break
            else:
                print("There is #", numFilesWithExt.getNumFilesWithExt(fileExt), "files ending with ", fileExt, "in:", workingPath)
                break
        elif operationToRun == 3:
            workingPath = input("Please enter path to search (Leave empty to search everywhere)")
            if not workingPath:
                findDuplicates.findDup()
            else:
                findDuplicates.findDup(workingPath)
                break
        elif operationToRun == 4:
            fileToCopy = input("Please enter full file path: ")
            copyToWorkDirectory.copyFileToWorkDirectory(fileToCopy)
            break