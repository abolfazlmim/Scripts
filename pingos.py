import subprocess
import os 
cmd = ['ping','www.linuxmind.info']
try:
  subprocess.run(cmd , timeout=5)
except subprocess.TimeoutExpired:
    print('process too long ')


