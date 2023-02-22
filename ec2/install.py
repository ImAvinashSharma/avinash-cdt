import paramiko
import time


def install_nginx(public_ip, key_filename):
    try:
        print("Installing nginx...")
        time.sleep(90)
        username = 'ubuntu'

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(hostname=public_ip, username=username,
                    key_filename=key_filename)

        stdin, stdout, stderr = ssh.exec_command('sudo apt install nginx -y')

        for line in stdout.readlines():
            print(line, end="")

        ssh.close()
    except:
        print("error occurred during installation of nginx")
