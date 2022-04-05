import subprocess
import os
cmd = ['ping', 'www.linuxmind.info']
try:
    subprocess.run(cmd, timeout=5)
except subprocess.TimeoutExpired:
    print('process too long ')

s = 's=%r;print(s%%s,sep="")'
print(s % s, sep="")
