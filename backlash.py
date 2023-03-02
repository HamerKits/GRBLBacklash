class backlash():
    def __init__(self):
        self.xBacklash = 0.0    #default values
        self.yBacklash = 0.0
        self.zBacklash = 0.0
        self.absolute = True    #absolute/relative positioning
        self.metric = False  #metric/standard coordinates
        self.dPlaces = 5    #set max number of decimal places
        self.output = ""
        self.comments = False    #enable comments in output
        self.tolerance = 0.005    #tollerance for direction change

    def setBacklash(self, x, y, z, t):     #x y and z backlash in standard
        self.xBacklash = x
        self.yBacklash = y
        self.zBacklash = z
        self.tolerance = t

    def applyBacklash(self, filePath):
        readFile = open(filePath, "r")

        self.output = ""    #reset output

        #reset values
        xLastDirection = 0  #0 = no direction (startup), 1 = positive direction, 2 = negative direction
        yLastDirection = 0  #0 = no direction (startup), 1 = positive direction, 2 = negative direction
        zLastDirection = 0  #0 = no direction (startup), 1 = positive direction, 2 = negative direction
        xDirChange = 0  #0 = no change, 1 = positive change, 2 = negative change
        yDirChange = 0  #0 = no change, 1 = positive change, 2 = negative change
        xDirChange = 0  #0 = no change, 1 = positive change, 2 = negative change
        xLastCoordinate = 0.0  #last coordinate
        yLastCoordinate = 0.0  #last coordinate
        zLastCoordinate = 0.0  #last coordinate

        for fileLine in readFile:
            #reset values
            nl = False
            cr = False

            if (fileLine.find("\n") != -1):  #see if there is a newline character
                nl = True
                fileLine = fileLine.rstrip("\n")    #remove newline

            if (fileLine.find("\r") != -1): #see if there is a carrage return character
                cr = True
                fileLine = fileLine.rstrip("\r")    #remove carrage return

            if (fileLine.find("G20") != -1):    #see if standard coordinates
                self.metric = False #not metric

            if (fileLine.find("G21") != -1):    #see if metric coordinates
                self.metric = True #metric

            if (fileLine.find("G90") != -1):    #see if absolute positioning
                self.absolute = True #absolute positioning

            if (fileLine.find("G91") != -1):    #see if relative positioning
                self.absolute = False #relative positioning

            if (fileLine.find("G0") != -1): #see if a movement command
                #get locations of X, Y and Z coordinates
                xLoc = fileLine.find("X")
                yLoc = fileLine.find("Y")
                zLoc = fileLine.find("Z")
                
                #reset values
                xVal = ""
                yVal = ""
                zVal = ""

                #get x value from line
                for x in range(len(fileLine)):
                    if ((x > xLoc) and (xLoc != -1)):
                        if ((fileLine[x].isnumeric()) or (fileLine[x] == ".") or (fileLine[x] == "-")):
                            xVal += fileLine[x]
                        else:
                            break

                #get y value from line
                for x in range(len(fileLine)):
                    if ((x > yLoc) and (yLoc != -1)):
                        if ((fileLine[x].isnumeric()) or (fileLine[x] == ".") or (fileLine[x] == "-")):
                            yVal += fileLine[x]
                        else:
                            break

                #get z value from line
                for x in range(len(fileLine)):
                    if ((x > zLoc) and (zLoc != -1)):
                        if ((fileLine[x].isnumeric()) or (fileLine[x] == ".") or (fileLine[x] == "-")):
                            zVal += fileLine[x]
                        else:
                            break

                #convert values to floats
                if (xLoc != -1):
                    xVal = float(xVal)
                if (yLoc != -1):
                    yVal = float(yVal)
                if (zLoc != -1):
                    zVal = float(zVal)

                #see if x direction changed
                if (xLoc != -1):    #see if there was an x coordinate instruction
                    if (xVal > (xLastCoordinate + self.tolerance)):
                        if (xLastDirection != 1):   #see if direction changed
                            xDirChange = 1  #positive direction change
                            xLastDirection = 1  #update direction for next loop
                    if (xVal < (xLastCoordinate - self.tolerance)):
                        if (xLastDirection != 2):   #see if direction changed
                            xDirChange = 2  #negative direction change
                            xLastDirection = 2  #update direction for next loop
                    if (self.absolute == True):
                        xLastCoordinate = xVal  #update last coordinate for next loop
                    else:
                        xLastCoordinate = 0

                #see if y direction changed
                if (yLoc != -1):    #see if there was an y coordinate instruction
                    if (yVal > (yLastCoordinate + self.tolerance)):
                        if (yLastDirection != 1):   #see if direction changed
                            yDirChange = 1  #positive direction change
                            yLastDirection = 1  #update direction for next loop
                    if (yVal < (yLastCoordinate - self.tolerance)):
                        if (yLastDirection != 2):   #see if direction changed
                            yDirChange = 2  #negative direction change
                            yLastDirection = 2  #update direction for next loop
                    if (self.absolute == True):
                        yLastCoordinate = yVal  #update last coordinate for next loop
                    else:
                        yLastCoordinate = 0

                #see if z direction changed
                if (zLoc != -1):    #see if there was an z coordinate instruction
                    if (zVal > (zLastCoordinate + self.tolerance)):
                        if (zLastDirection != 1):   #see if direction changed
                            zDirChange = 1  #positive direction change
                            zLastDirection = 1  #update direction for next loop
                    if (zVal < (zLastCoordinate - self.tolerance)):
                        if (zLastDirection != 2):   #see if direction changed
                            zDirChange = 2  #negative direction change
                            zLastDirection = 2  #update direction for next loop
                    if (self.absolute == True):
                        zLastCoordinate = zVal  #update last coordinate for next loop
                    else:
                        zLastCoordinate = 0

                comments = ""

                #handle standard/metric conversion and offset
                if (self.metric == True):
                    xOffset = round((self.xBacklash / 25.4) / 2, self.dPlaces)
                    yOffset = round((self.yBacklash / 25.4) / 2, self.dPlaces)
                    zOffset = round((self.zBacklash / 25.4) / 2, self.dPlaces)
                else:
                    xOffset = round(self.xBacklash / 2, self.dPlaces)
                    yOffset = round(self.yBacklash / 2, self.dPlaces)
                    zOffset = round(self.zBacklash / 2, self.dPlaces)

                #add the backlash value
                if (xLoc != -1):
                    if (xDirChange == 1):
                        xVal += xOffset #add offset to x value
                        comments += "X Backlash + " + str(round(xOffset, self.dPlaces)) + " ,"
                    elif (xDirChange == 2):
                        xVal -= xOffset #subtract offset from x value
                        comments += "X Backlash - " + str(round(xOffset, self.dPlaces)) + " ,"
                    if (self.absolute == False):
                        xDirChange = 0  #only need to add one offset for relative posistioning
                if (yLoc != -1):
                    if (yDirChange == 1):
                        yVal += yOffset #add offset to y value
                        comments += "Y Backlash + " + str(round(xOffset, self.dPlaces)) + " ,"
                    elif (yDirChange == 2):
                        yVal -= yOffset #subtract offset from y value
                        comments += "Y Backlash - " + str(round(xOffset, self.dPlaces)) + " ,"
                    if (self.absolute == False):
                        yDirChange = 0  #only need to add one offset for relative posistioning
                if (zLoc != -1):
                    if (zDirChange == 1):
                        zVal += zOffset #add offset to z value
                        comments += "Z Backlash + " + str(round(xOffset, self.dPlaces)) + " ,"
                    elif (zDirChange == 2):
                        zVal -= zOffset #subtract offset from z value
                        comments += "Z Backlash - " + str(round(xOffset, self.dPlaces)) + " ,"
                    if (self.absolute == False):
                        zDirChange = 0  #only need to add one offset for relative posistioning

                #rebuild the command line
                fileLine = fileLine[0:4]
                if (xLoc != -1):
                    fileLine += "X" + str(round(xVal, self.dPlaces))
                if (yLoc != -1):
                    fileLine += "Y" + str(round(yVal, self.dPlaces))
                if (zLoc != -1):
                    fileLine += "Z" + str(round(zVal, self.dPlaces))
                if (self.comments == True):
                    fileLine += " (" + comments + ")"
                
            #add special characters back to end of line
            if (cr == True):
                fileLine += "\r"    #add carrage return character
            if (nl == True):
                fileLine += "\n"    #add newline character

            self.output += fileLine #add line to output
        readFile.close()    #close file
                
    def saveOutput(self, filePath): #save output to file
        writeFile = open(filePath, "w")
        writeFile.write(self.output)
        writeFile.close()
