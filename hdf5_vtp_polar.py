# Import libraries
import datetime
import matplotlib as mp
import numpy as np
import pandas as pd
#import pyevtk
import os


# Import external libraries
from evtk.hl import pointsToVTK 

# Specify directories
working_directory = 'bin/ptc_full/'

# Input Files
input_filename_prefix = 'particles'
input_filename_suffix = '000.h5'

# Output files
output_directory = working_directory + 'vtp/'
output_prefix_filename = 'polar'
output_suffix_filename = '.vtp'
if not os.path.exists(output_directory):
	os.makedirs(output_directory)
print("directory of files: " + output_directory)

# Loop all the .h5 files
ntime = 4
index = 40
#for index in range(0, ntime, 1):
	
# Prefix number of input file
# if index < 10:
# 	zeros = '00'
# elif index < 100:
# 	zeros = '0'
# else:
# 	zeros = ''
zeros = '';

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
tau_xy = np.array(df['tau_xy'])
tau_yz = np.array(df['tau_yz'])
tau_xz = np.array(df['tau_xz'])

# Make data to store
data   = np.empty([len(coord_x), 3])
radial = np.random.rand(len(coord_x))
hoop   = np.random.rand(len(coord_x))
shear  = np.random.rand(len(coord_x))

for iterate in range(1, len(coord_x)):

	theta = np.arctan2(coord_y[iterate], coord_x[iterate])
	costheta = np.cos(theta)
	sintheta = np.sin(theta)
	cos2theta = np.cos(2 * theta)
	sin2theta = np.sin(2 * theta)

	# Radial stress
	data[iterate][0] = stress_xx[iterate] * np.power(costheta, 2) + stress_yy[iterate] * np.power(sintheta, 2) + tau_xy[iterate] * sin2theta
	# Hoop Stress
	data[iterate][1] = stress_xx[iterate] * np.power(sintheta, 2) + stress_yy[iterate] * np.power(costheta, 2) - tau_xy[iterate] * sin2theta
	# Shear Stress
	data[iterate][2] = sintheta * costheta * (stress_yy[iterate] - stress_xx[iterate]) + tau_xy[iterate] * cos2theta

	radial[iterate] = data[iterate][0]
	hoop[iterate]   = data[iterate][1]
	shear[iterate]  = data[iterate][2]

	# Update iterate
	iterate += 1

print(data.shape)

# radial = data[..., 0]
# hoop   = data[..., 1]
# shear  = data[..., 2]

print(radial.shape)

# Write VTP file
pointsToVTK(output_filename, coord_x, coord_y, coord_z, data = {"radial" : radial, "hoop" : hoop, "shear" : shear})

# Print prompts
print(output_prefix_filename + str(index) + output_suffix_filename + " has been processed at " + str(datetime.datetime.now()))

# Update index for next time step
#index += 1



