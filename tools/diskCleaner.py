import subprocess
"""
will delete disk created by command
"""

DiskToDelete = "S:"


def deleteDisk():
	try:
		cmd = "subst /d S:"
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
							stderr=subprocess.PIPE, universal_newlines=True)
		print "disco S: borrado!!"

	except Exception as e:
		raise Exception(e)


if __name__ == '__main__':
	deleteDisk()
