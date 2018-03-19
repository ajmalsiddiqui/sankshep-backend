'''
Function to invoke a speech to text API
TODO: Complete the goddamn module :3
Try speechmatics maybe?
'''
import requests

def getText(filename):
	file_data ={
		'data_file': open(filename, 'rb'),
		'model': ('', 'en-US')
	}
	# TODO write the rest of the code :p
	
