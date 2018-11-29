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

	# Each value of the LUT are stored on their own line, in the format 'R G B'
	# So split the file on new lines ('\n') in order to parse it
	splittedData = textData.splitlines()

	# The LUT has a header line if the first line contains one of those:
	#   "Index", "Red", "Green" or "Blue"
	firstLineLower = splittedData[0].lower()
	hasIndexValues = False

	if ('red' and 'green' and 'blue') in firstLineLower:
		# Detect if the line contains the 4th "index" column
		if 'index' in firstLineLower: hasIndexValues = True

		# Drop the first line from data
		splittedData = splittedData[0:]

	# Loop through lines
	# TODO: use regexes!!
	for line in splittedData:
		# Detect the separation character used in lines (tab or space(s)?)
		# If none of them are used, skip line
		if '\t' in line:  splitChar = '\t'
		elif ' ' in line: splitChar = ' '
		else: continue

		# Split current line using the character detected above
		tmpLine = line.split(sep = splitChar)
		tmpArray = []

		for c in tmpLine:
			if c.isprintable() and c.isnumeric():
				tmpArray.append(int(c))

		# In the case where the line contains 4 values, drop the "Index" one
		# If the current line did not provide 3 values, ignore it
		if (len(tmpArray) == 4 and hasIndexValues): tmpArray.pop(0)
		if len(tmpArray) != 3: continue

		# Once we finished parsing the line, add the list to 'rgbValues'
		rgbValues.append(tmpArray)

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

	# If the binary data begins with the magic bytes 0x4943 0x4f4c, then it has
	# a 32-bits header before the real data, which has to be removed.
	if binData[:4] == bytearray(b'\x49\x43\x4f\x4c'):
		binData = binData[32:]

	# Compute the length of one data block
	dataLen   = len(binData)
	remainder = dataLen % 3
	blockSize = int((dataLen - remainder) / 3)

	# If the LUT can't be divided in 3 blocks, print an error
	if (remainder != 0):
		print("Can\'t open LUT at path '{}'".format(filePath))
		return rgbValues

	# Retrieve the different RGB values in this LUT
	for i in range(blockSize):
		r = int(binData[i])
		g = int(binData[i + blockSize])
		b = int(binData[i + blockSize + blockSize])

		# Append data to output list
		rgbValues.append([r, g, b])

	# Return the array containing the colors
	return rgbValues

# end of fileParse_Bin()
