import csv

def parse_flatfile(datafilename, formatfilename):
    output = {} #Dictionary output
    outputList = []
    colNames = []

    with open(datafilename) as dataFile, open(formatfilename) as formatFile:
        fileformat = csv.reader(formatFile)

        for key in fileformat: #getting the column names in list to work with later.
            if key[0] == 'column name':
                continue
            colNames.append(key[0])

        for dataLine in dataFile:
            dataLine = dataLine.split() #To seperate values I need to work with

            if len(dataLine) < 3: #Some lines the valid value and count value are not seperated by space bar so this fixes that
                dataLine.append(dataLine[1][1:])
                dataLine[1] = dataLine[1][:1]

            output[colNames[0]] = dataLine[0]
            output[colNames[1]] = bool(dataLine[1])
            output[colNames[2]] = int(dataLine[2])
            outputList.append(output.copy()) #Create list of the key-value pairs.



        #for data in file_data:
            #for formatLine in formatFile:
                #formatLine = formatLine.rstrip()  # get rid of '\n' showing up in list
                #formatLine = formatLine.split(',')
                #print(formatLine)
    print(outputList)

parse_flatfile('datafile.txt','formatfile.csv')

