import os
import subprocess
"""
will update repository in S disk
You can place the script anywhere or even set it as a scheduled task
"""

path = r"S:\repoTools"
if not os.path.exists(path):
    raise Exception("Path not found!!.Clonaste el repositorio???")
os.chdir(path)


def updateRepo():
    try:
        cmd = "git pull"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        out, err = process.communicate()
        if err:
            raise Exception(err)
        print out
    except Exception as e:
		raise Exception(e)


if __name__ == '__main__':
	updateRepo()
