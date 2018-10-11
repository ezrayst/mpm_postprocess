# Import libraries
import datetime
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Specify directories
working_directory = 'bin/gravity_nopoisson/'

# Input Files
input_filename_prefix = 'particles'
input_filename_suffix = '00.h5'

# Output files
output_directory = working_directory + 'results/'
output_prefix_filename = 'strain'
output_suffix_filename = '.vtp'
if not os.path.exists(output_directory):
	os.makedirs(output_directory)
print("directory of files: " + output_directory)

# Add input
ntime = 99
dt = 0.01
point_id = [2, 3];

# Preallocate variables
time = np.zeros((ntime + 1, 1))
stress = np.zeros((ntime + 1, len(point_id)))

# Loop all the .h5 files
for index in range(0, ntime + 1, 1):

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
	#coord_x = np.array(df['coord_x'])
	#coord_y = np.array(df['coord_y'])
	#coord_z = np.array(df['coord_z'])
	#stress_xx = np.array(df['stress_xx'])
	stress_yy = np.array(df['stress_yy'])
	#stress_zz = np.array(df['stress_zz'])
	#tau_xy = np.array(df['tau_xy'])
	#strain_xx = np.array(df['strain_xx'])
	#strain_yy = np.array(df['strain_yy'])
	#strain_zz = np.array(df['strain_zz'])

	# Make data to store
	for j in range(0, len(point_id), 1):
		stress[index, j] = stress_yy[point_id[j]]	

	# Prompt to make sure it's OK
	print(input_filename + " has been read at " + str(datetime.datetime.now()))

	# Update time
	time[index] = index * dt;

	# Update index for next time step
	index += 1

# Plot
plt.plot(time, stress, 'b')
plt.axis([0, 1, -30000, 0])
plt.xlabel('Time (s)')
plt.ylabel('Stress (Pa)')
plt.show()


