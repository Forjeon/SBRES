import datetime
import time
import os


numProjects = 0
projectsDict = {}

def main():
	for i in range(50):
		print("")
	time.sleep(2)
	print("		SBRES v.β_01_02")
	time.sleep(1)
	print("")
	print("		Begin Entry Sequence")
	print("")
	time.sleep(3)
	print("")
	if (os.path.isfile("sbresLog.txt")):
		userInMainUseLog = input("-|Run with Last Use log?    ")
		if (userInMainUseLog == 'n' or userInMainUseLog == 'N'):
			time.sleep(.5)
			print("")
			print("Skipping use of log")
			print("")
			time.sleep(1)
			print("Routing to Entry System via non-positive remembrance")
			print("")
			time.sleep(2)
			entrySystem(False)
			return
		else:
			time.sleep(.5)
			print("")
			print("Processing with log TRUE")
			print("")
			time.sleep(1)
			print("Routing to Entry System via true-pulse remembrance")
			print("")
			time.sleep(2)
			entrySystem(True)
			return
	else:
		print("No Log File Detected")
		print("")
		time.sleep(1)
		print("Routing to Entry System via non-positive remembrance")
		print("")
		time.sleep(2)
		entrySystem(False)
		return

def entrySystem(useLog):
	print("")
	time.sleep(.5)
	for i in range(5):
		print("")
	time.sleep(.3)
	for i in range(50):
		print("")
	if (useLog == False):
		time.sleep(1)
		print("To complete generation of new log file, please answer the following to instantiate a")
		print("Project that will start the log")
		print("")
		print("")
		time.sleep(3)
		userInEntrySystemSpecifyDumpPath = input("-|Please enter the relative path to dump entries to:    ")
		print("")
		print("")
		time.sleep(2)
		userInEntrySystemSpecifyProjectName = input("-|Please enter the project name:    ")
		print("")
		print("")
		time.sleep(2)
		userInEntrySystemSpecifyCreatorName = input("-|Please enter the creator's name:    ")
		print("")
		print("")
		time.sleep(2)
		print("Writing")
		time.sleep(.5)
		if (os.path.isfile("sbresLog.txt")):
			os.remove("sbresLog.txt")
		logFileObj = open("sbresLog.txt", 'a')
		for i in range(50):
			print("")
		print("     .")
		time.sleep(.5)
		for i in range(50):
			print("")
		print("     ..")
		time.sleep(.5)
		logFileObj.write("{0}\n".format(userInEntrySystemSpecifyProjectName))
		for i in range(50):
			print("")
		print("     ...")
		time.sleep(.5)
		logFileObj.write("{0}\n".format(userInEntrySystemSpecifyCreatorName))
		for i in range(50):
			print("")
		print("     .")
		time.sleep(.5)
		logFileObj.write("{0}\n".format(userInEntrySystemSpecifyDumpPath))
		for i in range(50):
			print("")
		print("     ..")
		time.sleep(.5)
		logFileObj.write("{0}\n".format("0"))
		for i in range(50):
			print("")
		print("     ...")
		time.sleep(.5)
		logFileObj.close()
		for i in range(50):
			print("")
		print("Log File Created")
		time.sleep(2)
		for i in range(50):
			print("")
	time.sleep(1)
	print("    Reading")
	time.sleep(2)
	logObj = open("sbresLog.txt", 'r')
	for i in range(50):
		print("")
	print("     .")
	time.sleep(.5)
	logLines = logObj.readlines()
	for i in range(50):
		print("")
	print("     ..")
	time.sleep(.5)
	numProjects = int(len(logLines) / 4)
	for i in range(50):
		print("")
	print("     ...")
	time.sleep(.5)
	for i in range(numProjects):
		projectsDict[logLines[i * 4].strip()] = [logLines[(i * 4) + 1].strip(), logLines[(i * 4) + 3].strip(), logLines[(i * 4) + 2].strip()]
	for i in range(50):
		print("")
	print("Reading complete")
	logObj.close()
	print("")
	time.sleep(2)
	for i in range(50):
		print("")
	time.sleep(1)
	print(" 	There are {0} detected projects".format(numProjects))
	print("")
	for i in range(numProjects):
		time.sleep(.5)
		print("Project_{0}:".format(i + 1))
		print("    {0}".format(logLines[i * 4].strip()))
		print("")
	while True:
		time.sleep(1)
		userInEntrySystemAddOrEntry = input("-|Would you like to add a project ('a') or add an entry (any except 'a')?    ")
		time.sleep(1)
		if (userInEntrySystemAddOrEntry == 'a'):
			time.sleep(1)
			print("")
			userInEntrySystemAddProjectName = input("-|Type the name of the new project:    ")
			print("")
			time.sleep(.5)
			print("")
			userInEntrySystemAddProjectCreatorName = input("-|Type the name of the project creator:    ")
			print("")
			time.sleep(.5)
			print("")
			userInEntrySystemAddProjectDumpPath = input("-|Type the relative dump path for the project:    ")
			print("")
			time.sleep(1)
			print("")
			print(" Writing...")
			time.sleep(2)
			addProjectFileObj = open("sbresLog.txt", 'a')
			addProjectFileObj.write("{0}\n".format(userInEntrySystemAddProjectName))
			addProjectFileObj.write("{0}\n".format(userInEntrySystemAddProjectCreatorName))
			addProjectFileObj.write("{0}\n".format(userInEntrySystemAddProjectDumpPath))
			addProjectFileObj.write("{0}\n".format("0"))
			addProjectFileObj.close()
			print("")
			time.sleep(1)
			print("Done!")
			continue
		else:
			break
	time.sleep(1)
	print("")
	newLogObj = open("sbresLog.txt", 'r')
	newLogLines = newLogObj.readlines()
	numProjects = int(len(newLogLines) / 4)
	projectsDict.clear()
	for i in range(numProjects):
		projectsDict[newLogLines[i * 4].strip()] = [newLogLines[(i * 4) + 1].strip(), newLogLines[(i * 4) + 3].strip(), newLogLines[(i * 4) + 2].strip()]
	time.sleep(1)
	print(" 	There are {0} detected projects".format(numProjects))
	print("")
	for i in range(numProjects):
		time.sleep(.5)
		print("Project_{0}:".format(i + 1))
		print("    {0}".format(newLogLines[i * 4].strip()))
		print("")
	newLogObj.close()
	userInEntrySystemChooseProjectEntry = input("-|Please type the project number you wish to create an entry for:    ")
	time.sleep(1)
	print("")
	print("Chosen Project: {0}".format(newLogLines[(int(userInEntrySystemChooseProjectEntry) - 1) * 4]))
	print("")
	time.sleep(2)
	print("     Begin Entry Logging")
	time.sleep(2)
	entryNumTrackerInObj = open("sbresLog.txt", 'r')
	entryNumTrackerLines = entryNumTrackerInObj.readlines()
	entryNumTrackerInObj.close()
	entryNumTrackerLines[((int(userInEntrySystemChooseProjectEntry) - 1) * 4) + 3] = str(int(entryNumTrackerLines[((int(userInEntrySystemChooseProjectEntry) - 1) * 4) + 3]) + 1)
	entryNumTrackerOutObj = open("sbresLog.txt", 'w')
	entryNumTrackerOutObj.writelines(entryNumTrackerLines)
	entryNumTrackerOutObj.close()
	entryLogger(newLogLines[(int(userInEntrySystemChooseProjectEntry) - 1) * 4].strip())
	return

