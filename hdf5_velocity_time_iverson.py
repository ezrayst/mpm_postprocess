# Import libraries
import datetime
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Specify directories
working_directory = ['bin/final-long/']
# Input Files
input_filename_prefix = 'particles'
input_filename_suffix = '000.h5'

# Add input
ntime = 100
dt = 0.05
point_id = [20, 316, 2784, 4325, 5024, 4958];

# Preallocate variables
time = np.zeros((ntime + 1, 1))
velocity = np.zeros((ntime + 1, len(point_id) * 2))

# Loop all the .h5 files
for index in range(0, ntime + 1, 1):

	# Index multiplication
	multiplication = 20
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
	input_filename = working_directory[0] + input_filename_prefix + zeros + str(index_mult) + input_filename_suffix
	
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
	#strain_xx = np.array(df['strain_xx'])
	#strain_yy = np.array(df['strain_yy'])
	#strain_zz = np.array(df['strain_zz'])
	velocity_x = np.array(df['velocity_x'])
	velocity_y = np.array(df['velocity_y'])

	# Make data to store
	for k in range(0, len(point_id), 1):
		#velocity[index, k] = np.sqrt(np.square(velocity_y[point_id[0]]) + np.square(velocity_x[point_id[0]]))	
		velocity[index, k * 2] = velocity_x[point_id[k]]
		velocity[index, k * 2 + 1] = velocity_y[point_id[k]]

	# Prompt to make sure it's OK
	print(input_filename + " has been read at " + str(datetime.datetime.now()))
	
	# Update time
	time[index] = index * dt;
	
	# Update index for next time step
	index += 1

np.savetxt('results_mpm.txt', velocity, delimiter=',')

# Plot
# line1, = plt.plot(time_analytical, velocity_analytical[:, [0]], 'k', label='Analytical Friction Coefficient = 0.0')
# line2, = plt.plot(time, velocity[:, [0]], 'r--', label='MPM Friction Coefficient = 0.0')
# line3, = plt.plot(time_analytical, velocity_analytical[:, [1]], 'm', label='Analytical Friction Coefficient = 0.2')
# line4, = plt.plot(time, velocity[:, [2]], 'b-.', label='MPM Friction Coefficient = 0.2')
# line5, = plt.plot(time_analytical, velocity_analytical[:, [2]], 'c', label='Analytical Friction Coefficient = 0.4')
# line6, = plt.plot(time, velocity[:, [4]], 'g:', label='MPM Friction Coefficient = 0.4')
# line7, = plt.plot(time_analytical, velocity_analytical[:, [3]], 'k', label='Analytical Friction Coefficient = 0.6')
# line8, = plt.plot(time, velocity[:, [6]], 'y--', label='MPM Friction Coefficient = 0.6')
# plt.axis([0, 0.80, 0, 4])
# plt.xlabel('Time (s)')
# plt.ylabel('Resultant Velocity (m/s)')
# plt.legend(handles=[line1, line2, line3, line4, line5, line6, line7, line8])
# plt.show()


