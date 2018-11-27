import numpy as np
import matplotlib.pyplot as plt
import csv
import matplotlib.patches as patches
import sys


def visualize(file_name, plot_type, index):
	print("plot_type", plot_type)
	print("index", index)
	index = int(index)
	arena_size = (800,800)


	#fig2 = plt.figure(figsize=(7,7))

	fig2 = plt.figure()
	ax2 = fig2.add_subplot(111, aspect='equal')


	#plt.axis((ax2[0],ax2[1],ax2[3],ax2[2]))

	#ax2.set_facecolor('xkcd:salmon')

	#draw rectable of view
	ax2.add_patch(
	     patches.Rectangle(
	        (0, 0),
	        arena_size[0],
	        arena_size[0],
	        fill=False
	     ) )

	plt.xlim(-10, arena_size[0]+10)
	plt.ylim(-10, arena_size[0]+10)

	#Get data
	opened_file = open(file_name)


	df_x = []
	df_y = []

	if(plot_type=="latest"):
		last_row = list(csv.reader(opened_file))[-1]
		print(last_row)
		for ind in range(2,len(last_row)):
			if(not (not last_row[ind])):
			    data = last_row[ind][1:-1].split(",")
			    df_x.append(float(data[0]))
			    df_y.append(float(data[1]))


	if(plot_type=="index"):

		with open(file_name, newline='') as csvfile:
			loc_reader = csv.reader(csvfile)
			for row in loc_reader:
				if row != []:

					if row[0] == str(index):
						#print("got to index")

						locs = list(row[1:])
						spots = eval(locs[0])

		for index in spots:				#spots is a list of tuples, each tuple is (x,y) coridnate of bee

			df_x.append(float(index[0]))	#df_x is list of x cordinates
			df_y.append(float(index[1]))	#df_y is list of y cordinates

		t = np.linspace(0,len(df_x),len(df_x))
		plt.scatter(df_x, df_y, c=t,cmap=plt.get_cmap("cool"), alpha=0.8)
		plt.plot(df_x, df_y)
		plt.colorbar()
		plt.show()

	'''

	#plt.figure(figsize=(10,10))
	if(plot_type=="all"):

		#index is the id number
		for row in list(csv.reader(f)):
			df_x = []
			df_y = []
			#print(len(row))
			#print(row)
			for ind in range(1,len(row)):
			    #print(ind)
			    if(not (not row[ind])):

				    data = row[ind][1:-1].split(",")
				    #print(data)
				    #print(str(data))
				    #print(str(data).is_empty())
				    df_x.append(float(data[0]))
				    df_y.append(float(data[1]))

			plt.scatter(df_x, df_y, alpha=0.2)
			plt.plot(df_x, df_y, alpha=0.2)

			#t=np.linspace(0,len(df_x),len(df_x))
			#plt.scatter(df_x, df_y, c=t,cmap=plt.get_cmap("viridis"))

			#plt.plot(df_x, df_y)
		#plt.colorbar()
		plt.show()

		else:
			t  =np.linspace(0,len(df_x),len(df_x))
			plt.scatter(df_x, df_y, c=t,cmap=plt.get_cmap("cool"), alpha=0.8)
			plt.plot(df_x, df_y)
			plt.colorbar()
			plt.show()
			'''


	def saveVisualization(file_name, plot_type, index):
		index = int(index)
		arena_size = (800,800)
		fig2 = plt.figure()
		ax2 = fig2.add_subplot(111, aspect='equal')

		#draw rectable of view
		ax2.add_patch(
		     patches.Rectangle(
		        (0, 0),
		        arena_size[0],
		        arena_size[0],
		        fill=False
		     ) )

		plt.xlim(-10, arena_size[0]+10)
		plt.ylim(-10, arena_size[0]+10)

		#Get data
		f = open(file_name)
		df_x = []
		df_y = []
		if(plot_type=="latest"):
			last_row = list(csv.reader(f))[-1]
			print(last_row)
			for ind in range(2,len(last_row)):
				if(not (not last_row[ind])):
				    data = last_row[ind][1:-1].split(",")
				    df_x.append(float(data[0]))
				    df_y.append(float(data[1]))

		if(plot_type=="index"):
			last_row = list(csv.reader(f))[index]
			for ind in range(1,len(last_row)):
				if(not (not last_row[ind])):
				    data = last_row[ind][1:-1].split(",")
				    df_x.append(float(data[0]))
				    df_y.append(float(data[1]))

		#plt.figure(figsize=(10,10))
		if(plot_type=="all"):
			#print(len(list(csv.reader(f))))
			for row in list(csv.reader(f)):
				df_x = []
				df_y = []
				#print(len(row))
				#print(row)
				for ind in range(1,len(row)):
				    #print(ind)
				    if(not (not row[ind])):

					    data = row[ind][1:-1].split(",")
					    #print(data)
					    #print(str(data))
					    #print(str(data).is_empty())
					    df_x.append(float(data[0]))
					    df_y.append(float(data[1]))

				plt.scatter(df_x, df_y, alpha=0.2)
				plt.plot(df_x, df_y, alpha=0.2)

				#t=np.linspace(0,len(df_x),len(df_x))
				#plt.scatter(df_x, df_y, c=t,cmap=plt.get_cmap("viridis"))

				#plt.plot(df_x, df_y)
			#plt.colorbar()
			return plt

		else:
			t=np.linspace(0,len(df_x),len(df_x))
			plt.scatter(df_x, df_y, c=t,cmap=plt.get_cmap("cool"), alpha=0.8)
			plt.plot(df_x, df_y)
			plt.colorbar()
			return plt
# main
# if(len(sys.argv) < 2):
# 	print("Please specify file name")
# 	exit()
# elif(len(sys.argv) < 3):
# 	file_name= sys.argv[1]
# 	plot_type= "latest"
# else:
# 	file_name= sys.argv[1]
# 	plot_type= str.lower(sys.argv[2])
# 	if(len(sys.argv) < 4):
# 		if(plot_type == "index"):
# 			print("Please specify index of path to plot")
# 			exit()
# 	else:
# 		index = int(sys.argv[3])

#visualize(file_name, plot_type, index)
