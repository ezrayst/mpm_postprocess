# Import libraries
from evtk.hl import unstructuredGridToVTK 
from evtk.hl import pointsToVTK 
import matplotlib as mp
import numpy as np
import pandas as pd
import os

# Specify directories
working_directory = 'bin/20180918_columncollapse_usf/'

# Input Files
input_filename_prefix = 'particles00'
input_filename_suffix = '00.h5'

# Output files
output_directory = working_directory + 'vtk/'
output_prefix_filename = 'stress'
output_suffix_filename = '.vtk'
if not os.path.exists(output_directory):
	os.makedirs(output_directory)

# Loop all the .h5 files
ntime = 5
for index in range(0, ntime, 1):
	# Concatenate filename
	input_filename = working_directory + input_filename_prefix + str(index) + input_filename_suffix
	output_filename = output_directory + output_prefix_filename + str(index)

	# Read HDF5 - df refers to DataFrame
	df = pd.read_hdf(input_filename)

	# Make np.array
	coord_x = np.array(df['coord_x'])
	coord_y = np.array(df['coord_y'])
	coord_z = np.array(df['coord_z'])
	stress_xx = np.array(df['stress_xx'])
	stress_yy = np.array(df['stress_yy'])
	conn = np.zeros(len(coord_x))
	celltype = np.zeros(len(coord_x))
	offset = np.zeros(len(coord_x))

	# Write VTK file
	unstructuredGridToVTK(output_filename, coord_x, coord_y, coord_z, connectivity = conn, offsets = offset, cell_types = celltype, cellData = {"stress_xx" : stress_xx }, pointData = {"stress_yy" : stress_yy})
	
	# Update index for next time step
	index += 1



