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
	print('LUT size: {}'.format(len(rgbValues)))
	for val in rgbValues: print(val)

	# Return the array containing the colors
	return rgbValues

# end of fileParse_Txt()


def fileParse_Bin(filePath):
	""" fileParse_Bin

	Input(s):
		filepath:	A string containing the path to a text-formatted LUT

	Returns:
		rgbValues:	A 2D list of 8-bits RGB values

	"""

	# Open the file in read only & binary mode, then read 8 KiB
	with open(filePath, 'rb') as fid:
		binData = fid.read(8192)

	# Init the list that will be returned to the caller
	rgbValues = []

	# Compute the length of one data block
	dataLen   = len(binData)
	remainder = dataLen % 3
	blockSize = int((dataLen - remainder) / 3)

	# If the LUT has an amount of byte that can't be divided by 3 (e.g some LUTs
	# have 50 bytes), then drop the first few byte(s)
	if (remainder != 0):
		binData = binData[remainder-1:]

	# Retrieve the different RGB values in this LUT
	for i in range(blockSize):
		r = int(binData[i])
		g = int(binData[i + blockSize])
		b = int(binData[i + blockSize + blockSize])

		# Append data to output list
		rgbValues.append([r, g, b])

	# Debug
	print('LUT size: {}'.format(len(rgbValues)))
	for val in rgbValues: print(val)

	# Return the array containing the colors
	return rgbValues

# end of fileParse_Bin()
