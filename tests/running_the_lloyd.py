import sys
[sys.path.append(i) for i in ['.', '..']]

from lloyd import Field
import numpy as np

# generate 2000 observations with 2 dimensions
points = np.random.rand(2000, 2)

# create a lloyd model on which one can perform iterations
field = Field(points)

# run one iteration of Lloyd relaxation on the field of points
field.relax()

# get the resulting point positions
new_positions = field.get_points()

