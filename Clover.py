def parse_flatfile(datafilename, formatfilename):
    output = {} #Dictionary output
    data = []
    with open(datafilename) as dataFile, open(formatfilename) as formatFile:
        for dataLine in dataFile:
            dataLine = dataLine.split() #To seperate values I need to work with

            if len(dataLine) < 3: #Some lines the valid value and count value are not seperated by space bar so this fixes that
                dataLine.append(dataLine[1][1:])
                dataLine[1] = dataLine[1][:1]
            print(dataLine)

            output['name'] = dataLine[0]
            output['valid'] = dataLine[1]
            output['count'] = dataLine[2]

            data.append(output) #Create list of the key-value pairs.



        #for data in file_data:
            #for formatLine in formatFile:
                #formatLine = formatLine.rstrip()  # get rid of '\n' showing up in list
                #formatLine = formatLine.split(',')
                #print(formatLine)
    print(data)

parse_flatfile('datafile.txt','formatfile.csv')

