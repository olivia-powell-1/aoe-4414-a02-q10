# sez_to_ecef.py
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
#  Converts SEZ to ECEF frame
# Parameters:
#   o_lat_deg: original latitude in degrees in SEZ coordinate frame
#   o_lon_deg: original longetude in degrees in SEZ coordinate frame
#   o_hae_km: original height above the elipsoid in km in SEZ coordinate frame
#   s_km: s component in km
#   e_km: e component in km
#   z_km: z component in km 
# Output:
#   ecef_x_km: x component in km in ECEF coordinate frame
#   ecef_y_km: y component in km in ECEF coordinate frame
#   ecef_z_km: z component in km in ECEF coordinate frame
#
# Written by Olivia Powell
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math as m # math ops
import numpy as np # matrix function

# "constants"
r_e_km = 6378.137 # redius of earth
e_e = 0.081819221456 # eccentricity of earth

# helper functions

## function description
def calc_denom(ecc,lat_rad):
    return m.sqrt(1-ecc**2 *(m.sin(lat_rad))**2)

# initialize script arguments
o_lat_deg = float('nan')  
o_lon_deg = float('nan')  
o_hae_km = float('nan')  
s_km = float('nan')
e_km = float('nan')
z_km = float('nan')

# parse script arguments
if len(sys.argv)==7: #if the # of things in the command line is 4
    o_lat_deg = float(sys.argv[1])  
    o_lon_deg = float(sys.argv[2])  
    o_hae_km = float(sys.argv[3])  
    s_km = float(sys.argv[4])
    e_km = float(sys.argv[5])
    z_km = float(sys.argv[6])
    ...
else:
    print(\
    'Usage: '\
    'python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km'\
    )
    exit()

# write script below this line

# convert longitude and latitude to radians
o_lat_rad = o_lat_deg*m.pi/180.0
o_lon_rad = o_lon_deg*m.pi/180.0

# use rotation matricies to shift from sez to ecef
denom = calc_denom(e_e, o_lat_rad)
c_e = r_e_km/denom
s_e = r_e_km*(1-e_e**2)/denom
r_x_km = (c_e+o_hae_km)*m.cos(o_lat_rad)*m.cos(o_lon_rad)
r_y_km = (c_e+o_hae_km)*m.cos(o_lat_rad)*m.sin(o_lon_rad)
r_z_km = (s_e+o_hae_km)*m.sin(o_lat_rad)
r = np.array([r_x_km, r_y_km, r_z_km]) # define r as row vector
r = r.reshape(-1, 1) # transpose r to column vector
r_sez = np.array([s_km, e_km, z_km]) # define r in sez coordinates as a row vector
r_sez = r_sez.reshape(-1, 1) # transpose r_sez to column vector

# define y axis rotation matrix
ry = np.array([[m.sin(o_lat_rad), 0, m.cos(o_lat_rad)], [0, 1, 0], [-m.cos(o_lat_rad), 0, m.sin(o_lat_rad)]])

# define z axis rotation matrix
rz = np.array([[m.cos(o_lon_rad), -m.sin(o_lon_rad), 0], [m.sin(o_lon_rad), m.cos(o_lon_rad), 0], [0, 0, 1]])

# calculate ecef vector
y_rot = np.matmul(ry, r_sez) # multiply y axis rotation matrix by r_sez vector
z_rot = np.matmul(rz, y_rot) # multiply z axis rotation matrix by results of y axis rotation above
ecef_x_km = r[0] + z_rot[0]
ecef_y_km = r[1] + z_rot[1]
ecef_z_km = r[2] + z_rot[2]

# print
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)