# Import libraries
import datetime
import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import os

# Specify directories
working_directory = ['bin/ptc_analysis/']
# Input Files
input_filename_prefix = 'particles0'
input_filename_suffix = '0.h5'

# Add input
ntime = 27
# point_id = [0, 1, 2, 3, 4, 5, 9, 12, 1280, 1283];
point_id = [0, 1, 2, 9, 1280];

# Preallocate variables
pq = np.zeros((ntime, 2 * len(point_id)))

for k in range(0, len(working_directory), 1):

	# Loop all the .h5 files
	for index in range(1500, 1500 + ntime, 1):
	
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
		#coord_x = np.array(df['coord_x'])
		#coord_y = np.array(df['coord_y'])
		#coord_z = np.array(df['coord_z'])
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
			pq[index - 1500, j * 2]     = -1/3 * (stress_xx[point_id[j]] + stress_yy[point_id[j]] +stress_zz[point_id[j]]) 
			j2 = 1/6 * (np.power(stress_xx[point_id[j]] - stress_yy[point_id[j]], 2) + np.power(stress_yy[point_id[j]] - stress_zz[point_id[j]], 2) + np.power(stress_xx[point_id[j]] - stress_zz[point_id[j]], 2)) + np.power(tau_xy[point_id[j]], 2) + np.power(tau_yz[point_id[j]], 2) + np.power(tau_xz[point_id[j]], 2)
			pq[index - 1500, j * 2 + 1] = np.sqrt(3 * j2)

		# Prompt to make sure it's OK
		print(input_filename + " has been read at " + str(datetime.datetime.now()))
	
		# Update index for next time step
		index += 1

# Write output
output_filename1 = 'pq_study.txt'
np.savetxt(output_filename1, pq, fmt="%.6f")

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

line1  = plt.plot(pq[:, [2]], pq[:, [3]], 'k-', label='Point 1')
line2  = plt.plot(pq[:, [0]], pq[:, [1]], 'r--', label='Point 0')
line3  = plt.plot(pq[:, [4]], pq[:, [5]], 'r--', label='Point 2')
line4  = plt.plot(pq[:, [6]], pq[:, [7]], 'r--', label='Point 9')
line5  = plt.plot(pq[:, [8]], pq[:, [9]], 'r--', label='Point 1280')
line6  = plt.plot(p, q, 'g', label='Initial Yield')

# plt.axis([0, 0.80, 0, 4])
plt.xlabel('p (Pa)')
plt.ylabel('q (Pa)')
# plt.legend(handles=[line1, line2, line3, line4, line5, line6, line7, line8, line9, line10])
plt.axis('equal')
plt.show()

