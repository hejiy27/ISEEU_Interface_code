import subprocess

def get_subprocess_result(command):
    proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    (out, err) = proc.communicate()
    return [line for line in out.split("\n") if line.strip() not in ('')]