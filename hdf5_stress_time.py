# Import libraries
import datetime
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Specify directories
working_directory = ['bin/small-usf/']
# Input Files
input_filename_prefix = 'particles'
input_filename_suffix = '0.h5'

# Add input
ntime = 99
dt = 0.00001
point_id = [4861];

# Preallocate variables
time = np.zeros((ntime + 1, 1))
stress = np.zeros((ntime + 1, len(working_directory)))

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
		if k < 2:
			multiplication = 1
		elif k < 4:
			multiplication = 2
		else:
			multiplication = 4

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
		#coord_x = np.array(df['coord_x'])
		#coord_y = np.array(df['coord_y'])
		#coord_z = np.array(df['coord_z'])
		stress_xx = np.array(df['stress_xx'])
		stress_yy = np.array(df['stress_yy'])
		#stress_zz = np.array(df['stress_zz'])
		#tau_xy = np.array(df['tau_xy'])
		#strain_xx = np.array(df['strain_xx'])
		#strain_yy = np.array(df['strain_yy'])
		#strain_zz = np.array(df['strain_zz'])
	
		# Make data to store
		for j in range(0, len(point_id), 1):
			stress[index, k] = np.sqrt(np.square(stress_xx[point_id[j]]) + np.square(stress_yy[point_id[j]]))	
	
		# Prompt to make sure it's OK
		print(input_filename + " has been read at " + str(datetime.datetime.now()))
	
		# Update time
		time[index] = index * dt;
	
		# Update index for next time step
		index += 1

# Plot
line1, = plt.plot(time, stress[:, [0]], 'r', label='USF Case 1')
#plt.axis([0, 0.0005, -3000, 0])
plt.xlabel('Time (s)')
plt.ylabel('Stress Magnitude (Pa)')
plt.legend(handles=[line1, line2, line3, line4, line5, line6])
plt.show()


