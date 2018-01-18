import csv

def parse_flatfile(datafilename, formatfilename):
    output = {} #Dictionary output
    outputList = [] #Want a list of dictionaries
    colNames = [] #Will be the key names in output dictionary

    with open(datafilename) as dataFile, open(formatfilename) as formatFile:
        formatCSV = csv.reader(formatFile)

        for key in formatCSV: #getting the column names in list to work with later.
            if key[0] == 'column name': #skipping first row
                continue
            colNames.append(key[0])

        for dataLine in dataFile:
            dataLine = dataLine.split() #To separate values I need to work with

            if len(dataLine) < 3: #Some lines the valid value and count value are not seperated by space bar so this fixes that
                dataLine.append(dataLine[1][1:])
                dataLine[1] = dataLine[1][:1]

            output[colNames[0]] = dataLine[0]
            output[colNames[1]] = bool(dataLine[1])
            output[colNames[2]] = int(dataLine[2])
            outputList.append(output.copy()) #Create list of the key-value pairs.

    print(outputList)

parse_flatfile('datafile.txt','formatfile.csv')

