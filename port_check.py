#Port Scan 
import os
import re

def nmap(ip):
    num = []

    command = "nmap -F "+ip
    process = os.popen(command)
    results = str(process.read())
    r = results.split()
    del r[0:28:1]
    del r[-18:-1:1]
    r.pop()

    for group in chunker(r, 3):
        #print(group) # check for nmap result

        if group[1] == 'open':
            i = int(re.findall('\d+', group[0])[0]) #print only number
            num.append(i)
    return num


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


