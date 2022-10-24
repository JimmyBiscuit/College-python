# First set of arrays
firstName = []
surname = []
examMarks = []

# Start of score module
with open("demo files/Studentmarks.txt", "rt") as f:
    for each_line in f:
        tmp, score = each_line.split(' : ')
        first, last = tmp.split(' ')

        examMarks.append(score)
        firstName.append(first)
        surname.append(last)
f.close()
# End of score module
