
import re
import sys
import os.path
import time


def usage():
    print("Usage: "   + sys.argv[0] + " [AUTHENTICATION METHOD] [SCOPE] [DEBUG]")
    print("Usage: "   + sys.argv[0] + " [pubkey|password|all] [valid|failed|all] verbose|off")
    print("Example: " + sys.argv[0] + " pubkey failed off")
    sys.exit()

def log_line_parser(line):
    global debug
    match0 = re.search('^(...).(..).(..:..:..)',line)
    match1 = re.search('for(.+?)from', line)
    match2 = re.search('from(.+?)port', line)
    match3 = re.search('sshd\[.*\]:(.+?)for',line)
    timestamp   = match0.group()
    username    = match1.group(1)
    ipaddress   = match2.group(1)
    auth_result = match3.group(1)
    if debug:
        pass
        # print(line,end = '')
    else:
        pass
        # print(timestamp + auth_result + username + ipaddress)

def log_file_parser(log_type,log_scope):
    # centos_ssh_log_file_path = "/var/log/secure"
    # ubuntu_shh_log_file_path = "/var/log/auth.log"
    fake_log_file = './auth.log.test.large'

    ssh_log_files = [fake_log_file]

    password_valid_login  = 'sshd\[.*\]*Accepted password'
    password_failed_login = 'sshd\[.*\]*Failed password'
    pubkey_valid_login    = 'sshd\[.*\]*Accepted publickey'
    pubkey_failed_login   = 'sshd\[.*\]*Failed publickey'

    for log_file in ssh_log_files:
        if os.path.isfile(log_file) :
            with open(log_file, "r") as file:
                for line in file:

                    if log_scope == 'valid' or log_scope == 'all':
                        if log_type == 'password' or log_type == 'all':
                            for match in re.finditer(password_valid_login, line, re.S):
                                log_line_parser(line)
                        if log_type == 'pubkey' or log_type == 'all':
                            for match in re.finditer(pubkey_valid_login, line, re.S):
                                log_line_parser(line)

                    if log_scope == 'failed' or log_scope == 'all':
                        if log_type == 'password' or log_type == 'all':
                            for match in re.finditer(password_failed_login, line, re.S):
                                log_line_parser(line)
                        if log_type == 'pubkey' or log_type == 'all':
                            for match in re.finditer(pubkey_failed_login, line, re.S):
                                log_line_parser(line)

if __name__ == '__main__':
    # option 1
    t1 = time.time()
    log_type    = "all"
    log_scope   = "all"
    verbose     = "verbose"
    if verbose == 'verbose':
        debug = True
    else:
        debug = False
    log_file_parser(log_type,log_scope)
    print(f"Time to process option 1 {time.time() - t1}")

    # option 2
    t2 = time.time()
    log_type    = "all"
    log_scope   = "failed"
    verbose     = "verbose"
    if verbose == 'verbose':
        debug = True
    else:
        debug = False
    log_file_parser(log_type,log_scope)
    print(f"Time to process option 2 {time.time() - t2}")

    # option 3
    t3 = time.time()
    log_type    = "password"
    log_scope   = "valid"
    verbose     = "verbose"
    if verbose == 'verbose':
        debug = True
    else:
        debug = False
    log_file_parser(log_type,log_scope)
    print(f"Time to process option 3 {time.time() - t3}")