def entryLogger(projectName):
	entryList = []
	entryListOrder = []
	for i in range(50):
		print("")
	time.sleep(1)
	print("")
	time.sleep(.5)
	print("")
	print("At any point in the logging, press [ENTER] with an empty input")
	print("to end the current entry loop")
	print("")
	time.sleep(.5)
	print("")
	print("")
	print("{0} - Entry {1}".format(projectName, (int(projectsDict[projectName][1]) + 1)))
	time.sleep(.5)
	print("")
	print("")
	while True:
		userInEntryLoggerTextOrImage = input("-|Text ('t') or Image ('i')?    ")
		if (userInEntryLoggerTextOrImage == ''):
			break
		elif (userInEntryLoggerTextOrImage == 't'):
			while True:
				userInEntryLoggerText = input("-|Type a paragraph:    ")
				if (userInEntryLoggerText == ''):
					break
				else:
					entryListOrder.append('t')
					entryList.append(userInEntryLoggerText)
					continue
			continue
		elif (userInEntryLoggerTextOrImage == 'i'):
			while True:
				userInEntryLoggerImage = input("-|Enter the relative path to the image (from the project dump location):    ")
				if (userInEntryLoggerImage == ''):
					break
				else:
					entryListOrder.append('i')
					entryList.append(userInEntryLoggerImage)
					userInEntryLoggerImageLabel = input("-|Enter the label of that image:    ")
					entryListOrder.append('l')
					entryList.append(userInEntryLoggerImageLabel)
					continue
			continue
	time.sleep(2)
	print("")
	print("Data recorded")
	print("")
	time.sleep(2)
	print("")
	print("")
	print("     Begin Log Entering")
	print("")
	time.sleep(2)
	entryWriter(entryList, entryListOrder, (int(projectsDict[projectName][1]) + 1), projectName, projectsDict[projectName][2])
	return

