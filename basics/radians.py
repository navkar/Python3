# Definition of radius
r = 192500

# Import radians function of math package
# import math
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
# You can calculate this as r * phi, where r is the radius and phi is the angle in radians. To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported.
dist = r * radians(12)

# Print out dist
print(str(dist))