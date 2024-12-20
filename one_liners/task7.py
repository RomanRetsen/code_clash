import re
import os

centos_ssh_log_file_path = "/var/log/secure"
ubuntu_shh_log_file_path = "/var/log/auth.log"
reg_pat = r"sshd\[(.*)\]"
ssh_log_files = [centos_ssh_log_file_path,ubuntu_shh_log_file_path]
for log_file in ssh_log_files:
    if os.path.isfile(log_file):
        with open(log_file) as f:
            for line in f:
                if (result := re.search(reg_pat, line)):
                    print(result.group(1))