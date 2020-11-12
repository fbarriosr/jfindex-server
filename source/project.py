import os
import sys
from source.myPrint import *



class Project:
    name = ""
    files = []
    status = False
    errorMsg = "No message"

    # estados
    s1 = False
    s2 = False
    s3 = False
    s4 = False

    # data s1
    e_L = 0
    e_H = 0
    e_N = 0
    energia = ''

    # data s2
    e_S   = 0
    e_NP1 = 0

    # data s3
    e_NN1 = 0

    # data Inferida
    HLGAP   = 0
    deltaSL = 0
    j_A     = 0
    j_I     = 0
    j_HL    = 0

    def __init__(self, name):
	self.name = name
	aux = name[::-1]
	t1 = aux.find('_')   # right to left
	t1 = len(aux) -1 - t1  # arreglando el puntero 
	self.shortName =  name[0:t1]
	self.dftNumber = name.replace(self.shortName+'_' ,'')

    def getNamePosFile(self):
	aux = self.name+'_N+1.log'
	if self.status:
	    if aux in self.files:
		return aux
	    else:
		return "False"
	else:
	    return "False"

    def getNameNegFile(self):
	aux = self.name+'_N-1.log'
	if self.status:
	    if aux in self.files:
		return aux
	    else:
		return "False"
	else:
	    return "False"

    def getNameMainFile(self):
	aux = self.name+'_N.log'
	if self.status:
	    if aux in self.files:
		return aux
	    else:
		return "False"
	else:
	    return "False"

    def getName(self):
	return self.name
	
    def getShortName(self):
	return self.shortName
		
    def viewName(self):
	print('Name:',self.name)

    def view(self):
	printElement('-',40)
	print('Name:',self.name)
	print('shortname:',self.shortName)
	print('files:',self.files)
	print('status:',self.status)
	print('s1:', self.s1)
	print('s2:', self.s2)
	print('s3:', self.s3)
	print('s4:', self.s4)
	print('error:',self.errorMsg)
	print('S1:')
	print('energia:',self.energia)
	print('e_N:',self.e_N)
	print('e_L:',self.e_L)
	print('e_H:',self.e_H)
	print('S2:')	
	print('e_S:',self.e_S)
	print('e_NP1:',self.e_NP1)
	print('S3:')
	print('e_NN1:',self.e_NN1)
	print('S4:')
	print('HLGAP:',self.HLGAP)
	print('deltaSL:',self.deltaSL)
	print('j_I:',self.j_I)
	print('j_A:',self.j_A)
	print('j_HL:',self.j_HL)

	printElement('-',40)
	return

    def loadingFiles(self, allFilesNames):
	self.files =[]
	for i in range (len(allFilesNames)):
	    if allFilesNames[i].find(self.name) != -1:           # encuentra los archivos del proyecto
		self.files.append(allFilesNames[i])
	#print('files:',self.files)
	return
		
    def checkUnique(self):
	countNPos1 = 0
	countNNeg1 = 0
	count      = 0

	for i in range (len(self.files)):
	    if   self.files[i].find('N+1.log') != -1:
		countNPos1 += 1
	    elif self.files[i].find('N-1.log') != -1:
		countNNeg1 += 1
	    elif self.files[i].find('N.log') != -1:
		count 	   += 1

	#print('file:',self.files)
	#print('countNPos1:',countNPos1)
	#print('countNNeg1:',countNNeg1)
	#print('countN    :',count)


	if (len(self.files)  == 3):
	    if ( (countNPos1 == 1 ) and (countNNeg1 == 1 ) and (count == 1 ) ):
		self.status = True
		self.errorMsg = "No hay errores en los nombres de los archivos"
	    else:
		self.status = False
		self.errorMsg = "Hay errores en los nombres de los archivos"

	elif (len(self.files) == 2):
	    if ( (countNPos1 == 1 ) and (countNNeg1 == 1 )  ):
		self.status = False
		archivo = self.name + "N"
		self.errorMsg = "Hay errores. Te falta el archivo: "+ archivo
	    elif ( (countNPos1 == 1 ) and (count== 1 )  ):
		self.status = False
		archivo = self.name + "N-1"
		self.errorMsg = "Hay errores. Te falta el archivo: "+ archivo
	    elif ( (countNNeg1 == 1 ) and (count== 1 )  ):
		self.status = False
		archivo = self.name + "N+1"
		self.errorMsg = "Hay errores. Te falta el archivo: "+ archivo

	elif (len(self.files) == 1):
	    if ( countNPos1 == 1 )  :
		self.status = False
		archivo1 = self.name 
		archivo2 = self.name + "N-1"
		self.errorMsg = "Hay errores. Te faltan los archivos: "+ archivo1+' y ' + archivo2
	    elif ( countNNeg1 == 1 )  :
		self.status = False
		archivo1 = self.name 
		archivo2 = self.name + "N+1"
		self.errorMsg = "Hay errores. Te faltan los archivos: "+ archivo1+' y ' + archivo2
	    elif ( count == 1 )  :
		self.status = False
		archivo1 = self.name + "N+1"
		archivo2 = self.name + "N-1"
		self.errorMsg = "Hay errores. Te faltan los archivos: "+ archivo1+' y ' + archivo2

	elif (len(self.files)  > 3):
	    self.status = False
	    archivo1 = self.name 
	    archivo2 = self.name + "N+1"
	    archivo3 = self.name + "N-1"
	    self.errorMsg = "Hay errores, se encontraron multiples archivos, solo debes tener 3:"+archivo1+', '+archivo2 +' y '+archivo3
	return

    def stageS1(self):
	if self.status:
	    fileName = self.getNameMainFile()
	    #print('fileName',fileName)
	    with open(fileName) as f:
		lines = f.readlines() #read
		f.close()
	    tSistema = False
	    tLumo    = False
	    tHomo    = False
	    tPopulation = False
	    prevLine  = 0
	    for line in lines:
		if not(tSistema):             # buscamos Sistema
		    if line.upper().find('SCF DONE')!= -1:
			t = line.split()
			self.e_N = float(t[4])
			self.energia =  t[2]
			self.energia = self.energia.replace('E(','')
			self.energia = self.energia.replace(')','')
			#print ('Linea:')
			#print (t)
			#print('energia:',self.energia)
			#print('e_N:',self.e_N)
			tSistema = True
		elif not(tLumo):
		    if not(tPopulation):

			if line.upper().find('POPULATION ANALYSIS USING THE SCF DENSITY') != -1:
			    tPopulation = True
			    #print('Population analysis using the SCF Density:',True)
		    else:
			if line.find('Alpha virt. eigenvalues') != -1:
			    t = line.split()
			    self.e_L = float(t[4])
			    #print ('t:',t)
			    #print('e_L:',self.e_L )
			    tLumo = True
			    p = prevLine.split()
			    self.e_H = float(p[len(p)-1])
			    #print ('t:',t)
			    #print('e_H:',self.e_H )
			    tHomo = True
		elif tSistema and tHomo and tLumo:
		    self.s1 = True
		    return True

		prevLine = line
	else:
	    return False

    def stageS2(self):
	if self.status and self.s1:
	    fileName = self.getNamePosFile()
	    with open(fileName) as f:
		lines = f.readlines() #read
		f.close()
	    tSistema = False
	    tSomo    = False

	    tPopulation = False
	    prevLine  = 0
	    for line in lines:
		if not(tSistema):             # buscamos Sistema
		    if line.upper().find('SCF DONE')!= -1:
			t = line.split()
			self.e_NP1 = float(t[4])
			tSistema = True
		elif not(tSomo):
		    if not(tPopulation):
			if line.upper().find('POPULATION ANALYSIS USING THE SCF DENSITY') != -1:
			    tPopulation = True
		    else:
			if line.find('Alpha virt. eigenvalues') != -1:
			    p = prevLine.split()
			    self.e_S = float(p[len(p)-1])
			    tSomo = True
		elif tSistema and tSomo:
		    self.s2 = True
		    return True

		prevLine = line
	else:
	    return 	False

    def stageS3(self):
	if self.status and self.s1 and self.s2:
	    fileName = self.getNameNegFile()
	    with open(fileName) as f:
		lines = f.readlines() #read
		f.close()
	    tSistema = False
	    for line in lines:
		if not(tSistema):             # buscamos Sistema
		    if line.upper().find('SCF DONE')!= -1:
			t = line.split()
			self.e_NN1 = float(t[4])
			tSistema = True
		elif tSistema:
		    self.s3 = True
		    return True
	else:
	    return False

    def stageS4(self):
	if self.status and self.s1 and self.s2 and self.s3:
	    self.HLGAP   	= self.e_L - self.e_H
	    self.deltaSL 	= abs(self.e_L - self.e_S)
	    self.j_I     	= abs(self.e_H + self.e_NN1 - self.e_N )
	    self.j_A    	= abs(self.e_L + self.e_N - self.e_NP1 )
	    self.j_HL    	= pow( ( pow(self.j_I ,2) + pow(self.j_A,2) ), 0.5 )
	    self.desviation = self.deltaSL/self.e_H
	    self.s4      = True
	else:
	    return False

    def valuesHartree(self,cifras):
	lista =[]
	lista.append(self.energia+'('+ self.shortName+')')
	lista.append(str(round(self.e_H ,cifras)))
	lista.append(str(round(self.e_L ,cifras)))
	lista.append(str(round(self.e_S ,cifras)))
	lista.append(str(round(self.HLGAP ,cifras)))
	lista.append(str(round(self.j_I,cifras)))
	lista.append(str(round(self.j_A ,cifras)))
	lista.append(str(round(self.j_HL ,cifras)))
	lista.append(str(round(self.deltaSL ,cifras)))
	return lista
		
    def valuesEV(self,cifras):
	eV = 27.2116
	lista =[]
	lista.append(self.energia+'('+ self.shortName+')')
	lista.append(str(round(eV * self.e_H ,cifras)))
	lista.append(str(round(eV * self.e_L ,cifras)))
	lista.append(str(round(eV * self.e_S ,cifras)))
	lista.append(str(round(eV * self.HLGAP ,cifras)))
	lista.append(str(round(eV * self.j_I,cifras)))
	lista.append(str(round(eV * self.j_A ,cifras)))
	lista.append(str(round(eV * self.j_HL ,cifras)))
	lista.append(str(round(eV * self.deltaSL ,cifras)))
	return lista

    def valuesKcalMol(self,cifras):
	kcalMol = 627.5095
	lista =[]
	lista.append(self.energia+'('+ self.shortName+')')
	lista.append(str(round(kcalMol  * self.e_H ,cifras)))
	lista.append(str(round(kcalMol  * self.e_L ,cifras)))
	lista.append(str(round(kcalMol  * self.e_S ,cifras)))
	lista.append(str(round(kcalMol  * self.HLGAP ,cifras)))
	lista.append(str(round(kcalMol  * self.j_I,cifras)))
	lista.append(str(round(kcalMol  * self.j_A ,cifras)))
	lista.append(str(round(kcalMol  * self.j_HL ,cifras)))
	lista.append(str(round(kcalMol  * self.deltaSL ,cifras)))
	return lista

    def valuesKJMol(self,cifras):
	KJMol = 2625.4997
	lista =[]
	lista.append(self.energia+'('+ self.shortName+')')
	lista.append(str(round(KJMol  * self.e_H ,cifras)))
	lista.append(str(round(KJMol  * self.e_L ,cifras)))
	lista.append(str(round(KJMol  * self.e_S ,cifras)))
	lista.append(str(round(KJMol  * self.HLGAP ,cifras)))
	lista.append(str(round(KJMol  * self.j_I,cifras)))
	lista.append(str(round(KJMol  * self.j_A ,cifras)))
	lista.append(str(round(KJMol  * self.j_HL ,cifras)))
	lista.append(str(round(KJMol  * self.deltaSL ,cifras)))
	return lista

    def labels(self):
	lista = []
	lista.append('Density Functional')
	lista.append('E_H')
	lista.append('E_L')
	lista.append('E_S')
	lista.append('HLGAP')
	lista.append('J_I')
	lista.append('J_A')
	lista.append('J_HL')
	lista.append('Delta_SL')
	return lista

class ProjectMethod:
    def __init__(self, name):
	self.name = name
	self.lista = []

    def appendProject(self,project):
	self.lista.append(project)
	return 0

    def view(self):
	printElement('-',40)
	print('Project:',self.name)
	if len(self.lista) != 0:
	    for list in self.lista:
		print('Methods:',list.name)	
	else:
	    print('Without Methods')
    def getName(self):
	return self.name

		
def checker(message):
    if message == "":
	inputt = input()
    else:
	inputt = input(message+'\n')
    try:
	return int(inputt)
    except ValueError:
	print ("Error!, Enter a number!")
	return checker("")

