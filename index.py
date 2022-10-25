def readFile():
    examMarks = []
    firstName = []
    surname = []

    with open("demo files/Studentmarks.txt", "rt") as f:
        for each_line in f:
            tmp, score = each_line.split(' : ')
            first, last = tmp.split(' ')

            examMarks.append(int(score[:-1]))
            firstName.append(first)
            surname.append(last)

    return examMarks, firstName, surname


def highestMark(examMarks, firstName, surname):
    maximum = 0
    pos = -1

    for index in range(len(examMarks)):

        if examMarks[index] > maximum:
            maximum = examMarks[index]
            pos = index

    highestFirstName = firstName[pos]
    highestSurname = surname[pos]

    return highestFirstName, highestSurname, maximum


def sendResults(highestFirstName, highestSurname, maximum):
    print("The top mark was", maximum, "by", highestFirstName, highestSurname)


def newFile(firstName, surname, examMarks):
    f = open("NewFileResults.txt", "w")

    for index in range(50):
        fileInput = firstName[index] + " " + surname[index] + "has a score of " + str(examMarks[index])

        f.write(fileInput + "\n")


examMarks, firstName, surname = readFile()
highestFirstName, highestSurname, maximum = highestMark(examMarks, firstName, surname)
sendResults(highestFirstName, highestSurname, maximum)
newFile(firstName, surname, examMarks)
