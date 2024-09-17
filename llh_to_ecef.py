# python3 llh_to_ecef lat_deg lon_deg hae_km
#
# Usage: python3 llh_to_ecef lat_deg lon_deg hae_km
#  Converts llh to ECEF coordinates 
# Parameters:
#  lat_deg: lattitude in degrees
#  lon_deg : longetude in degrees
#  hae_km : height above the ellipsoid in km
# Output:
#
# Written by Olivia Powell
# Other contributors: 

# import Python modules
import sys # argv
import math as m

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions
## function description
def calc_denom(ecc,lat_rad):
    return m.sqrt(1-ecc**2 *(m.sin(lat_rad))**2)

# initialize script arguments
lat_deg = float('nan') #float is anything that is not a whole real number
lon_deg = float('nan') 
hae_km = float('nan')

# parse script arguments
if len(sys.argv)==4: #if the # of things in the command line is 4
  lat_deg = float(sys.argv[1]) #the first thing in the command line is this
  lon_deg = float(sys.argv[2]) #the second thing in the command line is this
  hae_km = float(sys.argv[3])  #etc., etc.
  ...
else:
  print(\
   'Usage: '\
   'python3 llh_to_ecef lat_deg lon_deg hae_km'\
  )
  exit()

  ## scripting below

  # equations to find r_x, r_y, and r_z
lat_rad = lat_deg*m.pi/180
lon_rad = lon_deg*m.pi/180
denom = calc_denom(E_E, lat_rad)
c_e = R_E_KM/denom
s_e = R_E_KM*(1 - E_E**2)/denom
r_x = (c_e+hae_km)*m.cos(lat_rad)*m.cos(lon_rad)
r_y = (c_e+hae_km)*m.cos(lat_rad)*m.sin(lon_rad)
r_z = (s_e+hae_km)*m.sin(lat_rad)

print(r_x)
print(r_y)
print(r_z)
