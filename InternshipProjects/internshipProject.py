import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import inspect
import changefinder


def simpleGraph(y,x=0,label="lable not set"):
	plt.plot(y)
	plt.ylabel('data from {}'.format(label))
	plt.show()

def thisfunc(level=1,span=3):
	return inspect.stack()[level][span]

class machine:
	def __init__(self,name):
		#subclass init
		self.debug=self.debug(self)
		#assign name
		self.name=name
		print("Machine {} initialized".format(name))

	class debug:
		def __init__(self,self1):
			#parent self passing
			self.self=self1

		def get_fault_points(self,showgraph=True):
			try:
				df=self.self.df
				y=df['Vibration_Az']
			except :
				print("Execute {}.set_log(path) before using function => {} "
					.format(self.self.__class__.__name__,thisfunc()))
				return

			def show_graph(averagedInputs,showgraph):
				if showgraph:
					for i,avginp in enumerate(averagedInputs):
						plt.plot(avginp["array"], label = "line{}".format(i))
					plt.show()

			def common_values(array2D):
				#performs mathematical intersection on items
				arrayset=[set(x) for x in array2D]
				return sorted(list(set.intersection(arrayset[0],*arrayset)))

			def rolling_average_step(array,step=100): 
			#step wise implementation of rolling average
				RA=[]
				window=[]
				for i in range(0,len(array),step):
					try:
						window=array[i:i+step]
						calculated=np.full(step,np.average(np.var(window)))
						RA.extend(calculated)
					except Exception as e:
						print(thisfunc() + str(e))
						break
				return {"array":RA,"step":step}
			
			def generateRAS(): #arrays with various rolling_average_step applied on same data | RAS = rolling avg step
				averagedInputs=[]
				for i in range(1,2):
					averagedInputs.append(rolling_average_step(y,3000*i))
				return averagedInputs

			def analyseRAS(averagedInputs):
				#will return highly suspicious points where fault may be present
				suspiciousPoints=[[] for x in averagedInputs]
				for i,avginp in enumerate(averagedInputs):
					prev=0;
					for k,val in enumerate(avginp['array']) :
						if val > prev and val > 3 * prev :
							suspiciousPoints[i].append(k)
						prev=val

				return suspiciousPoints

			averagedInputs = 	generateRAS()
			suspiciousPoints = 	common_values(analyseRAS(averagedInputs))
			print("\n\nFAULT STARTED FROM",suspiciousPoints)
			#PLOT ALL AVERAGES GRAPH
			show_graph(averagedInputs,showgraph=showgraph)


	def set_log(self,path):
		self.path = path
		self.df = pd.read_csv(path)
		# self.debug=self.debug(self)
		print('Machine \"{}\" loaded from file >> {}'.format(self.name,path))

	def show_log(self):
		try:
			dataset=self.df
			print("\n\ndisplaying Log Contents from >> {}".format(self.path))
			print(self.df.head(3)) 
		except :
			print("Execute {}.set_log(path) before using function => {} ".format(__class__.__name__,thisfunc()))

	def get_data_features(self):
		try:
			dataset=self.df
			# d= caching result for prnt and return to save computing
			d=dataset.describe() 	
			d.loc['var'] = d.var()
			d.loc['skew'] = d.skew()
			d.loc['kurt'] = d.kurtosis()
			dataset['describe']=d
			print("\n\nFEATURES OF DATASET\n",d,sep='\n')
			return d
		except Exception as e:
			print("Execute {}.set_log(path) before using function => {} ".format(__class__.__name__,thisfunc()))
			print(e)

	def realtimeSTFT(self,windowSamples=1000,step=1,interval=30):
		windowSamples=windowSamples
		Y_Axis=self.df['Vibration_Az'][220000:300000] #the vibration starts approximately here
		X_Axis=np.arange(0, len(Y_Axis),0.01)

		def calculate_fft(window):
			#here window argument refers to the sliced window on which fft needs to be calculated
			fft= np.fft.fft(Y_Axis[:windowSamples])
			return np.absolute(fft)

		def window_fft(window,slider):
			#here window argument refers to the sliced window on which fft needs to be calculated
			fft= np.fft.fft(Y_Axis[slider:windowSamples+slider])
			return np.absolute(fft)

		def plot(graph,xdata,ydata):
			p=graph.plot(xdata, ydata, "-g", animated=True,label='First Line')[0]
			# print(p)
			return p

		def initGraph():
			def animate(i):
				#moving window i is moving it
				graph1.set_data(X_Axis[:windowSamples],Y_Axis[i:windowSamples+i]) 
				DynamicWindowFFT=window_fft(Y_Axis[:windowSamples],i)
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
		initGraph()


	def shortFFT(self,start=0,end=0):
		return np.fft.fft(self.df['Vibration_Az'][start:end])

	def fullFFT(self):
		y=self.df['Vibration_Az']
		fft=np.absolute(np.fft.fft(y))
		topFrequencies=fft[0:int(len(fft)/2)].argsort()[-10:] # halving because symmetry
		print("\nTOP FREQUENCIES IN FFT ARE" , topFrequencies)
		plt.plot(fft)
		plt.title("FFT ANALYSIS")
		plt.show()
		return topFrequencies

	

machineABC=machine('machineABC')
machineABC.set_log("Vibration.csv")
machineABC.show_log()
machineABC.get_data_features()
machineABC.debug.get_fault_points(showgraph=True)
machineABC.fullFFT()
#Oscilloscope to manually inspect whats happening when
machineABC.realtimeSTFT(windowSamples=2000,step=10,interval=1)
	







