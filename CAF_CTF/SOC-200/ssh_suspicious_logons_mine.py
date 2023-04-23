import re
import sys
import os.path
import time

def usage():
    print("Usage: "   + sys.argv[0] + " [AUTHENTICATION METHOD] [SCOPE] [DEBUG]")
    print("Usage: "   + sys.argv[0] + " [pubkey|password|all] [valid|failed|all] verbose|off")
    print("Example: " + sys.argv[0] + " pubkey failed off")
    sys.exit()

def log_line_parser(line, verbose):
    global debug
    match0 = re.search('^(...).(..).(..:..:..)',line)
    match1 = re.search('for(.+?)from', line)
    match2 = re.search('from(.+?)port', line)
    match3 = re.search('sshd\[.*\]:(.+?)for',line)
    timestamp   = match0.group()
    username    = match1.group(1)
    ipaddress   = match2.group(1)
    auth_result = match3.group(1)
    if verbose == "verbose":
        pass
        # print(line,end = '')
    else:
        pass
        # print(timestamp + auth_result + username + ipaddress)

def log_file_parser(log_type,log_scope,verbose):
    # centos_ssh_log_file_path = "/var/log/secure"
    # ubuntu_shh_log_file_path = "/var/log/auth.log"
    fake_log_file = './auth.log.test.large'

    ssh_log_files = [fake_log_file]

    password_valid_login  = 'sshd\[.*\]*Accepted password'
    password_failed_login = 'sshd\[.*\]*Failed password'
    pubkey_valid_login    = 'sshd\[.*\]*Accepted publickey'
    pubkey_failed_login   = 'sshd\[.*\]*Failed publickey'

    if log_scope == 'all':
        search_pattern = r"sshd\[.*\]*Accepted password|" \
                            "sshd\[.*\]*Failed password|" \
                            "sshd\[.*\]*Accepted publickey|" \
                            "sshd\[.*\]*Failed publickey"
    elif log_scope == "valid":
        if log_type == "all":
            search_pattern = r"sshd\[.*\]*Accepted password|sshd\[.*\]*Accepted publickey"
        elif log_type == "password":
            search_pattern = r"sshd\[.*\]*Accepted password"
        elif log_type == "pubkey":
            search_pattern = r"sshd\[.*\]*Accepted publickey"
    elif log_scope == "failed":
        if log_type == "all":
            search_pattern = r"sshd\[.*\]*Failed password|sshd\[.*\]*Failed publickey"
        elif log_type == "password":
            search_pattern = r"sshd\[.*\]*Failed password"
        elif log_type == "pubkey":
            search_pattern = r"sshd\[.*\]*Failed publickey"

    for log_file in ssh_log_files:
        if os.path.isfile(log_file) :
            with open(log_file, "r") as file:
                for line in file:
                    if re.search(search_pattern, line, re.S):
                        log_line_parser(line, verbose)

if __name__ == '__main__':
    # option 1
    t1 = time.time()
    log_type    = "all"
    log_scope   = "all"
    verbose     = "verbose"
    log_file_parser(log_type,log_scope, verbose)
    print(f"Time to process option 1 {time.time() - t1}")

    # option 2
    t2 = time.time()
    log_type    = "all"
    log_scope   = "failed"
    verbose     = "verbose"
    log_file_parser(log_type,log_scope, verbose)
    print(f"Time to process option 2 {time.time() - t2}")

    # option 3
    t3 = time.time()
    log_type    = "password"
    log_scope   = "valid"
    verbose     = "verbose"
    log_file_parser(log_type,log_scope, verbose)
    print(f"Time to process option 3 {time.time() - t3}")