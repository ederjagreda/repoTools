import os
import subprocess
"""
will create a visible disk for S.O based on an asigned folder
Please replace folder value for your own folder path
"""

DiskToCreate = "S:"
folder = r"D:\dataSpain\conectarUnidadRedS" # dont forget to update!!!!!!!!!!


def createDisk():
	if not os.path.exists(folder):
		raise Exception("La ruta no parece correcta!!.Por favor revisar!!")
	try:
		cmd = "subst %s %s" % (DiskToCreate, folder)
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
							stderr=subprocess.PIPE, universal_newlines=True)
		out, err = process.communicate()
		if out:
			if 'SUBST' in str(out):
				print "disk already exists!!"
			else:
				raise Exception(out)
		elif err:
			raise Exception(err)
		else:
			print "disk created!!"
	except Exception as e:
		raise Exception(e)


if __name__ == '__main__':
	createDisk()
