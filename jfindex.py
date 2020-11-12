#!/usr/bin/env python3
import curses
import os
import sys

from source.myCurses import *
from source.project import *
from source.myPrint import *

if (len(sys.argv)-1 ==0 ):
    vision = True
else:
    if (sys.argv[1] == 'more'):
	vision = False
    else:
	vision = True
myCmd = os.popen('ls | grep "\.log$"').read()
allFilesNames = myCmd.split()
nameProgram = 'JFINDEX'

if vision:
    screen = curses.initscr() # set the style
    curses.wrapper(do_it)    # pantalla de Inicio

    printCenter("WELLCOME TO "+nameProgram.upper(),screen)
    printFooterLeft("Version: 1.1",screen)
    printFooterRight("2020 ",screen)
    screen.refresh()
    curses.napms(3000)
    
    if len(allFilesNames) == 0:
	screen.clear()
	printCenter("No Files *.log :(",screen)
	screen.refresh()
	curses.napms(3000)
	curses.endwin()
	sys.exit(0)   # salir sin errores
else:
    printElement('-',40)
    printElementName(nameProgram.upper(),'-',40)
    printElement('-',40)
    if len(allFilesNames) == 0:
	printElementName('No Files *.log','=',40)
	sys.exit(0)   # salir sin errores


# List for the project

allProjectName =[]                  # Project Name
allBadFilesName = []                # Bad Project  Name

listProject = []                    # List Project 
listProjectIncomplete = []          # List Incomple Project 

listProjectMethod = []               # List Project  Method
allProjectMethodName =[]                   # List Project  Method Name 
# Load List All  Project & All Bad 

for i in range (len(allFilesNames)):
    name = allFilesNames[i]
    if name.find('_N+1.log') != -1 or name.find('_N-1.log') != -1 or name.find('_N.log') != -1:
	aux = allFilesNames[i].replace('.log','')
	aux = aux.replace('_N-1','')
	aux = aux.replace('_N+1','')
	aux = aux.replace('_N','')
	if not(aux in allProjectName):
	    allProjectName.append(aux)
    else:
	allBadFilesName.append(allFilesNames[i].replace('.log',''))

#print('Contenido')
#print(allFilesNames)
#print(allBadFilesName)
#print('allProjectName:',allProjectName)
 
# load the project names

for i in range (len(allProjectName)):
    a = Project(allProjectName[i])
    a.loadingFiles(allFilesNames)
    a.checkUnique()
    if a.status == True :
	listProject.append(a)
    else:
	listProjectIncomplete.append(a) 

for project in listProject:
    aux = project.shortName
    if not(aux in allProjectMethodName):
	allProjectMethodName.append(aux)
    #print('Sub-Projects:', project.name)

for name in allProjectMethodName:
    a = ProjectMethod(name)
    listProjectMethod.append(a)

for projectMethod in listProjectMethod:
    for project in listProject:
	if project.shortName == projectMethod.name:
	    projectMethod.appendProject(project)

#for project in listProjectMethod:
	#project.view()		

#print('Project List:',allProjectMethodName)
	

if len(listProjectMethod)!= 0:
    if vision:
	screen.clear()
	printTop("Project List",screen)
	for i in range (len(listProjectMethod)):
	    aux=str(i)+': '+listProjectMethod[i].getName()
	    printCenterPlus(aux,screen,i)
	screen.refresh()
    else:
	printElementName('Project List','*',40)
	for i in range (len(listProjectMethod)):
	    print(str(i)+': ',listProjectMethod[i].getName())
	printElement('*',40)

else:
    if vision:
	screen.clear()
	printCenter("No Project  :(",screen)
	screen.refresh()
	curses.napms(2000)
	curses.endwin()
    else:
	printElementName('No Project  :(','=',40)
	sys.exit(0)   # salir sin errores



# Choose the project for work

flag = False

while True:
    if vision:
	answer = my_int_input('Choose Project',screen,flag)
    else:
	answer = checker('Choose Project')
    if ( answer < 0) or (answer > len(listProjectMethod)-1):
	if vision:
	    flag = True
	else:
	    print('Action not valid: ', answer)
    else:
	break

nproject = answer


# Step6

if vision:
    curses.napms(2000)
    screen.clear()
    printTop('*** Working ***',screen)
    screen.refresh()

else:
    printElementName('Working','*',40)

