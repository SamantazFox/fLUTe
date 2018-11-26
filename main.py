from flute.fileopen import *
from flute.display import simple


data = fileParse_Bin('luts/topography.lut')
simple.unixTerm(data, 5)

data = fileParse_Txt('luts/vivid.lut')
simple.unixTerm(data, 5)
