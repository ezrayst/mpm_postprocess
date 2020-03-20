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
# point_id = [0, 1, 2, 9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38, 45, 46, 47, 54, 55, 56, 63, 64, 65, 72, 73, 74, 81, 82, 83, 90, 91, 92, 99, 100, 101, 108, 109, 110, 117, 118, 119, 126, 127, 128, 135, 136, 137, 144, 145, 146, 153, 154, 155, 162, 163, 164, 171, 172, 173, 180, 181, 182, 189, 190, 191, 198, 199, 200, 207, 208, 209, 216, 217, 218, 225, 226, 227, 234, 235, 236, 243, 244, 245, 252, 253, 254, 261, 262, 263, 270, 271, 272, 279, 280, 281, 288, 289, 290, 297, 298, 299, 306, 307, 308, 315, 316, 317, 1279, 1280, 45351, 45352];
point_id = [0, 1, 2, 9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38, 45, 46, 47, 54, 55, 56, 63, 64, 65, 72, 73, 74, 81, 82, 83, 90, 91, 92, 99, 100, 101, 108, 109, 110, 117, 118, 119, 126, 127, 128, 135, 136, 137, 144, 145, 146, 153, 154, 155, 162, 163, 164, 171, 172, 173, 180, 181, 182, 189, 190, 191, 198, 199, 200, 207, 208, 209, 216, 217, 218, 225, 226, 227, 234, 235, 236, 243, 244, 245, 252, 253, 254, 261, 262, 263, 270, 271, 272, 279, 280, 281, 288, 289, 290, 297, 298, 299, 306, 307, 308, 315, 316, 317, 324, 325, 326, 333, 334, 335, 342, 343, 344, 351, 352, 353, 360, 361, 362, 369, 370, 371, 378, 379, 380, 387, 388, 389, 396, 397, 398, 405, 406, 407, 414, 415, 416, 423, 424, 425, 432, 433, 434, 441, 442, 443, 450, 451, 452, 459, 460, 461, 468, 469, 470, 477, 478, 479, 486, 487, 488, 495, 496, 497, 504, 505, 506, 513, 514, 515, 522, 523, 524, 531, 532, 533, 540, 541, 542, 549, 550, 551, 558, 559, 560, 567, 568, 569, 576, 577, 578, 585, 586, 587, 594, 595, 596, 603, 604, 605, 612, 613, 614, 621, 622, 623, 630, 631, 632, 639, 640, 641, 648, 649, 650, 657, 658, 659, 666, 667, 668, 675, 676, 677, 684, 685, 686, 693, 694, 695, 702, 703, 704, 711, 712, 713, 720, 721, 722, 729, 730, 731, 738, 739, 740, 747, 748, 749, 756, 757, 758, 765, 766, 767, 774, 775, 776, 783, 784, 785, 792, 793, 794, 801, 802, 803, 810, 811, 812, 819, 820, 821, 828, 829, 830, 837, 838, 839, 846, 847, 848, 855, 856, 857, 864, 865, 866, 873, 874, 875, 882, 883, 884, 891, 892, 893, 900, 901, 902, 909, 910, 911, 918, 919, 920, 927, 928, 929, 936, 937, 938, 945, 946, 947, 954, 955, 956, 963, 964, 965, 972, 973, 974, 981, 982, 983, 990, 991, 992, 999, 1000, 1001, 1008, 1009, 1010, 1017, 1018, 1019, 1026, 1027, 1028, 1035, 1036, 1037, 1044, 1045, 1046, 1053, 1054, 1055, 1062, 1063, 1064, 1071, 1072, 1073, 1080, 1081, 1082, 1089, 1090, 1091, 1098, 1099, 1100, 1107, 1108, 1109, 1116, 1117, 1118, 1125, 1126, 1127, 1134, 1135, 1136, 1143, 1144, 1145, 1152, 1153, 1154, 1161, 1162, 1163, 1170, 1171, 1172, 1179, 1180, 1181, 1188, 1189, 1190, 1197, 1198, 1199, 1206, 1207, 1208, 1215, 1216, 1217, 1224, 1225, 1226, 1233, 1234, 1235, 1242, 1243, 1244, 1251, 1252, 1253, 1260, 1261, 1262, 1269, 1270, 1271, 1278, 1279, 1280, 45351, 45352, 45353];

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