# working togheter
for project in listProjectMethod[nproject].lista:
    project.stageS1()
    nameaux = project.getName()
    if project.s1 :
	if vision:
	    curses.napms(1000)
	    screen.clear()
	    printCenter(nameaux,screen)
	    printTop('**** Working S1 ****',screen)
	    screen.refresh()

	else:
	    printElementName(nameaux,'',40) 
	    printElementName(' --> S1 OK','',40) 
	project.stageS2()
	if project.s2 :
	    if vision:
		curses.napms(1000)
		screen.clear()
		printCenter(nameaux,screen)
		printTop('**** Working S2 ****',screen)
		screen.refresh()
	    else:
		printElementName(' --> S2 OK','',40) 
		project.stageS3()
		if project.s3:
		    if vision:
			curses.napms(1000)
			screen.clear()
			printCenter(nameaux,screen)
			printTop('**** Working S3 ****',screen)
			screen.refresh()
		    else:
			printElementName(' --> S3 OK','',40) 
		    project.stageS4()
		    if project.s4: 
			if vision:
			    curses.napms(1000)
			    screen.clear()
			    printCenter(nameaux,screen)
			    printTop('**** Working S4 ****',screen)
			    screen.refresh()
			else:
			    printElementName(' --> S4 OK','',40) 
		    else:
			if vision:
			    curses.napms(1000)
			    screen.clear()
			    printCenter(nameaux,screen)
			    printTop('**** ERROR S4 ****',screen)
			    screen.refresh()
			else:
			    printElementName(nameaux+'ERROR S4','*',40)
		else:
		    if vision:
			curses.napms(1000)
			screen.clear()
			printCenter(nameaux,screen)
			printTop('**** ERROR S3 ****',screen)
			screen.refresh()
		    else:
			printElementName(nameaux+'ERROR S3','*',40) 
	else:
	    if vision:
		curses.napms(1000)
		screen.clear()
		printCenter(nameaux,screen)
		printTop('**** ERROR S2 ****',screen)
		screen.refresh()

	    else:
		printElementName(nameaux+'ERROR S2','*',40) 
    else:
	if vision:
	    curses.napms(1000)
	    screen.clear()
	    printCenter(nameaux,screen)
	    printTop('**** ERROR S1 ****',screen)
	    screen.refresh()

	else:
	    printElementName(nameaux+'ERROR S1','*',40) 
	
    #project.view()

#latex("TablaHartree.tex", listProjectMethod[nproject].lista,5,"hartree")
#csv("TablaHartree.csv", listProjectMethod[nproject].lista,5,"hartree")

nameCurrentProject = listProjectMethod[nproject].getName()

fileOutputTex = nameCurrentProject +'_Hartree.tex'
fileOutputCsv = nameCurrentProject +'_Hartree.csv'
while True:
    if vision:
	answer = str(my_raw_input("Export Files to Hartree  y/n ? " ,screen))
	answer = answer.replace('b\'','')
	answer = answer.replace('\'','')

    else:
	if sys.version_info < (3,):  # python 2
	    answer = raw_input("Export Files to Hartree    y/n: ?\n")
	else:
	    answer = str(input("Export Files to Hartree    y/n: ?\n"))
    if answer == 'y':
	latex(fileOutputTex , listProjectMethod[nproject].lista, 5, "hartree")
	csv(fileOutputCsv   , listProjectMethod[nproject].lista, 5, "hartree")
	if vision:
	    screen.clear()
	    printCenter("Generate Hartree Files !",screen)
	    screen.refresh()
	    curses.napms(1000)
	    screen.clear()
	    printTop('*** Working ***',screen)
	else:
	    printElementName('Output Files','*',40)
	    print('Tex File:',fileOutputTex)
	    print('Csv File:',fileOutputCsv)
	    printElement('*',40)
	break
    elif answer == 'n':
	if vision:
	    screen.clear()
	    printTop('*** Working ***',screen)
	break
    else:
	if vision:
	    screen.clear()
	    printTop('*** Working ***',screen)
	    printFooter('Action not valid: ' +  answer ,screen)
	    curses.napms(1000)

	    screen.refresh()
	else:
	    print('Action not valid: ', answer)

