import json
import glob




def AppendFiles(jsonfilesList):
    for file in glob.glob("*.json"):
        jsonfilesList.append(file)
    return jsonfilesList


def ReadFiles():
    jsonfileslist = []
    AppendFiles(jsonfileslist)
    print(jsonfileslist)

    for file in jsonfileslist:
        with open(file, ) as jsonFile:
            data = json.load(jsonFile)
        
        # id = data["id"]
    print(id)



def WriteFiles():
    
    jsonfilelist = []
    AppendFiles(jsonfilelist)

    # value = 5885

    name = "Name  #"
    slash = "/"
    gif = ".gif"

    for file in jsonfilelist:
        with open(file, 'r+') as jsonFile:
            data = json.load(jsonFile)
            data["edition"] = str(value)                         # <--- add 'id' value.
            data["name"] = name + str(value)
            data["image"] = slash + str(value) + gif
            jsonFile.seek(0)                           # <--- should reset file position to the beginning.
            json.dump(data, jsonFile, indent=4)
            jsonFile.truncate()  
        value += 1


#ReadFiles()
WriteFiles()