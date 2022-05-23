testingMarkListTwelve = [("CS1", 45), ("CS1", 45), ("CS1", 90), ("CS2", 85), ("CS3", 95), ("CS4", 90), ("CS5", 80), ("CS6", 80), ("CS7", 45), ("CS7", 90), ("CS8", 85), ("CS9", 95)]
testingMarkListThirty = [("CS1", 45), ("CS1", 45), ("CS1", 90), ("CS2", 85), ("CS3", 95), ("CS4", 90), ("CS5", 80), ("CS6", 80), ("CS7", 45), ("CS7", 90), ("CS8", 85), ("CS9", 95), ("CS10", 12), ("CS10", 40), ("CS10", 65), ("CS11", 65), ("CS12", 66), ("CS13", 67), ("CS14", 68), ("CS15", 69), ("CS16", 70), ("CS17", 71), ("CS18", 72), ("CS19", 73), ("CS19", 74), ("CS20", 75), ("CS21", 76), ("CS22", 77), ("CS23", 78), ("CS24", 79)]
#Contains student information in format[[personID, lastName, email, [markList]]]
database = [
            #Six failures
            ["SixF", "Fails", "sixf@EOU", [("CS1", 30), ("CS1", 20), ("CS1", 55), ("CS2", 12), ("CS2", 30), ("CS2", 60), ("CS3", 10), ("CS3", 20), ("CS3", 51), ("CS4", 55), ("CS5", 70), ("CS6", 60)]],
            #Course Average >= 70
            ["BobD", "Dylan", "bobd@EOU", testingMarkListTwelve],
            #Course Average >= 65, Best eight average >= 80
            ["EightQ", "Qualified", "eightq@EOU", [("CS1", 45), ("CS1", 50), ("CS2", 49), ("CS2", 55), ("CS3", 70), ("CS4", 80), ("CS5", 90), ("CS6", 80), ("CS7", 95), ("CS8", 85), ("CS9", 50), ("CS10", 90)]],
            #Course average >= 60, Best eight average >= 80
            ["ChanceF", "Further", "chancef@EOU", [("CS1", 10), ("CS1", 50), ("CS2", 10), ("CS2", 55), ("CS3", 70), ("CS4", 80), ("CS5", 90), ("CS6", 80), ("CS7", 95), ("CS8", 85), ("CS9", 50), ("CS10", 90)]],
            #Course Average >= 60, Best eight average < 80
            ["RheaS", "Sess", "rheas@EOU", [("CS1", 45), ("CS1", 50), ("CS2", 49), ("CS2", 55), ("CS3", 70), ("CS4", 80), ("CS5", 90), ("CS6", 80), ("CS7", 80), ("CS8", 85), ("CS9", 49), ("CS10", 51)]],
            #Course average < 60
            ["NoC", "Chance", "noc@EOU", [("CS1", 10), ("CS1", 51), ("CS2", 10), ("CS2", 55), ("CS3", 55), ("CS4", 55), ("CS5", 55), ("CS6", 55), ("CS7", 55), ("CS8", 55), ("CS9", 50), ("CS10", 55)]],
            ]

#SERVER
def printMarks(unitMarkList):
    for unitMark in unitMarkList:  
        print(unitMark[0] + ": " + str(unitMark[1]))

#TEST successful printing 12 marks
print("Printing 12 marks")
printMarks(testingMarkListTwelve)
#TEST successful printing 30 marks
print("Printing 30 marks")
printMarks(testingMarkListThirty)

#Returns the average mark from unitMarkList
def calculateCourseAverage(unitMarkList):
	markSum = 0;
	for unitMarkTuple in unitMarkList:
		markSum += unitMarkTuple[1]
	if len(unitMarkList) != 0:
		markAverage = markSum/len(unitMarkList)
	return markAverage

#TEST course average successful calc 12 marks
print("Course average for 12 marks")
print("Course Average: " + str(calculateCourseAverage(testingMarkListTwelve)) + "\n")
#TEST successful average calc 30 marks
print("Course average for 30 marks")
print("Course Average: " + str(calculateCourseAverage(testingMarkListThirty)) + "\n")

#Returns an average mark generated from the 8 highest scores in unitMarkList
def calculateBestEightAverage(unitMarkList):
#-1 indicates empty slot; can we assume marks are positive?
	bestEight = [-1, -1, -1, -1, -1, -1, -1, -1]
	for unitMarkTuple in unitMarkList:
		for pos in range(8):
			# if mark is greater than or equal to score at pos in bestEight, and less than or equal to the next score up (I.E. if score belongs in this position)
			if unitMarkTuple[1] >= bestEight[pos] and (pos == 7 or unitMarkTuple[1] <= bestEight[pos+1]):
				bestEight.pop(0)
				bestEight.insert(pos, unitMarkTuple[1])
				break
    #TODO: Remove print, just there to make testing easier
	print(bestEight)
	markSum = 0
	for mark in bestEight:
		if mark != -1:
			markSum += mark
	markAverage = markSum/(8-bestEight.count(-1))
	return markAverage

