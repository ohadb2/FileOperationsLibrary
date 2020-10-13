import hashlib
import os
import defaultPath as dp

def findDup(pathToSearch="None"):
    flagFoundDuplicates = 0
    # Create a dictionary to save md5 as key and filename as value
    md5OfFiles = {}
    # If user not send any path to search, program will call to function that will set default path per Operation System
    if pathToSearch == "None":
        pathToSearch = dp.setDefualtPath()
    for root, dirs, files in os.walk(pathToSearch):
        for name in files:
            md5Hash = hashlib.md5()
            try:
                workFile = open(os.path.abspath(os.path.join(root, name)), "rb")
            except PermissionError:
                pass
            except FileNotFoundError:
                pass
            except OSError:
                pass
            else:
                try:
                    content = workFile.read()
                except OSError:
                    pass
                else:
                    md5Hash.update(content)
                    digest = md5Hash.hexdigest()
                    # If the key already exist, add the filename to the list
                    if (digest in md5OfFiles.keys()):
                        md5OfFiles[digest].append(os.path.abspath(os.path.join(root, name)))
                    # If the key not exist create new list in the key and add the filename to the list
                    else:
                        md5OfFiles[digest] = []
                        md5OfFiles[digest].append(os.path.abspath(os.path.join(root, name)))


    # Check if any md5-key has more than 1 elements in his list (Mean: There is duplicates files)
    for v in md5OfFiles:
        if ((len(md5OfFiles[v])) > 1):
            flagFoundDuplicates = 1 # Turn the flag
            print("These #", len(md5OfFiles[v]), " files are duplicates: ", md5OfFiles[v])

    if flagFoundDuplicates == 0: # If the flag still down - There is no duplicates found
        print("There is no duplicates files")

    return

