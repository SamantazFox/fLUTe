from flute.fileopen import *
from flute.display import simple


# Define the vertical size, in terminal lines, to be use when displaying LUTs
vSizeTerm = 2

# Basic binary file
data = fileParse_Bin('luts/topography.lut')
simple.unixTerm(data, vSizeTerm)

# Basic ascii file
data = fileParse_Txt('luts/vivid.lut')
simple.unixTerm(data, vSizeTerm)

# Advanced binary file, with header
data = fileParse_Bin('luts/royal.lut')
simple.unixTerm(data, vSizeTerm)

# Advanced ascii file, with header
data = fileParse_Txt('luts/neon-green.lut')
simple.unixTerm(data, vSizeTerm)
