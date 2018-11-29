#!/bin/python
# -*- coding: utf-8 -*-

"""
	fLUTe - Simple (command-line) output methods

	:copyright: Copyright 2018, Samantaz
	:license: BSD 3-clauses, see LICENSE.md for more details

"""

from os import system


def unixTerm(rgbArray, lineCount = 3):
	""" unixTerm

	Input(s):
		rgbArray:   A list of RGB values, like what fileParse_xxx() can return
		lineCount:  The amount of terminal lines to use when printing the LUT

	Returns:
		Nothing.

	"""

	# Check that the LUT is not empty
	arrayLength = len(rgbArray)

	if not (arrayLength > 0):
		print('\nCannot display empty LUT')
		return

	# Display the amount of RGB values in the array
	print('\nLUT size: ' + str(arrayLength))

	# Init the output string
	outStr = ''

	# Create a string of output sequences 
	for val in rgbArray:
		outStr += '\e[48;2;{};{};{}m '.format(val[0], val[1], val[2])

	# Terminate the string with a "reset" escape sequence and a new line
	outStr +=  '\e[0m\n'

	# Print as many lines as what was provided in parameter
	for i in range(lineCount):
		system('printf "' + outStr + '"')

# end of unixTerm()
