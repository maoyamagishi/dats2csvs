import csv
import datetime

class Interface:
    def ManageCSV(datdata,folderpath):
        filename = datdata[0]
        lst1 = datdata[1]
        lst2 = datdata[2]
        matrix = Interface.AlterDataStructure(lst1,lst2)
        filepath = Interface.createCSV(folderpath,filename)
        Interface.writeCSV(matrix,filepath,filename)

    def writeCSV(matrix,writingPath,filename):
        with open(writingPath,"a",newline="") as f:
            writer = csv.writer(f)
            f.truncate(0)
            writer.writerow([filename])#([])とすることで文字列であるファイル名を配列に変換、csv.writer.writerowに適応させる
            for ii in range(len(matrix)):
                writer.writerow(matrix[ii])   
    
    def createCSV(folderpath,filename):
        creatingfileName = filenameManager.newfilename(filename)
        filepath =  str(folderpath) + '\\' +creatingfileName  +  '.csv'
        with open(filepath,"w") as f:
            writer = csv.writer(f)
            writer.writerow('')
        f.close
        return filepath

    def AlterDataStructure(lst1,lst2):
        RawContent = []
        for ii in range(len(lst1)):
            RawContent.append([lst1[ii],lst2[ii]])
        return RawContent



class filenameManager:
    def newfilename(oldfilename):
        date = filenameManager.getDate()
        time = filenameManager.getTime()
        newname = oldfilename +'(' + date + time + ')'
        return newname

    def getDate():
        DateToday = datetime.date.today()
        year = DateToday.year
        month = DateToday.month
        day = DateToday.day
        return filenameManager.tristringize(year,month,day)
        
    def getTime():
        timeNow = datetime.datetime.now().time()
        hour = timeNow.hour
        minute = timeNow.minute
        sec = timeNow.second
        return filenameManager.tristringize(hour,minute,sec)

    def tristringize(arg1,arg2,arg3):
        tristrized = str(arg1) + str(arg2) + str(arg3)
        return tristrized

