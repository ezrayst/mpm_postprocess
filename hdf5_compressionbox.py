# Import libraries
import datetime
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Specify directories
working_directory = ['compressionbox_00_5/', 'compressionbox_00_6/', 'compressionbox_00_7/',
					 'compressionbox_30_5/', 'compressionbox_30_6/', 'compressionbox_30_7/',
					 'compressionbox_45_5/', 'compressionbox_45_6/', 'compressionbox_45_7/']


# Input Files
input_filename_prefix = 'particles'
input_filename_suffix = '000.h5'

# Add input
ntime = 1

# Preallocate variables
stress = np.zeros((len(working_directory), 3 * 3))

for k in range(0, len(working_directory), 1):

	# Loop all the .h5 files
	for index in range(1, ntime + 1, 1):
	
		if (np.remainder((k + 1), 3) == 1):
			multiplication = 100
		elif (np.remainder((k + 1), 3) == 2):
			multiplication = 1000
		elif (np.remainder((k + 1), 3) == 0):
			multiplication = 10000

		index_mult = index * multiplication;

		# Prefix number of input file
		zeros = ''

		# Concatenate filename
		input_filename = working_directory[k] + input_filename_prefix + zeros + str(index_mult) + input_filename_suffix
	
		# Read HDF5 - df refers to DataFrame
		df = pd.read_hdf(input_filename)
	
		# Make np.array
		#coord_x = np.array(df['coord_x'])
		#coord_y = np.array(df['coord_y'])
		#coord_z = np.array(df['coord_z'])
		stress_xx = np.array(df['stress_xx'])
		stress_yy = np.array(df['stress_yy'])
		#stress_zz = np.array(df['stress_zz'])
		tau_xy = np.array(df['tau_xy'])
		#tau_yz = np.array(df['tau_yz'])
		#tau_xz = np.array(df['tau_xz'])
		#strain_xx = np.array(df['strain_xx'])
		#strain_yy = np.array(df['strain_yy'])
		#strain_zz = np.array(df['strain_zz'])
		#gamma_xy = np.array(df['gamma_xy'])
		#gamma_yz = np.array(df['gamma_yz'])
		#gamma_xz = np.array(df['gamma_xz'])
	
		# Make data to store in MPa
		stress[index, 0] = np.mean(stress_xx) / 1000000
		stress[index, 1] = np.mean(stress_yy) / 1000000
		stress[index, 2] = np.mean(tau_xy) / 1000000
		stress[index, 3] = np.min(stress_xx) / 1000000
		stress[index, 4] = np.min(stress_yy) / 1000000
		stress[index, 5] = np.min(tau_xy) / 1000000
		stress[index, 6] = np.max(stress_xx) / 1000000
		stress[index, 7] = np.max(stress_yy) / 1000000
		stress[index, 8] = np.max(tau_xy) / 1000000

		# Prompt to make sure it's OK
		print(input_filename + " has been read at " + str(datetime.datetime.now()))
	
	
		# Update index for next time step
		index += 1

# Write output
output_filename1 = 'stress_compressionbox.txt'
np.savetxt(output_filename1, stress, fmt="%.16f")