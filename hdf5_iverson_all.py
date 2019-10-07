# Import libraries
import datetime
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Specify directories
working_directory = ['../results/iverson_2d_2500_4_dt17/',
                     '../results/iverson_2d_2500_4_dt27/',
                     '../results/iverson_2d_2500_4_dt57/',
                     '../results/iverson_2d_2500_4/',
					 '../results/iverson_2d_2500_4_dt26/',
                     '../results/iverson_2d_2500_4_dt56/']

# working_directory = ['iverson_2d_2500_4_dt17/']

# Input Files
input_filename_prefix = 'particles'
input_filename_suffix = '000.h5'
# input_filename_suffix = '.h5'

# Add input
# Total time is 2000
ntime = 200
dt = 0.001

# Preallocate variables
time = np.zeros((ntime + 1, 1))
coord = np.zeros((ntime + 1, 2 * len(working_directory)))
center_mass = np.zeros((ntime + 1, 2 * len(working_directory)))
velocity = np.zeros((ntime + 1, 2 * len(working_directory)))

for k in range(0, len(working_directory), 1):
	
	# Make multiplication
	if k == 0:
		multiplication = 100
	elif k == 1:
		multiplication = 50
	elif k == 2:
		multiplication = 20
	elif k == 3:
		multiplication = 10
	elif k == 4:
		multiplication = 5
	elif k == 5:
		multiplication = 2

	# Loop all the .h5 files
	for index in range(0, ntime + 1, 1):

		# Index multiplication
		index_mult = index * multiplication;

		# if index == 0:
		# 	if k == 0 or k == 1:
		# 		input_filename_suffix = '000.h5'
		# 	elif k == 2 or k == 3 or k == 4:
		# 		input_filename_suffix = '00.h5'
		# 	elif k == 5:
		# 		input_filename_suffix = '0.h5'				
		# else:
		# 	input_filename_suffix = '000.h5'

		# Prefix number of input file
		if k == 0 or k == 1:
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
		elif k == 2 or k == 3 or k == 4:
			if index_mult < 10:
				zeros = '000'
			elif index_mult < 100:
				zeros = '00'
			elif index_mult < 1000:
				zeros = '0'
			else: 
			    zeros = ''
		else:
			if index_mult < 10:
				zeros = '00'
			elif index_mult < 100:
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
		#coord_z = np.array(df['coord_z'])
		velocity_x = np.array(df['velocity_x'])
		velocity_y = np.array(df['velocity_y'])
		#velocity_z = np.array(df['velocity_z'])		
		#stress_xx = np.array(df['stress_xx'])
		#stress_yy = np.array(df['stress_yy'])
		#stress_zz = np.array(df['stress_zz'])
		#tau_xy = np.array(df['tau_xy'])
		#strain_xx = np.array(df['strain_xx'])
		#strain_yy = np.array(df['strain_yy'])
		#strain_zz = np.array(df['strain_zz'])
	
		# Get center of mass
		center_mass[index, k * 2] = np.mean(coord_x)
		center_mass[index, k * 2 + 1] = np.mean(coord_y)

		# Get average velocity
		velocity[index, k * 2] = np.mean(velocity_x)
		velocity[index, k * 2 + 1] = np.mean(velocity_y)

		# Get 1-99% for front and tail
		coord_x.sort()
		length_points = len(coord_x)
		front_point = round(0.99 * length_points)
		tail_point = round(0.01 * length_points)

		# Make data to store
		coord[index, k * 2]     = coord_x[front_point]
		coord[index, k * 2 + 1] = coord_x[tail_point]
	
		# Prompt to make sure it's OK
		print(input_filename + " has been read at " + str(datetime.datetime.now()))
	
		# Update time
		time[index] = index * dt;
	
		# Update index for next time step
		index += 1

# Write output
output_filename1 = 'postprocessing.txt'
output_filename2 = 'centermass.txt'
output_filename3 = 'velocity.txt'
np.savetxt(output_filename1, coord, fmt="%.6f")
np.savetxt(output_filename2, center_mass, fmt="%.6f")
np.savetxt(output_filename3, velocity, fmt="%.6f")