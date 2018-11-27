from flute.fileopen import *
from flute.display import simple


# Basic binary file
data = fileParse_Bin('luts/topography.lut')
simple.unixTerm(data, 5)

# Basic ascii file
data = fileParse_Txt('luts/vivid.lut')
simple.unixTerm(data, 5)

# Advanced binary file, with header
data = fileParse_Bin('luts/royal.lut')
simple.unixTerm(data, 5)