#TEST Best eight average successful calc 12 marks
print("Best 8 average for 12 marks")
print("Best Eight Average: " + str(calculateBestEightAverage(testingMarkListTwelve)) + "\n")
#TEST Best eight average for 30 marks
print("Best 8 average for 30 marks")
print("Best Eight Average: " + str(calculateBestEightAverage(testingMarkListThirty)) + "\n")

#Returns the response string that matches how qualified for honors study a student with the provided dataset is
def evaluateQualification(personID, unitMarkList):
	courseAverage = calculateCourseAverage(unitMarkList)
	bestEightAverage = calculateBestEightAverage(unitMarkList)
	numFails = 0
	for unitMarkTuple in unitMarkList:
		if unitMarkTuple[1] < 50:
			numFails += 1
	if numFails >= 6:
		return str(personID) + ", " + str(courseAverage) + ", with 6 or more Fails! DOES NOT QUALIFY FOR HONORS STUDY!"
	elif courseAverage >= 70:
		return str(personID) + ", " + str(courseAverage) + ", QUALIFIED FOR HONOURS STUDY!"
	elif courseAverage >= 65 and bestEightAverage >= 80:
		return str(personID) + ", " + str(courseAverage) + ", QUALIFIED FOR HONOURS STUDY!"
	elif courseAverage >= 60 and bestEightAverage >= 80:
		return str(personID) + ", " + str(courseAverage) + ", " + str(bestEightAverage) + ", MAY HAVE GOOD CHANCE! Need further assessment!"
	elif courseAverage >= 60 and bestEightAverage < 80:
		return str(personID) + ", " + str(courseAverage) + ", " + str(bestEightAverage) + ", MAY HAVE A CHANCE! Must be carefully reassessed and get the coordinator's permission!"
	else:
		return str(personID) + ", " + str(courseAverage) + ", DOES NOT QUALIFY FOR HONORS STUDY!"

#TEST six fails
print("Testing with six fails")
print(evaluateQualification(database[0][0], database[0][3]))
#test courseAverage >= 70
print("Testing with course average >= 70")
print(evaluateQualification(database[1][0], database[1][3]))
#test courseAverage >= 65 and best eight average >= 80
print("Testing with course average >= 65 and best eight average >= 80")
print(evaluateQualification(database[2][0], database[2][3]))
#test courseAverage >= 60 and best eight average >= 80
print("Testing with course average >= 60 and best eight average >= 80")
print(evaluateQualification(database[3][0], database[3][3]))
#test courseAverage >= 60 and best eight average < 80
print("Testing with course average >= 60 and best eight average >= 80")
print(evaluateQualification(database[4][0], database[4][3]))
#test courseAverage < 60
print("Testing with course average < 60")
print(evaluateQualification(database[5][0], database[5][3]))


def EOUStudentEvaluation(personID, lastName, email):
    matchingEntry = False
    for entry in database:
        if entry[0] == personID and entry[1] == lastName and entry[2] == email:
            matchingEntry = entry
            break
    if matchingEntry:
        return(evaluateQualification(entry[0], entry[3]))
    else:
        return "Verification details do not match recorded values for an EOU student"
        
#CLIENT
def main():
    while True:
        EOUStudent = input("Are you an EOU Student? (y/n): ")
        if EOUStudent == "y" or EOUStudent == "n":
            break
        print("Invalid input")
    if EOUStudent == "y":
        #Use recorded data
        personID = ""
        lastName = ""
        email = ""
        while True:
            print("Please enter personal details for verification")
            personID = input("Person ID: ")
            lastName = input("Last name: ")
            email = input("EOU email: ")
            valid = input("Are these details correct? (y/n)")
            if valid == "y":
                break
                
        #Server call
        print(EOUStudentEvaluation(personID, lastName, email))
    else:
        #Enter new data
        personID = input("Please enter your Person ID: ")
        while True:
            print("Please enter 12-30 unit codes and marks, and enter 'done' when complete")
            unitMarkList = []
            while True:
                unitCode = input("Unit code: ")
                if unitCode == "done":
                    break
                markString = input("Mark: ")
                mark = -1
                try:
                    mark = int(markString)
                except ValueError:
                    pass
                
                numPasses = 0
                numFails = 0
                for unitMark in unitMarkList:
                    if unitMark[0] == unitCode:
                        if unitMark[1] >= 50:
                            numPasses += 1
                        else:
                            numFails +=1
                if mark < 0 or mark > 100:
                    #Catches non-number input as well, as if cannot be converted to number mark will still be -1
                    print("Invalid mark, please enter a number between 0 and 100")
                elif not unitCode:
                    print("Please enter a valid unit code")
                elif numPasses == 1 and mark >= 50:
                    print(unitCode + " has already had a passing mark recorded, only one passing mark is allowed")
                elif numFails == 2 and mark < 50:
                    print(unitCode + " already has two failing marks, only two failing marks are allowed")
                else:
                    unitMarkList.append((unitCode, mark))
                    if len(unitMarkList) == 30:
                        print("Maximum of 30 marks reached, evaluating using provided marks")
                        break                    
        if len(unitMarkList >= 12):
            #Server call
            print(evaluateQualification(personID, unitMarkList))
        else:
            print("Insufficent marks entered, at least 12 are required")
main()
