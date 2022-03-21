#Did you know that #Python has a built-in way to un-tar files?

#Check out this example using `tarfile`:
import tarfile
tar=tarfile.open("file.tar.gz")
tar.extractall()
tar.close()