def entryWriter(entryContentList, contentDistinguisherList, entryNum, projectName, projectDumpPath):
	entryTitle = (projectDumpPath + "/" + projectName + "_Entry_" + str(entryNum))
	projectIndexTitle = (projectDumpPath + "/" + projectName + "_Index")
	for i in range(50):
		print("")
	time.sleep(1)
	print("    Updating project Index Page...")
	if (os.path.isfile(projectIndexTitle + ".html")):
		os.remove(projectIndexTitle + ".html")
	projectIndexPageObj = open(projectIndexTitle + ".html", 'w')
	projectIndexPageObj.write("<!DOCTYPE html>\n")
	projectIndexPageObj.write("<html>\n")
	projectIndexPageObj.write("<head>\n")
	projectIndexPageObj.write("<title> Project '{0}' Index</title>\n".format(projectName))
	projectIndexPageObj.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"{0}\">\n".format((projectName + "_Index" + ".css")))
	projectIndexPageObj.write("</head>\n")
	projectIndexPageObj.write("<body>\n")
	projectIndexPageObj.write("<div>\n")
	projectIndexPageObj.write("<h1>Project '{0}' Index</h1>\n".format(projectName))
	projectIndexPageObj.write("<h2>Updated {0}</h2>\n".format(datetime.datetime.now().isoformat()))
	projectIndexPageObj.write("</div>\n")
	projectIndexPageObj.write("<div>\n")
	projectIndexPageObj.write("<ul>\n")
	for i in range(entryNum):
		projectIndexPageObj.write("<li><a href=\"{0}\">Entry 0{1}</a></li>\n".format((projectName + "_Entry_" + str(i + 1) + ".html"), str(i + 1)))
	projectIndexPageObj.write("</ul>\n")
	projectIndexPageObj.write("</div>\n")
	projectIndexPageObj.write("</body>\n")
	projectIndexPageObj.write("</html>")
	projectIndexPageObj.close()
	if (os.path.isfile(projectIndexTitle + ".css")):
		os.remove(projectIndexTitle + ".css")
	projectIndexCSSObj = open(projectIndexTitle + ".css", 'w')
	projectIndexCSSObj.write("div {\n")
	projectIndexCSSObj.write("display: flex;\n")
	projectIndexCSSObj.write("flex-wrap: wrap;\n")
	projectIndexCSSObj.write("}\n")
	projectIndexCSSObj.write("div * {\n")
	projectIndexCSSObj.write("display: inline;\n")
	projectIndexCSSObj.write("}")
	projectIndexCSSObj.close()
	time.sleep(2)
	print("")
	print("    Project Index Page Updated.")
	print("")
	time.sleep(2)
	for i in range(50):
		print("")
	time.sleep(1)
	print("    Writing to page")
	time.sleep(2)
	entryPageObj = open(entryTitle + ".html", 'w')
	entryPageObj.write("<!DOCTYPE html>\n")
	entryPageObj.write("<html>\n")
	entryPageObj.write("<head>\n")
	entryPageObj.write("<title> Entry 0{0}</title>\n".format(entryNum))
	entryPageObj.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"{0}\">\n".format((projectName + "_Entry_" + str(entryNum) + ".css")))
	entryPageObj.write("</head>\n")
	for i in range(50):
		print("")
	print("    .")
	time.sleep(1)
	entryPageObj.write("<body>\n")
	entryPageObj.write("<div>\n")
	entryPageObj.write("<h1>{0} - Entry 0{1}</h1>\n".format(projectName, entryNum))
	entryPageObj.write("<h2>Uploaded {0}</h2>\n".format(datetime.datetime.now().isoformat()))
	entryPageObj.write("</div>\n")
	entryPageObj.write("<div>\n")
	entryPageObj.write("<a href=\"{0}\">Project '{1}' Index</a>\n".format((projectName + "_Index" + ".html"), projectName))
	entryPageObj.write("</div>\n")
	entryPageObj.write("<div>\n")
	for i in range(50):
		print("")
	print("    ..")
	time.sleep(1)
	for i in range(len(contentDistinguisherList)):
		if (contentDistinguisherList[i] == 't'):
			entryPageObj.write("<p>{0}</p>\n".format(entryContentList[i]))
		elif (contentDistinguisherList[i] == 'i'):
			entryPageObj.write("<div id=\"img\">\n")
			entryPageObj.write("<img src=\"{0}\">".format(entryContentList[i]))
			entryPageObj.write("<p>{0}</p>\n".format(entryContentList[i + 1]))
		elif (contentDistinguisherList[i] == 'l'):
			continue
	entryPageObj.write("</div>\n")
	entryPageObj.write("</body>\n")
	entryPageObj.write("</html>")
	entryPageObj.close()
	for i in range(50):
		print("")
	print("    ...")
	time.sleep(2)
	entryCSSObj = open(entryTitle + ".css", 'w')
	entryCSSObj.write("div {\n")
	entryCSSObj.write("display: flex;\n")
	entryCSSObj.write("flex-wrap: wrap;\n")
	entryCSSObj.write("}\n")
	entryCSSObj.write("div * {\n")
	entryCSSObj.write("display: inline;\n")
	entryCSSObj.write("}\n")
	entryCSSObj.write("#img {\n")
	entryCSSObj.write("display: inline;\n")
	entryCSSObj.write("background-color: black;\n")
	entryCSSObj.write("color: white;\n")
	entryCSSObj.write("}")
	entryCSSObj.close()
	for i in range(50):
		print("")
	time.sleep(1)
	print("    Writing successful")
	print("")
	print("")
	time.sleep(3)
	while True:
		print(" Would you like to go back to project picker, or exit?")
		userInEntryWriterNav = input("-|Return to another project ('r') or exit ('x')?    ")
		time.sleep(.5)
		if (userInEntryWriterNav == 'x'):
			time.sleep(.5)
			print("")
			print("Okay, goodbye!")
			break
		elif (userInEntryWriterNav == 'r'):
			time.sleep(.5)
			print("")
			print("Returning to project chooser...")
			print("")
			time.sleep(1)
			entrySystem(True)
			break
		else:
			time.sleep(1)
			print("")
			print("Error: invalid user response. Please try again.")
			time.sleep(.5)
			continue
	return

main()
