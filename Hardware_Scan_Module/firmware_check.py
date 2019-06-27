import subprocess
import datetime
import os
import sys
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ISEEU_Utility import file_control,subprocess_control

'''def get_data_file_list(data_file_name):
    data_path = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    data = open(data_path + data_file_name, 'r')
    return [line for line in data.read().split("\n") if line.strip() != '']'''

# Check the boot process on the root file system. if success, it returns 0
def Check_boot_sequence(rootfs_path):
    if type(rootfs_path) != str :
        print("command type is not str")
        exit(1)
    command = os.path.dirname(__file__)+"/firmwalker_mod.sh " + rootfs_path
    return subprocess.check_call(command, shell=True)

'''def Execute(command, save_folder, save_file):
    with file_control.file_open(save_folder, save_file, 'a') as save_file:
        for result in subprocess_control.get_subprocess_result(command):
            if result is not '':
                save_file.write(result+"\n")'''

'''def firmwalker_mod(path):
    dt = datetime.datetime.now()
    file_date = dt.strftime("%Y%m%d%H%M")
    save_path = "{}/result/firm_check/{}".format(os.path.dirname(os.path.abspath(os.path.dirname(__file__))),file_date)
    # 1) passfile
    for p in get_data_file_list("passfiles"):
        command = "find {FIRMDIR} -name {passfiles}".format(FIRMDIR=path, passfiles=p)
        Execute(command,save_path,"passfiles")

    # 2) MD5 hashes
    #command = "egrep -sro '\$1\$\w{8}\S{23}' {FIRMDIR}".format(FIRMDIR=path)
    #Execute(command,save_path,"Hash")

    # 3) SSL_Files
    for ssl in get_data_file_list("sslfiles"):
        command = "find {FIRMDIR} -name {sslfile} ".format(FIRMDIR=path,sslfile=ssl)
        Execute(command,save_path,"sslfiles")

    # 4) SSH_Files
    for ssh in get_data_file_list("sshfiles"):
        command = "find {FIRMDIR} -name {sshfile}".format(FIRMDIR=path,sshfile=ssh)
        Execute(command,save_path,"sshfiles")

    # 5) DB_Files
    for db in get_data_file_list("dbfiles"):
        command = "find {FIRMDIR} -name {file}".format(FIRMDIR=path,file=db)
        Execute(command,save_path,"dbfiles")

    # 6) Web_Servers
    for ws in get_data_file_list("webservers"):
        command="find {FIRMDIR} -name '{webserver}'".format(FIRMDIR=path,webserver=ws)
        Execute(command,save_path,"webservers")

    # 7) Binary
    for b in get_data_file_list("binaries"):
        command = "find {FIRMDIR} -name '{binary}'".format(FIRMDIR=path,binary=b)
        Execute(command,save_path,"binaries")

    # 8) Patterns
    for p in get_data_file_list("patterns"):
        command = "grep -lsirnw {FIRMDIR} -e '{pattern}'".format(FIRMDIR=path,pattern=p)
        Execute(command,save_path+"/patterns",p)
    # 9) IP
    #command = "grep -sRIEho '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' --exclude='console' $FIRMDIR | sort | uniq".format()

    #10)

    #11)

    #12) SetUID
    command = "find $FIRMDIR -user root -perm -4000"
    Execute(command,save_path,"SetUID")

    print("check_finished")
# stand-alone execution code
if __name__ == "__main__" :
    firmwalker_mod("/root/Desktop/qemu_mips/rootfs_int")'''
