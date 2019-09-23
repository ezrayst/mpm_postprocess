# Import libraries
import datetime
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Specify directories
working_directory = ['bin/iverson-2d-experiment/']
# Input Files
input_filename_prefix = 'particles'
input_filename_suffix = '000.h5'

# Add input
ntime = 126
dt = 0.001
point_id = [0];

# Preallocate variables
time = np.zeros((ntime + 1, 1))
coord = np.zeros((ntime + 1, len(working_directory)))

for k in range(0, len(working_directory), 1):

	# Output files
	output_directory = working_directory[k] + 'results/'
	output_prefix_filename = 'stress'
	output_suffix_filename = '.vtp'
	if not os.path.exists(output_directory):
		os.makedirs(output_directory)
	print("directory of files: " + output_directory)
	
	# Loop all the .h5 files
	for index in range(0, ntime + 1, 1):
	
		# Index multiplication
		#f k < 2:
		#	multiplication = 1
		#elif k < 4:
		#	multiplication = 2
		#else:
		#	multiplication = 4
		multiplication = 1
		index_mult = index * multiplication;

		# Prefix number of input file
		if index_mult < 10:
			zeros = '000'
		elif index_mult < 100:
			zeros = '00'
		else:
			zeros = '0'

		# Concatenate filename
		input_filename = working_directory[k] + input_filename_prefix + zeros + str(index_mult) + input_filename_suffix
		output_filename = output_directory + output_prefix_filename + str(index_mult)
	
		# Read HDF5 - df refers to DataFrame
		df = pd.read_hdf(input_filename)
	
		# Make np.array
		coord_x = np.array(df['coord_x'])
		coord_y = np.array(df['coord_y'])
		#coord_z = np.array(df['coord_z'])
		#stress_xx = np.array(df['stress_xx'])
		#stress_yy = np.array(df['stress_yy'])
		#stress_zz = np.array(df['stress_zz'])
		#tau_xy = np.array(df['tau_xy'])
		#strain_xx = np.array(df['strain_xx'])
		#strain_yy = np.array(df['strain_yy'])
		#strain_zz = np.array(df['strain_zz'])
	
		# Make data to store
		#for j in range(0, len(coord_x), 1):
			#coord[index, k] = max(coord_x[point_id[j]]	
		coord[index, k] = max(coord_x);

		# Prompt to make sure it's OK
		print(input_filename + " has been read at " + str(datetime.datetime.now()))
	
		# Update time
		time[index] = index * dt;
	
		# Update index for next time step
		index += 1


coord_save = np.zeros((50, 1))
for i in range(0, 12, 1):
	coord_save[i, 0] = coord[i * 10, 0]

np.savetxt('data.csv', coord_save, delimiter=',')

# Plot
line1, = plt.plot(time, coord[:, [0]] * 100, 'r', label='USF Case 1')
#line2, = plt.plot(time, stress[:, [1]], 'c--', label='USL Case 1')
#line3, = plt.plot(time, stress[:, [2]], 'g', label='USF Case 2')
#line4, = plt.plot(time, stress[:, [3]], 'm--', label='USL Case 2')
#line5, = plt.plot(time, stress[:, [4]], 'g', label='USF Case 3')
#line6, = plt.plot(time, stress[:, [5]], 'y--', label='USL Case 3')
#plt.axis([0, 0.20, -3000, 0])
plt.xlabel('Time (s)')
plt.ylabel('location in Longitunal (cm)')
#plt.legend(handles=[line1, line2, line3, line4, line5, line6])
plt.show()


