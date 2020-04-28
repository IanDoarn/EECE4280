"""
check.py

This script utilizes the asyncio lib to
check for an available file.

If no available file is present, nothing happens.
"""
import asyncio
import os

# number of attempts to check for a file
RETRY = 5

# number of seconds to wait in between attempts 
SLEEP_TIME = 5

# picture file extensions to check for
PIC_EXTS = ['.avi']

# Directory to pull images from
SOURCE = r'C:\\Users\\ronal\\Downloads\\openpose-1.5.1-binaries-win64-gpu-python-flir-3d_recommended\\openpose\\examples\\media'


def check_for_files():
	'''
	check if picture is available in the Files
	directory
	'''
	is_picture = lambda ext: ext in PIC_EXTS
	f = os.listdir(os.path.join(os.curdir, SOURCE))
	return any(is_picture(os.path.splitext(file)[1]) for file in f)


async def wait_for_file_available(retry=RETRY):
	'''
	Wait for a picture file to be available
	for processing. Retry check after a 
	specified amount of time. Default 5 times.
	'''
	for i in range(retry + 1):
		if check_for_files():
			print('File(s) found.')
			return True
		else:
			print('No file(s) found. Retrying in {} seconds [{} of {}]'.format(
				str(SLEEP_TIME), str(i), str(RETRY)))
			await asyncio.sleep(SLEEP_TIME)
	return False


async def main():

	ff = False

	# Check for source directory directory
	if not os.path.isdir(os.path.join(os.curdir, SOURCE)):
		raise FileNotFoundError('Could not locate directory {}'.format(
			os.path.join(os.curdir, SOURCE)))

	# Wait for picture file to be available
	try:
		print('Checking for available video files.')
		ff = await asyncio.wait_for(wait_for_file_available(), timeout=60.0)

		# # file is now available
		os.system("C:\\Users\\ronal\\Downloads\\openpose-1.5.1-binaries-win64-gpu-python-flir-3d_recommended\\openpose\\bin\\OpenPoseDemo.exe --video C:\\Users\\ronal\\Downloads\\openpose-1.5.1-binaries-win64-gpu-python-flir-3d_recommended\\openpose\\examples\\media\\capture.avi --write_video C:\\Users\\ronal\\Downloads\\openpose-1.5.1-binaries-win64-gpu-python-flir-3d_recommended\\openpose\\examples\\media\\test.avi --display 0")


	except asyncio.TimeoutError:
		print('Process timed out after 60 seconds.')
	finally:
		if not ff:
			print('No file(s) found. Please place a file of type(s) {}' \
				  ' in the directory [{}]'.format(str(PIC_EXTS), os.path.join(os.curdir, SOURCE)))



if __name__ == '__main__':
	asyncio.run(main())

	