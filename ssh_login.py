import pexpect

def ssh_connect(username, password, jumpserver):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-rsa ' + username + '@' + jumpserver
    maxRetries = 3
    retries = 0
    
    while(retries < maxRetries):
        try:
            
            child = pexpect.spawn(connStr)
            ret = child.expect([pexpect.TIMEOUT, pexpect.EOF, ssh_newkey, '[P|p]assword:'])
            if ret == 0:                                                                   
                if(retries >= maxRetries):
                    # print(child.before.decode())
                    print('[-] Error Connecting')
                    return 0
                # print(child.before.decode())
                retries+=1       
                continue
            if ret == 1:  
                if(retries >= maxRetries):
                    print('[-] Error Connecting')
                    return 1
                # print(child.before.decode())
                retries+=1       
                continue
            if ret == 2:
                child.sendline('yes')
                ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
                if ret == 0:
                    # print(child.before.decode())
                    print('[-] Error Connecting')
                    return 0
            # print(child.before.decode())
            child.sendline(password)
            child.expect('[$#]')
            return child
        
        except:
            return 0 

