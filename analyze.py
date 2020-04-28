from parse import KeyPoints, Point
import os
import pprint

FILE = "DATA_30_FPS_2000_FRAMES"

j_files = [os.path.join(FILE, x) for x in os.listdir(FILE) if x.split(".")[1] == "json"]

frames = []

kp = 0 

for f, file in enumerate(j_files):
	try:

		k = KeyPoints(file)
		frames.append(k)
		
		i = len(k.points.keys())
		cf = len(k.points.keys())

		for key in k.points.keys():
			if k.points[key].c == 0:
				i -= 1
		for key in k.points.keys():
			if k.points[key].c < 0.75:
				cf -= 1

		print("Frame: {}\tKey Point Count:[{} of 25]\tConfidence >=75% [{} of 25]".format(str(f), str(i), str(cf)))

	except Exception as e:
		print("Error: [{}] Unable to process frame number {}".format(e, str(f)))