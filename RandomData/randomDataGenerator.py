import random
import math

class randomFit(object):

	def function(self, x):
		y = -1*x**2 + 2*x + 9 #Modify this function 
		#y = math.exp(-0.3*x)*math.cos(0.9*x)
		return y

	def __init__(self, minLimit, maxLimit, step, xError, maxDev = 0.05, yError = 0): #Set Max Y-Values Error here (maxDev) in %
		self.minLimit = minLimit
		self.maxLimit = maxLimit
		self.step = step
		self.maxDev = maxDev #% of deviation for current fucntion valued on x
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


minRange = -4 #Min x-axis plot value
maxRange = 6 #Max x-axis plot value
step = 0.5 #How many points shall you get?
xError = 0.2 #Arbitrary absolute x-value uncertainty		
maxDeviation = 0.25 #Relative y-value (percent) error
		

a = randomFit(minRange, maxRange, step, xError, maxDeviation)
xValues = a.computeXRange()
yValues = a.computeFunctionValues(xValues)
xErrorValues = [xError for i in range(len(xValues))]
yErrorValues = a.computeYErrorValues()
run = fileManagement((xValues, yValues, xErrorValues, yErrorValues), ('x', 'y', 'xEr', 'yEr')) #Column names (x, y, x-Error, y-Error, etc...)
