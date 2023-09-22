import CsvWriter as cw
import datFileReader as df
import FilepathDialog as fp

folderAndFiles = fp.Interface.OpenDialog()
folderPath = folderAndFiles[0]
filePathList = folderAndFiles[1]

for ii in range(len(filePathList)):
    datdata = df.datFileInterface.DatHandler(filePathList[ii])
    cw.Interface.ManageCSV(datdata,folderPath)