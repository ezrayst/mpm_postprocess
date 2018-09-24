# Import libraries
import datetime
import matplotlib as mp
import numpy as np
import pandas as pd
import os

# Import external libraries
from evtk.hl import pointsToVTK 

# Specify directories
working_directory = 'bin/20180918_columncollapse_usf/'

# Input Files
input_filename_prefix = 'particles00'
input_filename_suffix = '00.h5'

# Output files
output_directory = working_directory + 'vtp/'
output_prefix_filename = 'stress'
output_suffix_filename = '.vtp'
if not os.path.exists(output_directory):
	os.makedirs(output_directory)
print("directory of files: " + output_directory)

# Loop all the .h5 files
ntime = 5
for index in range(0, ntime, 1):
	# Prefix number of input file
	if index < 10:
		zeros = '00'
	elif index < 100:
		zeros = '0'
	else:
		zeros = ''

	# Concatenate filename
	input_filename = working_directory + input_filename_prefix + zeros + str(index) + input_filename_suffix
	output_filename = output_directory + output_prefix_filename + str(index)

	# Read HDF5 - df refers to DataFrame
	df = pd.read_hdf(input_filename)

	# Make np.array
	coord_x = np.array(df['coord_x'])
	coord_y = np.array(df['coord_y'])
	coord_z = np.array(df['coord_z'])
	stress_xx = np.array(df['stress_xx'])
	stress_yy = np.array(df['stress_yy'])
	stress_zz = np.array(df['stress_zz'])

	# Make data to store
	data = np.empty((len(coord_x), np.zeros(3)))
	iterate = 1
	for iterate in range(1, len(coord_x)):
		data[iterate][1] = stress_xx[iterate]
		data[iterate][2] = stress_yy[iterate]
		data[iterate][3] = stress_zz[iterate]
		# Update iterate
		iterate += 1
	print(data.shape)

	# Write VTP file
	pointsToVTK(output_filename, coord_x, coord_y, coord_z, data = {output_prefix_filename : data})
	
	# Print prompts
	print(output_prefix_filename + str(index) + output_suffix_filename + " has been processed at " + str(datetime.datetime.now()))

	# Update index for next time step
	index += 1



