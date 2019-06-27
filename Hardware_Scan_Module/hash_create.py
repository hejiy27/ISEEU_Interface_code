import hashlib
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import datetime
from ISEEU_Utility import file_control
from functools import partial

def GetHashofDirs(directory, verbose=0):
  SHAhash = hashlib.md5()
  if not os.path.exists(directory):
    #Trigger when directory path not exist
    print("Path not exist")
    return -1
  try:
    #os.walk is A function that starts all the directories starting from the start directory
    for root, dirs, files in os.walk(directory):
      for names in files:
        if verbose == 1:
          #if verbose set, print file names.
          print('Hashing', names)
        filepath = os.path.join(root,names)
        try:
          #file open by binary mode
          f1 = open(filepath, 'rb')
        except:
          # You can't open the file for some reason
          f1.close()
          continue
        '''while 1:
          # Read file in as 4KB chunks
          buf = f1.read(4096)
          print(buf)
          if not buf : break
          SHAhash.update(hashlib.md5(buf).hexdigest())''' #only works in python2
        for buf in iter(partial(f1.read, 4096), b''):
            SHAhash.update(buf)
        f1.close()

  except:
    print("Error occured!")
    return -2
  #Return the digest of the data passed to the update() method.It returns hexadecimal digits
  return SHAhash.hexdigest()

def save_hash_dir(directory, verbose=0):
  dt = datetime.datetime.now()
  file_date = dt.strftime("%Y%m%d%H%M")
  file_name = "MD5_{file_date}".format(file_date=file_date)
  file = file_control.file_open("{}/result/hash_result"
                                .format(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))), file_name, 'w')
  file.write("{target}\t{result}\n".format(target = directory, result=GetHashofDirs(directory,verbose)))
  file.close()

if __name__ == "__main__":
    print(save_hash_dir("/root/Desktop/qemu_mips/rootfs_int"))