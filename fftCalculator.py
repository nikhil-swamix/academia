import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import inspect
import changefinder


def simpleGraph(y,x=0):
	plt.plot(y)
	plt.ylabel('data from {}'.format(thisfunc()))
	plt.show()
	pass
def thisfunc(level=1,span=3):
	return inspect.stack()[level][span]

class machine:
	def __init__(self,name):
		self.name=name
		print("Machine {} initialized".format(name))

	def set_logfile(self,path):
		self.path = path
		self.df = pd.read_csv(path)
		print('Machine \"{}\" loaded from file >> {}'.format(self.name,path))

	def show_log(self):
		try:
			dataset=self.df
			print("displaying Log Contents from >> {}".format(self.path))
			print(self.df.head()) 
		except :
			print("Execute {}.set_logfile(path) before using function => {} ".format(__class__.__name__,thisfunc()))


	def log_metrics(self):
		try:
			dataset=self.df
			# d= caching result for prnt and return to save computing
			d=self.df.describe() 	
			d.loc['var'] = d.var()
			d.loc['skew'] = d.skew()
			d.loc['kurt'] = d.kurtosis()
			print(type(d),d)
			return d
		except :
			print("Execute {}.set_logfile(path) before using function => {} ".format(__class__.__name__,thisfunc()))

	def realtimeSTFT(self,windowSamples=1000,step=1,interval=30):
		windowSamples=windowSamples
		Y_Axis=self.df['Vibration_Az'][220000:300000] #the vibration starts approximately here
		X_Axis=np.arange(0, len(Y_Axis),0.01)
		# Y_Axis=np.sin(X_Axis*np.pi*2)+np.sin(X_Axis*np.pi)

		def calculate_fft( window ):
			fft= np.fft.fft(Y_Axis[:windowSamples])
			return np.absolute(fft)

		def dynamic_fft(window,slider):
			fft= np.fft.fft(Y_Axis[slider:windowSamples+slider])
			return np.absolute(fft)

		def plot(graph,xdata,ydata):
			p=graph.plot(xdata, ydata, "-g", animated=True,label='First Line')[0]
			# print(p)
			return p

		def animate(i):
			#moving window i is moving it
			graph1.set_data(X_Axis[:windowSamples],Y_Axis[i:windowSamples+i]) 
			DynamicWindowFFT=dynamic_fft(Y_Axis[:windowSamples],i)
			graph2.set_data(X_Axis[:windowSamples],DynamicWindowFFT)
			return multiGraphObject

		fig, axes = plt.subplots(nrows=2)
		fig.suptitle('Data and FFT')
		# axes[0].set_xlim(-10, 110)
		axes[0].set_xlabel('Sample Space')
		graph1=plot(axes[0],X_Axis[:windowSamples],Y_Axis[:windowSamples]);
		graph2=plot(axes[1],X_Axis[:windowSamples],calculate_fft(Y_Axis[:windowSamples]))

		multiGraphObject=[]
		multiGraphObject.append(graph1)
		multiGraphObject.append(graph2)
		ani = animation.FuncAnimation(fig, animate, range(1, len(Y_Axis)-windowSamples,step),interval=interval, blit=True)
		plt.show()

	def faultFinder(self):
		try:
			df=self.df
		except :
			print("Execute {}.set_logfile(path) before using function => {} ".format(__class__.__name__,thisfunc()))
			return

		y=df['Vibration_Az']

		def weightedRollingAverage(array,samples):
			RA=[]
			window=[]
			for i in range(len(array)):
				window=array[i:i+samples]
				np.average(window)
				
			return RA

		simpleGraph(y)




machineABC=machine('machineABC')
machineABC.set_logfile("Vibration.csv")
machineABC.show_log()
machineABC.log_metrics()

faulty_areas=machineABC.faultFinder()
print(faulty_areas)
# machine.realtimeSTFT(windowSamples=2000,step=10,interval=1)

