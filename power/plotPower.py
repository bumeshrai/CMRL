import matplotlib.pyplot as plt, csv, datetime as dt, numpy as np #import libraries

#Initialise empty array
xA = []
yA = []
zA = []
xK = []
yK = []
zK = []
yT = []
curveType = []

curveType = raw_input('Type (1) for Regression Curve'+'\n'+'\t'+'And (2) otherwise '+'\t')

#Read from file and store selected data in arrays
with open ('powerPlot.csv','r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	for row in plots:
		if row[2] == 'ARSS':
			xA.append(row[1])
			yA.append(int(row[5]))
		if row[2] == 'KRSS':
			xK.append(row[1])
			yK.append(int(row[5]))

#Format to python format of dates
for day in xA:
	zA.append(dt.datetime(int(day[0:4]),int(day[5:7]),int(day[8:10])))

for day in xK:
	zK.append(dt.datetime(int(day[0:4]),int(day[5:7]),int(day[8:10])))

#Transform to numpy arrays for elementwise addition in arrays
yA = np.array(yA)
yK = np.array(yK)
yT = yA+yK

if curveType == '1':
#Regression curve
	r = np.arange(len(yT)) 		#array representing the number of elements
	m, b = np.polyfit(r,yT,1)	#fit 1 degree of polynomial
	plt.plot(r, m*r+b)
	plt.plot(r, yT)
else:
#Plot the raw data
	plt.plot(zK, yT, label = 'Total Power Consumption')
	plt.plot(zA, yA, label = 'Power Consumption at ARSS')
	plt.plot(zK, yK, label = 'Power Consumption at KRSS')

#Show the graph
plt.xlabel('Day')
plt.ylabel('KWH consumption')
plt.title(r'Daily energy consumption')
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()


