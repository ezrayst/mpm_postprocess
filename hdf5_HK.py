# Import libraries
import datetime
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Specify directories
working_directory = ['../results/HKC1-rigid/']
# Input Files
input_filename_prefix = 'particles'
input_filename_suffix = '00.h5'

# Add input
# Total time is 2000, sampe every 50
ntime = 50
multiplication = 10
dt = 0.1

# Preallocate variables
time = np.zeros((ntime + 1, 1))
coord = np.zeros((ntime + 1, 3 * len(working_directory)))
velocity = np.zeros((ntime + 1, 3 * len(working_directory)))

for k in range(0, len(working_directory), 1):
	
	# Loop all the .h5 files
	for index in range(0, ntime + 1, 1):

		# Index multiplication
		index_mult = index * multiplication;

		# Prefix number of input file
		if index_mult < 10:
			zeros = '000'
		elif index_mult < 100:
			zeros = '00'
		elif index_mult < 1000:
			zeros = '0'
		else: 
		    zeros = ''

		# Concatenate filename
		input_filename = working_directory[k] + input_filename_prefix + zeros + str(index_mult) + input_filename_suffix
	
		# Read HDF5 - df refers to DataFrame
		df = pd.read_hdf(input_filename)
	
		# Make np.array
		coord_x = np.array(df['coord_x'])
		coord_y = np.array(df['coord_y'])
		coord_z = np.array(df['coord_z'])
		velocity_x = np.array(df['velocity_x'])
		velocity_y = np.array(df['velocity_y'])
		velocity_z = np.array(df['velocity_z'])		
		#stress_xx = np.array(df['stress_xx'])
		#stress_yy = np.array(df['stress_yy'])
		#stress_zz = np.array(df['stress_zz'])
		#tau_xy = np.array(df['tau_xy'])
		#strain_xx = np.array(df['strain_xx'])
		#strain_yy = np.array(df['strain_yy'])
		#strain_zz = np.array(df['strain_zz'])
	
		# Make matrix
		matrix = np.column_stack((coord_x, coord_y, coord_z, velocity_x, velocity_y, velocity_z))

		# Get sort
		# matrix.sort(axis = 2)
		matrix = matrix[matrix[:, 2].argsort()]
		length_points = len(coord_z)
		frontband1_point = round(0.01 * length_points)
		frontband2_point = round(0.00 * length_points)
		print(length_points)
		# print(matrix[frontband2_point:frontband1_point, 3])

		# Make data to store
		# coord[index, k * 3    ] = np.median(matrix[frontband2_point:frontband1_point, 0])
		# coord[index, k * 3 + 1] = np.median(matrix[frontband2_point:frontband1_point, 1])
		# coord[index, k * 3 + 2] = np.median(matrix[frontband2_point:frontband1_point, 2])
		# velocity[index, k * 3    ] = np.median(matrix[frontband2_point:frontband1_point, 3])
		# velocity[index, k * 3 + 1] = np.median(matrix[frontband2_point:frontband1_point, 4])
		# velocity[index, k * 3 + 2] = np.median(matrix[frontband2_point:frontband1_point, 5])

		coord[index, k * 3    ] = np.average(matrix[frontband2_point:frontband1_point, 0])
		coord[index, k * 3 + 1] = np.average(matrix[frontband2_point:frontband1_point, 1])
		coord[index, k * 3 + 2] = np.average(matrix[frontband2_point:frontband1_point, 2])
		velocity[index, k * 3    ] = np.average(matrix[frontband2_point:frontband1_point, 3])
		velocity[index, k * 3 + 1] = np.average(matrix[frontband2_point:frontband1_point, 4])
		velocity[index, k * 3 + 2] = np.average(matrix[frontband2_point:frontband1_point, 5])

		# Prompt to make sure it's OK
		print(input_filename + " has been read at " + str(datetime.datetime.now()))
	
		# Update time
		time[index] = index * dt;
	
		# Update index for next time step
		index += 1

# Write output
output_filename1 = 'postprocessing.txt'
output_filename2 = 'velocity.txt'
np.savetxt(output_filename1, coord, fmt="%.6f")
np.savetxt(output_filename2, velocity, fmt="%.6f")