#Start of the function to open and sort the file into arrays
def readFile():
    examMarks = []
    firstName = []
    surname = []
    
    #Opens the file as f 
    with open("demo files/Studentmarks.txt", "rt") as f:
        for each_line in f:
            #Splits it into their components
            tmp, score = each_line.split(' : ')
            first, last = tmp.split(' ')

            #Inserts it into their respective arrays
            examMarks.append(int(score[:-1]))
            firstName.append(first)
            surname.append(last)

    return examMarks, firstName, surname
#End of file reading

#Beginning of function to find the highest mark   
def highestMark(examMarks, firstName, surname):
    #Set up for the variables
    maximum = 0
    pos = -1
    
    #Start of fixed loop to scout through the examMarks array
    for index in range(len(examMarks)):

        #If statment to find the highest number
        if examMarks[index] > maximum:
            maximum = examMarks[index]
            pos = index

    #Variables for storing the infomation
    highestFirstName = firstName[pos]
    highestSurname = surname[pos]

    return highestFirstName, highestSurname, maximum
#End of highest mark finder

#Sends the highest mark to the diplay with their full name
def sendResults(highestFirstName, highestSurname, maximum):
    print("The top mark was", maximum, "by", highestFirstName, highestSurname)

#Function to make a new file with their results
def newFile(firstName, surname, examMarks):
    #Creates the new file
    f = open("NewFileResults.txt", "w")

    #Fixed loop, loops 50 times
    for index in range(50):
        
        #Variable for the information to enter into the file
        fileInput = firstName[index] + " " + surname[index] + "has a score of " + str(examMarks[index])

        #Writes to the new file and takes a new line
        f.write(fileInput + "\n")
#End of new file function

#Runs entire program
examMarks, firstName, surname = readFile()
highestFirstName, highestSurname, maximum = highestMark(examMarks, firstName, surname)
sendResults(highestFirstName, highestSurname, maximum)
newFile(firstName, surname, examMarks)
