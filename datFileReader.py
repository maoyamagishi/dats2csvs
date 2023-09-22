class datFileInterface:
    def DatNameReader(name):
        # Reading first line with airfoil name
        object_name = name
        if(len(object_name)==0): 
            object_name = "No_name"
        object_name = object_name.replace(" ", "_")
        object_name = object_name.strip("\n")
        return  object_name
    
    def DatHandler(pathfile):
        with open(pathfile) as f:
            datfile = f.readlines()
            # Reading file into array
            filesize = len(datfile) -1
            filename = datFileInterface.DatNameReader(datfile[0])
            coXY = datFileInterface.DAT2List2(datfile,filesize)
        coordX = coXY[0]
        coordY = coXY[1]        
        return filename, coordX ,coordY


    def DAT2List2(datfile,filesize):
        coordX = []
        coordY = []
        for ii in range(filesize ):
            line = datfile[ii +1]
            line = line.strip(' \t')
            line = line.replace('\t', ' ')
            line = line.replace(',', ' ')
            p1 = line.find(" ")
            p2 = line.rfind(" ")
            try:
                x = float(line[0:p1])
            except ValueError:
                break
            try:
                y = float(line[p2+1:])
            except ValueError:
                break
            coordX.append(x)
            coordY.append(y)
            # Reading next line with coordinates
        return coordX,coordY
    
