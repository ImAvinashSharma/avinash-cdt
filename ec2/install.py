import paramiko


def install_nginx(instance):
    public_ip = instance.public_ip_address

    print(f"The public IP address of instance {instance_id} is {public_ip}")

    key_filename = 'avi_test.pem'
    username = 'ubuntu'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=public_ip, username=username,
                key_filename=key_filename)

    stdin, stdout, stderr = ssh.exec_command('sudo apt install nginx -y')

    for line in stdout.readlines():
        print(line, end="")

    ssh.close()
