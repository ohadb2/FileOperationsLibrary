import pathByName
import numFilesWithExt
import copyToWorkDirectory
import findDuplicates

while 1:
    print("Please choose operation to run:")
    print("\t1. Find a file path by file name.")
    print("\t2. Count the number of files with a specific extension.")
    print("\t3. Find duplicate files.")
    print("\t4. Copy a specific file to the work directory")
    print("\t5. Exit")
    operationToRun = int(input("Please enter your choise: "))
    if (operationToRun not in range(1,6)):
        print("Please choose operation from the list (1-5)")
    else:
        if operationToRun == 1:
            fileName = input("Please enter file name to search: ")
            workingPath = input("Please enter path to search (Leave empty to search everywhere)")
            if not workingPath:
                print(pathByName.getPathByName(fileName))
            else:
                print(pathByName.getPathByName(fileName, workingPath))
        elif operationToRun == 2:
            fileExt = input("Please enter extension to search: ")
            workingPath = input("Please enter path to search (Leave empty to search everywhere)")
            if not workingPath:
                print("There is #", numFilesWithExt.getNumFilesWithExt(fileExt), "files ending with ", fileExt)
            else:
                print("There is #", numFilesWithExt.getNumFilesWithExt(fileExt, workingPath), "files ending with ", fileExt, "in:", workingPath)
        elif operationToRun == 3:
            workingPath = input("Please enter path to search (Leave empty to search everywhere)")
            if not workingPath:
                findDuplicates.findDup()
            else:
                findDuplicates.findDup(workingPath)
        elif operationToRun == 4:
            fileToCopy = input("Please enter full file path: ")
            copyToWorkDirectory.copyFileToWorkDirectory(fileToCopy)
        elif operationToRun == 5:
            print("Bye Bye...")
            break

