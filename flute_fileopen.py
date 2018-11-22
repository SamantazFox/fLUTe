#!/bin/python
# -*- coding: utf-8 -*-

"""
	fLUTe - file opening utility

	:copyright: Copyright 2018, Samantaz
	:license: BSD 3-clauses, see LICENSE.md for more details

"""


def fileParse_Txt(filePath):
	""" fileParse_Txt

	Input(s):
		filepath:	A string containing the path to a text-formatted LUT

	Returns:
		rgbValues:	A 2D list of 8-bits RGB values

	"""

	# Open the file in text mode (read only) and read 8 KiB from it
	with open(filePath, 'r') as fid:
		textData = fid.read(8192)

	# Init the list that will hold the output data
	rgbValues = []

	# Loop through lines
	for line in textData.splitlines():
		tmpLine = line.split(sep = ' ')
		tmpArray = []

		for c in tmpLine:
			if c.isprintable() and c.isnumeric():
				tmpArray.append(int(c))

		# Once we finished parsing the line, add the list to 'rgbValues'
		rgbValues.append(tmpArray)

	# Debug
	for val in rgbValues: print(val)

	# Return the array containing the colors
	return rgbValues

# end of fileParse_Txt()


# "Main"
fileParse_Txt('luts/vivid.lut')
