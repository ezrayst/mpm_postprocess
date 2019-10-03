# Import libraries
import datetime
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Specify directories
working_directory = ['5000_2/results/iverson_2d_test/']
# Input Files
input_filename_prefix = 'particles'
input_filename_suffix = '.h5'

# Add input
ntime = 10000
dt = 0.000001
point_id = [159, 160, 161, 162, 173, 174, 175, 176, 188, 189, 203, 204];

# Preallocate variables
time = np.zeros((ntime + 1, 1))
strain = np.zeros((ntime + 1, 3 * len(point_id)))

for k in range(0, len(working_directory), 1):

	# Loop all the .h5 files
	for index in range(0, ntime + 1, 1):
	
		multiplication = 1
		index_mult = index * multiplication;

		# Prefix number of input file
		if index_mult < 10:
			zeros = '0000'
		elif index_mult < 100:
			zeros = '000'
		elif index_mult < 1000:
			zeros = '00'
		elif index_mult < 10000:
			zeros = '0'
		else:
			zeros = ''

		# Concatenate filename
		input_filename = working_directory[k] + input_filename_prefix + zeros + str(index_mult) + input_filename_suffix
	
		# Read HDF5 - df refers to DataFrame
		df = pd.read_hdf(input_filename)
	
		# Make np.array
		#coord_x = np.array(df['coord_x'])
		#coord_y = np.array(df['coord_y'])
		#coord_z = np.array(df['coord_z'])
		#stress_xx = np.array(df['stress_xx'])
		#stress_yy = np.array(df['stress_yy'])
		#stress_zz = np.array(df['stress_zz'])
		#tau_xy = np.array(df['tau_xy'])
		strain_xx = np.array(df['strain_xx'])
		strain_yy = np.array(df['strain_yy'])
		#strain_zz = np.array(df['strain_zz'])
		gamma_xy = np.array(df['gamma_xy'])

		# Make data to store
		for j in range(0, len(point_id), 1):
			strain[index, j * 3]     = strain_xx[point_id[j]]
			strain[index, j * 3 + 1] = strain_yy[point_id[j]]
			strain[index, j * 3 + 2] = gamma_xy[point_id[j]]
	
		# Prompt to make sure it's OK
		print(input_filename + " has been read at " + str(datetime.datetime.now()))
	
		# Update time
		time[index] = index * dt;
	
		# Update index for next time step
		index += 1

# Write output
output_filename1 = 'strain_study.txt'
np.savetxt(output_filename1, strain, fmt="%.16f")


