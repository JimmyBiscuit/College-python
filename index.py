# Start of score module
def readFile():

    examMarks = []
    firstName = []
    surname = []

    with open("demo files/Studentmarks.txt", "rt") as f:
        for each_line in f:
            tmp, score = each_line.split(' : ')
            first, last = tmp.split(' ')

            examMarks.append(score)
            firstName.append(first)
            surname.append(last)
    f.close()

    return examMarks, firstName, surname
# End of score module

examMarks, firstName, surname = readFile()
