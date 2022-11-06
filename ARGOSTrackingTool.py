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

# Ask the user for a date, specifying the format
user_date = input("Enter a date (M/D/YYYY):")

# Create a variable pointing to the data file
file_name = 'data/raw/Sara.txt'

# Create file object from file name
file_object = open(file=file_name, mode = 'r')

# read contents of file into a list
line_list = file_object.readlines()

# Close file
file_object.close()

# Create empty dictionaries
date_dict = {}
location_dict = {}

# Extract one line of line_list into a variable
for lineString in line_list:
    
    # Check if the lineString is a data line
    if lineString[0] in ('#','u'):
        continue
    
    # Use the split command to parse the items in lineString into a list object
    # default is space, so no need to add symbol
    lineData = lineString.split()
    
    # Assign variables to specfic items in the list
    record_id = lineData[0]   # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    obs_lc = lineData[4]       # Observation Location Class
    obs_lat = lineData[6]     # Observation Latitude
    obs_lon = lineData[7]     # Observation Longitude
    
    # filter for classes 1, 2, and 3
    if obs_lc in ("1", "2", "3"):
        
        # add items to dictionaries
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat, obs_lon)
    
    # Print information to the user
    #print (f'Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}.')

# Create list to store keys
matching_keys = []

# Loop through all key, value pairs in the date_dictionary
for the_key, the_value in date_dict.items():
    #See if the date (the value) matches the user date
    if the_value == user_date:
        # Add matching keys to list
        matching_keys.append(the_key)

# Reveal locations for each key in matching_keys
for matching_key in matching_keys:
    obs_lat, obs_lon = location_dict[matching_key]
    print(f"Record {matching_key} indicates Sarah was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}.")