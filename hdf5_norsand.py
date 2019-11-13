# Import libraries
import datetime
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Specify directories
working_directory = ['../results/norsand_contractive_bonded/']
# Input Files
input_filename_prefix = 'particles'
input_filename_suffix = '0000.h5'

# Add input
ntime = 1000
point_id = [0];

# Preallocate variables
time = np.zeros((ntime + 1, 1))
stress = np.zeros((ntime + 1, 3 * len(point_id)))
strain = np.zeros((ntime + 1, 3 * len(point_id)))
pq = np.zeros((ntime + 1, 2 * len(point_id)))
state_parameters = np.zeros((ntime + 1, 7 * len(point_id)))

for k in range(0, len(working_directory), 1):

	# Loop all the .h5 files
	for index in range(0, ntime + 1, 1):
	
		multiplication = 1
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
		#coord_x = np.array(df['coord_x'])
		#coord_y = np.array(df['coord_y'])
		#coord_z = np.array(df['coord_z'])
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
		p_image = np.array(df['p_image'])
		e_image = np.array(df['e_image'])
		void_ratio = np.array(df['void_ratio'])
		lode_angle = np.array(df['lode_angle'])
		M_theta = np.array(df['M_theta'])
		p_cohesion = np.array(df['p_cohesion'])
		p_dilation = np.array(df['p_dilation'])
	
		# Make data to store
		for j in range(0, len(point_id), 1):
			stress[index, j * 3]     = stress_xx[point_id[j]]
			stress[index, j * 3 + 1] = stress_yy[point_id[j]]
			stress[index, j * 3 + 2] = stress_zz[point_id[j]]

			pq[index, j * 2]     = (stress_xx[point_id[j]] + stress_yy[point_id[j]] + stress_zz[point_id[j]]) / 3
			pq[index, j * 2 + 1] = np.sqrt(0.5 * (np.square(stress_xx[point_id[j]] - stress_yy[point_id[j]]) + np.square(stress_yy[point_id[j]] - stress_zz[point_id[j]]) + np.square(stress_xx[point_id[j]] - stress_zz[point_id[j]])) + 6 * (np.square(tau_xy[point_id[j]]) + np.square(tau_yz[point_id[j]]) + np.square(tau_xz[point_id[j]])))

			state_parameters[index, j * 3]     = p_image[point_id[j]]
			state_parameters[index, j * 3 + 1] = e_image[point_id[j]]
			state_parameters[index, j * 3 + 2] = void_ratio[point_id[j]]
			state_parameters[index, j * 3 + 3] = lode_angle[point_id[j]]
			state_parameters[index, j * 3 + 4] = M_theta[point_id[j]]
			state_parameters[index, j * 3 + 5] = p_cohesion[point_id[j]]
			state_parameters[index, j * 3 + 6] = p_dilation[point_id[j]]

			strain[index, j * 3]     = strain_xx[point_id[j]]
			strain[index, j * 3 + 1] = strain_yy[point_id[j]]
			strain[index, j * 3 + 2] = strain_zz[point_id[j]]

		# Prompt to make sure it's OK
		print(input_filename + " has been read at " + str(datetime.datetime.now()))
	
		# Update index for next time step
		index += 1

# Write output
output_filename1 = 'stress_study.txt'
np.savetxt(output_filename1, stress, fmt="%.6f")

output_filename2 = 'strain_study.txt'
np.savetxt(output_filename2, strain, fmt="%.6f")

output_filename3 = 'pq_study.txt'
np.savetxt(output_filename3, pq, fmt="%.6f")

output_filename4 = 'state_parameter.txt'
np.savetxt(output_filename4, state_parameters, fmt="%.6f")