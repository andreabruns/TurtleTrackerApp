#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Andrea Bruns (andrea.bruns@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

# Create a variable pointing to the data file
file_name = 'data/raw/Sara.txt'

# Create file object from file name
file_object = open(file=file_name, mode = 'r')

# read contents of file into a list
lineString = file_object.readline()

# Extract one line of line_list into a variable
while lineString != "":
    
    # Check if the lineString is a data line
    if lineString[0] in ('#','u'):
        lineString = file_object.readline()
        continue
    
    # Use the split command to parse the items in lineString into a list object
    # default is space, so no need to add symbol
    lineData = lineString.split()
    
    # Assign variables to specfic items in the list
    record_id = lineData[0]   # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    ob_lc = lineData[4]       # Observation Location Class
    obs_lat = lineData[6]     # Observation Latitude
    obs_lon = lineData[7]     # Observation Longitude
    
    # Print information to the user
    print (f'Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}.')
    
    # move to the next line in the file
    lineString = file_object.readline()

# close the file object
file_object.close()