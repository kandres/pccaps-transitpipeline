import os, datetime
import glob,json

filePath='data//'

def getLatestFileDate():
    list_of_files = glob.glob(filePath + "*.json")
    if list_of_files:
        latest_file = max(list_of_files, key=os.path.getctime)
        ctime= os.path.getctime(latest_file)

        return datetime.datetime.fromtimestamp(ctime)
    else:
        return None

def readData():
    list_of_files = glob.glob(filePath + "*.json")
    for file in list_of_files:
        with open (file) as jsonFile:
            data=json.load(jsonFile)
            print(data)

readData()
