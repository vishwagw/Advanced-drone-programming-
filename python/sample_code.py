# this is a sample python script for using mavlink protocol to control the drone.

#we need the libraries first. pymavlink is the key to enable mavlink protocol in the python programming.
from pymavlink import mavutil

#Now we have to establish a connection with the drone.
vehicle = mavutil.mavlink_connection('udp:127.0.0.14550')

#after connecting the drone with software, we now can create our command fucntions to control drone movements.

#first we can send a take off command to the drone to start and take off from the ground. 
vehicle.mav.command_long_send(
0, 1, # System ID and Component ID
mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, # Command ID
0, 0, 0, 0, 0, 0, 0, 0 # Parameters
)

# Send a command to fly to a specific location
vehicle.mav.command_long_send(
0, 1, # System ID and Component ID
mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, # Command ID
0, 0, 0, 0, 0, 0, # Parameters
latitude, longitude, altitude # Target location
)

# Send a command to land the drone
vehicle.mav.command_long_send(
0, 1, # System ID and Component ID
mavutil.mavlink.MAV_CMD_NAV_LAND, # Command ID
0, 0, 0, 0, 0, 0, 0, 0 # Parameters
)
# Close the connection
vehicle.close()