fileOutputTex = nameCurrentProject +'_EV.tex'
fileOutputCsv = nameCurrentProject +'_EV.csv'
while True:
    if vision:
	answer = str(my_raw_input("Export Files to eV  y/n ? " ,screen))
	answer = answer.replace('b\'','')
	answer = answer.replace('\'','')

    else:
	if sys.version_info < (3,):  # python 2
	    answer = raw_input("Export Files to eV    y/n: ?\n")
	else:
	    answer = str(input("Export Files to eVe   y/n: ?\n"))

    if answer == 'y':
	latex(fileOutputTex, listProjectMethod[nproject].lista, 5, "eV")
	csv(fileOutputCsv  , listProjectMethod[nproject].lista, 5, "eV")
	if vision:
	    screen.clear()
	    printCenter("Generate eV Files !",screen)
	    screen.refresh()
	    curses.napms(1000)
	    screen.clear()
	    printTop('*** Working ***',screen)
	else:
	    printElementName('Output Files','*',40)
	    print('Tex File:',fileOutputTex)
	    print('Csv File:',fileOutputCsv)
	    printElement('*',40)
	break
    elif answer == 'n':
	if vision:
	    screen.clear()
	    printTop('*** Working ***',screen)
	break
    else:
	if vision:
	    screen.clear()
	    printTop('*** Working ***',screen)
	    printFooter('Action not valid: ' +  answer ,screen)
	    curses.napms(1000)
	    screen.refresh()
	else:
	    print('Action not valid: ', answer)

fileOutputTex = nameCurrentProject +'_KcalMol.tex'
fileOutputCsv = nameCurrentProject +'_KcalMol.csv'

while True:
	
    if vision:
	answer = str(my_raw_input("Export Files to kcal/mol  y/n ? " ,screen))
	answer = answer.replace('b\'','')
	answer = answer.replace('\'','')

    else:
	if sys.version_info < (3,):  # python 2
	    answer = raw_input("Export Files to kcal/mol   y/n: ?\n")
	else:
	    answer = str(input("Export Files to kcal/mol    y/n: ?\n"))

    if answer == 'y':
	latex(fileOutputTex   , listProjectMethod[nproject].lista, 5, "kcal/mol")
	csv(fileOutputCsv     , listProjectMethod[nproject].lista, 5, "kcal/mol")
	if vision:
	    screen.clear()
	    printCenter("Generate kcal/mol Files !",screen)
	    screen.refresh()
	    curses.napms(1000)
	    screen.clear()
	    printTop('*** Working ***',screen)
	else:
	    printElementName('Output Files','*',40)
	    print('Tex File:',fileOutputTex)
	    print('Csv File:',fileOutputCsv)
	    printElement('*',40)
	break
    elif answer == 'n':
	if vision:
	    screen.clear()
	    printTop('*** Working ***',screen)
	break
    else:
	if vision:
	    screen.clear()
	    printTop('*** Working ***',screen)
	    printFooter('Action not valid: ' +  answer ,screen)
	    curses.napms(1000)
	    screen.refresh()
	else:
	    print('Action not valid: ', answer)

fileOutputTex = nameCurrentProject +'_KJMol.tex'
fileOutputCsv = nameCurrentProject +'_KJMol.csv'

while True:
    if vision:
	answer = str(my_raw_input("Export Files to kJ/mol  y/n ? " ,screen))
	answer = answer.replace('b\'','')
	answer = answer.replace('\'','')

    else:
	if sys.version_info < (3,):  # python 2
	    answer = raw_input("Export Files to kJ/mol    y/n: ?\n")
	else:
	    answer = str(input("Export Files to KJ/mol    y/n: ?\n"))

    if answer == 'y':
	latex(fileOutputTex , listProjectMethod[nproject].lista, 5, "kJ/mol")
	csv(fileOutputCsv   , listProjectMethod[nproject].lista, 5, "kJ/mol")
	if vision:
	    screen.clear()
	    printCenter("Generate kJ/mol Files !",screen)
	    screen.refresh()
	    curses.napms(1000)
	    screen.clear()
	    printTop('*** Working ***',screen)
	else:
	    printElementName('Output Files','*',40)
	    print('Tex File:',fileOutputTex)
	    print('Csv File:',fileOutputCsv)
	    printElement('*',40)
	break
    elif answer == 'n':
	if vision:
	    screen.clear()
	    printTop('*** Working ***',screen)
	    break
    else:
	if vision:
	    screen.clear()
	    printTop('*** Working ***',screen)
	    printFooter('Action not valid: ' +  answer ,screen)
	    screen.refresh()
	else:
	    print('Action not valid: ', answer)

if vision:

    curses.napms(2000)
    screen.clear()

    printCenter('Thanks you :) ',screen)
    screen.refresh()
    curses.napms(2000)
    curses.endwin()
else:
    printElement('-',40)
    printElementName('Thanks :)','-',40)
    printElement('-',40)

