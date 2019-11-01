# Import libraries
import datetime
import matplotlib as mp
import numpy as np
import pandas as pd
import os
import pyevtk as evtk

# Import external libraries
# Source: https://github.com/paulo-herrera/PyEVTK
# from evtk.hl import pointsToVTK 

# Specify directories
working_directory = ['../results/compressionbox_00_5/',
					 '../results/compressionbox_30_5/',
					 '../results/compressionbox_45_5/']

# Input Files
input_filename_prefix = 'particles'
input_filename_suffix = '00000.h5'

# Output files
output_directory = 'data/'
output_prefix_filename1 = 'stress'
output_prefix_filename2 = 'displacement'
output_suffix_filename = '.txt'
if not os.path.exists(output_directory):
	os.makedirs(output_directory)
print("directory of files: " + output_directory)

# Loop all the .h5 files
ntime = 1

for k in range(0, len(working_directory), 1):

	for index in range(1, ntime + 1, 1):
		# Prefix number of input file
		# if index < 10:
		# 	zeros = '00'
		# elif index < 100:
		# 	zeros = '0'
		# else:
		# 	zeros = ''
		zeros = ''

		# Concatenate filename
		input_filename = working_directory[k] + input_filename_prefix + zeros + str(index) + input_filename_suffix
	
		# Read HDF5 - df refers to DataFrame
		df = pd.read_hdf(input_filename)
	
		# Make np.array
		coord_x = np.array(df['coord_x'])
		coord_y = np.array(df['coord_y'])
		coord_z = np.array(df['coord_z'])
		displacement_x = np.array(df['displacement_x'])
		displacement_y = np.array(df['displacement_y'])
		displacement_z = np.array(df['displacement_z'])
		stress_xx = np.array(df['stress_xx'])
		stress_yy = np.array(df['stress_yy'])
		stress_zz = np.array(df['stress_zz'])
		tau_xy = np.array(df['tau_xy'])
		tau_yz = np.array(df['tau_yz'])
		tau_xz = np.array(df['tau_xz'])
		strain_xx = np.array(df['strain_xx'])
		strain_yy = np.array(df['strain_yy'])
		strain_zz = np.array(df['strain_zz'])
		gamma_xy = np.array(df['gamma_xy'])
		gamma_yz = np.array(df['gamma_yz'])
		gamma_xz = np.array(df['gamma_xz'])

		# Make data to store
		stress = np.zeros((len(stress_xx), 3))
		displacement = np.zeros((len(displacement_x), 3))
		iterate = 0
		for iterate in range(0, len(stress_xx)):
			meanstress = (stress_xx[iterate] + stress_yy[iterate]) / 2
			diffstress = (stress_xx[iterate] - stress_yy[iterate]) / 2
			stress_parallel = meanstress - np.sqrt(diffstress**2 + tau_xy[iterate]**2)
			stress_perpendicular = meanstress + np.sqrt(diffstress**2 + tau_xy[iterate]**2)

			displacement_total = np.sqrt(displacement_x[iterate]**2 + displacement_y[iterate]**2)

			# Put them into the data structure
			stress[iterate][0] = stress_parallel
			stress[iterate][1] = stress_perpendicular
			stress[iterate][2] = 0

			displacement[iterate][0] = displacement_total
			displacement[iterate][1] = 0
			displacement[iterate][2] = 0

			# Update iterate
			iterate += 1
		# print(stress)
		# print(displacement)
	
		# Write VTP file
		# evtk.pointsToVTK(output_filename, stress[:, 0], stress[:, 1], stress[:, 2], data = {output_prefix_filename : stress})
		
		# Write output
		output_filename1 = output_directory + output_prefix_filename1 + str(k) + output_suffix_filename
		np.savetxt(output_filename1, stress, fmt="%.16f")
		
		output_filename2 = output_directory + output_prefix_filename2 + str(k) + output_suffix_filename
		np.savetxt(output_filename2, displacement, fmt="%.16f")

		# Print prompts
		print(output_prefix_filename1 + str(k) + output_suffix_filename + " has been processed at " + str(datetime.datetime.now()))
		print(output_prefix_filename2 + str(k) + output_suffix_filename + " has been processed at " + str(datetime.datetime.now()))
	
		# Update index for next time step
		index += 1
