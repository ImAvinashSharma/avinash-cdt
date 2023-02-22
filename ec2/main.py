from vpc import create_vpc
from instance import create_ec2
from create_key import create_keypair
from install import install_nginx


if __name__ == '__main__':
    security_group_id, subnet_id = create_vpc()
    keypair = "avi_test1"
    create_keypair(keypair)
    public_ip = create_ec2(security_group_id, subnet_id, keypair)
    print("http://"+public_ip)
    install_nginx(public_ip, keypair+".pem")
