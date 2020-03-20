# Import libraries
import datetime
import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import os

# Specify directories
working_directory = ['bin/ptc_analysis2/']
# Input Files
input_filename_prefix = 'particles00'
input_filename_suffix = '.h5'

# Add input
ntime = 27
start_t = 1500;
# point_id = [0, 1, 2, 3, 4, 5, 9, 12, 1280, 1283];
point_id = [0, 1, 2, 9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38, 45, 46, 47, 54, 55, 56, 63, 64, 65, 72, 73, 74, 81, 82, 83, 90, 91, 92, 99, 100, 101, 108, 109, 110, 117, 118, 119, 126, 127, 128, 135, 136, 137, 144, 145, 146, 153, 154, 155, 162, 163, 164, 171, 172, 173, 180, 181, 182, 189, 190, 191, 198, 199, 200, 207, 208, 209, 216, 217, 218, 225, 226, 227, 234, 235, 236, 243, 244, 245, 252, 253, 254, 261, 262, 263, 270, 271, 272, 279, 280, 281, 288, 289, 290, 297, 298, 299, 306, 307, 308, 315, 316, 317, 1279, 1280, 45351, 45352];

# Preallocate variables
q_theta = np.zeros((len(point_id), 2))

for k in range(0, len(working_directory), 1):

	# Loop all the .h5 files
	for index in range(start_t, start_t + 1, 1):
	
		multiplication = 1
		index_mult = index * multiplication;

		# Prefix number of input file
		# if index_mult < 10:
		# 	zeros = '0000'
		# elif index_mult < 100:
		# 	zeros = '000'
		# elif index_mult < 1000:
		# 	zeros = '00'
		# elif index_mult < 10000:
		# 	zeros = '0'
		# else:
		# 	zeros = ''
		zeros = ''

		# Concatenate filename
		input_filename = working_directory[k] + input_filename_prefix + zeros + str(index_mult) + input_filename_suffix
	
		# Read HDF5 - df refers to DataFrame
		df = pd.read_hdf(input_filename)
	
		# Make np.array
		coord_x = np.array(df['coord_x'])
		coord_y = np.array(df['coord_y'])
		coord_z = np.array(df['coord_z'])
		stress_xx = np.array(df['stress_xx'])
		stress_yy = np.array(df['stress_yy'])
		stress_zz = np.array(df['stress_zz'])
		tau_xy = np.array(df['tau_xy'])
		tau_yz = np.array(df['tau_yz'])
		tau_xz = np.array(df['tau_xz'])
		#strain_xx = np.array(df['strain_xx'])
		#strain_yy = np.array(df['strain_yy'])
		#strain_zz = np.array(df['strain_zz'])
	
		# Make data to store
		for j in range(0, len(point_id), 1):
			theta = np.arctan2(coord_y[point_id[j]], coord_x[point_id[j]])
			q_theta[j, 0] = theta 
			j2            = 1/6 * (np.power(stress_xx[point_id[j]] - stress_yy[point_id[j]], 2) + np.power(stress_yy[point_id[j]] - stress_zz[point_id[j]], 2) + np.power(stress_xx[point_id[j]] - stress_zz[point_id[j]], 2)) + np.power(tau_xy[point_id[j]], 2) + np.power(tau_yz[point_id[j]], 2) + np.power(tau_xz[point_id[j]], 2)
			q_theta[j, 1] = np.sqrt(3 * j2)

		# Prompt to make sure it's OK
		print(input_filename + " has been read at " + str(datetime.datetime.now()))
	
		# Update index for next time step
		index += 1

# Write output
output_filename1 = 'q_theta_study.txt'
np.savetxt(output_filename1, q_theta, fmt="%.6f")

# Make yield surface
pi = 3000000
pc = 12000000
pd = 12000000
M = 1.06989
N = 0.3
p = np.linspace(11500000, 13500000, num = 100)
q = M / N * (p + pc) * (1 + (N - 1) * np.power((p + pc) / (pi + pc + pd), (N / (1 - N)))) 

# Plot
# line1  = plt.plot(pq[:, [2]], pq[:, [3]], 'k-', label='Point 1')
# line2  = plt.plot(pq[:, [0]], pq[:, [1]], 'r--', label='Point 0')
# line3  = plt.plot(pq[:, [4]], pq[:, [5]], 'r--', label='Point 2')
# line4  = plt.plot(pq[:, [6]], pq[:, [7]], 'r--', label='Point 3')
# line5  = plt.plot(pq[:, [8]], pq[:, [9]], 'r--', label='Point 4')
# line6  = plt.plot(pq[:, [10]], pq[:, [11]], 'r--', label='Point 5')
# line7  = plt.plot(pq[:, [12]], pq[:, [13]], 'r--', label='Point 9')
# line8  = plt.plot(pq[:, [14]], pq[:, [15]], 'r--', label='Point 12')
# line9  = plt.plot(pq[:, [16]], pq[:, [17]], 'r--', label='Point 1280')
# line10 = plt.plot(pq[:, [18]], pq[:, [19]], 'r--', label='Point 1283')

line1  = plt.plot(q_theta[:, 0], q_theta[:, 1], 'k*', label='Point 1')

# plt.axis([0, 0.80, 0, 4])
plt.xlabel('theta')
plt.ylabel('q (Pa)')
# plt.legend(handles=[line1, line2, line3, line4, line5, line6, line7, line8, line9, line10])
# plt.axis('equal')
plt.show()

