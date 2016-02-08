'''
Ing. Ivan Morales
Lab. Circuitos Electricos
Escuela de Ciencias Fisicas y Matematicas
Universidad de San Carlos de Guatemala
February 2016

USAGE
-------------------------
1) Modify the function according to your needs. If a special function is required (i.e. cos, sin, exp) math module should be invoqued first.
2) Modify the parameters to run the script and generate some random data based on the seed function. You may find these values at the end of this file.
-------------------------
'''

import random
import math

class randomFit(object):

	def function(self, x):
	
		#------------------ MODIFY THIS FUNCTION ------------------#
		y = -1*x**2 + 2*x + 9 #Modify this line so it can be used as a seed function to generate the random data values
		#y = math.exp(-0.3*x)*math.cos(0.9*x) #Another (more complex) random seed function using Python's Math library for special functions
		#------------------ MODIFY THIS FUNCTION ------------------#
		return y

	def __init__(self, minLimit, maxLimit, step, xError, maxDev = 0.05, yError = 0): #Do not modify anything here
		self.minLimit = minLimit
		self.maxLimit = maxLimit
		self.step = step
		self.maxDev = maxDev
		self.xError = xError
		self.yError = yError

	def getLimits(self):
		return (self.minLimit, self.maxLimit, self.step)

	def getMaxDev(self):
		return self.maxDev
		
	def getXError(self):
		return self.xError()
		
	def getYError(self, yValue = 0):
		if self.yError:
			return self.yError()
		else:
			return yValue*self.getMaxDev()

	def computeXRange(self):
		x =[]
		minLimit, maxLimit, step = self.getLimits()
		N = int((maxLimit - minLimit) / step)
		for i in range(N):
			x.append(minLimit + i*step)
		return x
			
	def computeFunctionValues(self, xRange):
		y = []
		maxDev = self.getMaxDev()
		for i in xRange:
			y.append(random.uniform(self.function(i)*(1 - maxDev), self.function(i)*(1 + maxDev)))
		return y
		
	def computeYErrorValues(self):
		xRange = self.computeXRange()
		yValues = self.computeFunctionValues(xRange)
		yErrors = []
		for i in yValues:
			yErrors.append(self.getYError(i))
		return yErrors
			
		

class fileManagement(object):

	SPLITTER = ' '

	def __init__(self, data, columnNames = ('x', 'y'), fileName = 'data.txt'):
		self.f = open(fileName, 'w')
		self.data = data
		for i in columnNames:
			self.f.write(i + self.SPLITTER)
		self.f.write('\n')
		self.appendData()
		self.f.close()

	def getFile(self):
		return self.f

	def getData(self):
		return self.data

	def appendData(self):
		f = self.getFile()
		data = self.getData()
		for i in range(len(data[0])):
			for j in range(len(data)):
				f.write(str(data[j][i]) + self.SPLITTER)
			f.write('\n')


#------------------ MODIFY THESE VALUES ------------------#
minRange = -4 #Min x-axis plot value
maxRange = 6 #Max x-axis plot value
step = 0.5 #How many points shall you get?
xError = 0.2 #Arbitrary absolute x-value uncertainty		
maxDeviation = 0.25 #Relative y-value (percent) error
#------------------ MODIFY THESE VALUES ------------------#
		

a = randomFit(minRange, maxRange, step, xError, maxDeviation)
xValues = a.computeXRange()
yValues = a.computeFunctionValues(xValues)
xErrorValues = [xError for i in range(len(xValues))]
yErrorValues = a.computeYErrorValues()
run = fileManagement((xValues, yValues, xErrorValues, yErrorValues), ('x', 'y', 'xEr', 'yEr')) #Column names (x, y, x-Error, y-Error, etc...)
