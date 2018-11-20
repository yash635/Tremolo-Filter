# Program Name: tremolo_filter.py
# Author Name: Yash Alpeshbhai Patel
# Course Title: CS 827 - Computer Audio
# Date: November 19, 2018
# Assignment Number: 3
# Program Description: This program read the PCM formatted mystery.dat file
#						as input and applies tremolo filter and writes the
#						output to out.dat as PCM formatted file.

import pandas as pd
import numpy as np
import random
import math

data = pd.read_csv("mystery.dat", header=None, delimiter=r"\s+")

a = data[0]
b = data[1]
time = []
amplitude = []

# Reading contents from mystery.dat file and storing to list
for i in range(0,int(len(a))):
   time.append(float(a.iloc[i]))
   amplitude.append(float(b.iloc[i]))

# Wet Level is depth of tremolo. 0 means no tremolo and 1 means it oscillates from 0 to maximum volume for given amplitude levels
wet_level = 0.75
control = 1
mod = 0
# Sampling rate divide by frequency of sinusiod for tremolo effect of the audio wave
# Frequency of the sample means number of oscillations of tremolo effect
sample = 44100/10
offset  = 1 - wet_level
temp = []

# Looping through each amplitude values and applying tremolo filter using LOw Frequency Oscillator
for i in range(0,int(len(time))):
	temp.append(float(amplitude[i]))
	m = mod*wet_level/sample
	temp[i] = (m + offset)*temp[i]
	mod += control
	if mod > sample:
		control = -1
	elif not mod:
		control = 1
	amplitude[i] = temp[i]   

# Open new file to write the output data
f = open("tremolo.dat", "w")

# Header for PCM formmated file
f.write("; Sample Rate "+str(44100)+"\n")
f.write("; Channels 1"+"\n")

# Wrtiing the list to the output file
for i in range(0,int(len(time))):
   f.write(str(time[i])+"   "+str(((amplitude[i])))) 
   f.write("\n")  

# Close the file
f.close()
