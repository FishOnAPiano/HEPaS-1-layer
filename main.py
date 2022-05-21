testingMarkList = [("CS1", 45), ("CS1", 45), ("CS1", 90), ("CS2", 85), ("CS3", 95), ("CS4", 90), ("CS5", 80), ("CS6", 80), ("CS7", 45), ("CS7", 90), ("CS8", 85), ("CS9", 95)]

#Contains student information in format[[personID, lastName, email, [markList]]]
database = [
            ["BobD", "Dylan", "bobd@EOU", [("CS1", 45), ("CS1", 45), ("CS1", 90), ("CS2", 85), ("CS3", 95), ("CS4", 90), ("CS5", 80), ("CS6", 80), ("CS7", 45), ("CS7", 90), ("CS8", 85), ("CS9", 95)]]
            ]

#SERVER
def printMarks(unitMarkList):
    for unitMark in unitMarkList:  
        print(unitMark[0] + ": " + str(unitMark[1]))

#TEST
printMarks(testingMarkList)

#Returns the average mark from unitMarkList
def calculateCourseAverage(unitMarkList):
	markSum = 0;
	for unitMarkTuple in unitMarkList:
		markSum += unitMarkTuple[1]
	if len(unitMarkList) != 0:
		markAverage = markSum/len(unitMarkList)
	return markAverage

#TEST
print("Course Average: " + str(calculateCourseAverage(testingMarkList)) + "\n")

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

#TEST
print("Best Eight Average: " + str(calculateBestEightAverage(testingMarkList)) + "\n")

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

print(evaluateQualification("bob", testingMarkList))

def EOUStudentEvaluation(personID, lastName, email):
    matchingEntry = False
    for entry in database:
        if entry[0] == personID and entry[1] == lastName and entry[2] == email:
            matchingEntry = entry
            break
    if matchingEntry:
        return(evaluateQualification(entry[0], entry[3]))
    else:
        return "No matching student found"
        
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
        personID = input("Please enter your Person ID")
        while True:
            print("Please enter 12-30 unit codes and scores, and enter 'done' when complete")
            unitMarkList = []
            while True:
                unitCode = input("Unit code: ")
                if unitCode == "done":
                    break
                #TODO: Verify input is 0-100
                unitMark = int(input("Mark: "))
                unitMarkList.append((unitCode, unitMark))
                if len(unitMarkList) == 30:
                    print("Maximum of 30 marks, evaluating using provided marks")
                    break
            if len(unitMarkList) >= 12:
		#Server call
                print(evaluateQualification(personID, unitMarkList))
                break
            print("Insufficent marks, at least 12 are required")
main()
