#ipaddress_networks.py
import ipaddress
import argparse
import binascii
import re


#need to use .format

parser = argparse.ArgumentParser()
parser.add_argument('--ip', action="store", required=False, help="example: 192.168.9.1")
parser.add_argument('--network', action="store", required=False, help="example: 10.9.0.0/24")
parser.add_argument('--inet', action="store", required=False, help="example: 10.9.0.0/24")
args = parser.parse_args()


def network_info(network):

    for n in network:
        net = ipaddress.ip_network(n)
        print('{!r}'.format(net))
        print('is private: {:>10}'.format(str(net.is_private)))
        if net.is_private:
            get_class = re.match('\d{1,3}', n)
            oct = int(get_class.group())
            if oct < 127:
               print('Class: {:>12}'.format('A'))
            elif 128 < oct < 192:
                print('Class: {:>12}'.format('B'))
            elif 192 < oct < 224:
                print('Class: {:>12}'.format('C'))
        print('broadcast: {:>20}'.format(str(net.broadcast_address)))
        print('compressed: {:>20}'.format(str(net.compressed)))
        print('with netmask: {:>29}'.format(net.with_netmask))
        print('with hostmask: {:>25}'.format(str(net.with_hostmask)))
        print('num addresses: {:>7}'.format(str(net.num_addresses)))
        print()



def ip_info(ip):

    for i in ip:
        addr = ipaddress.ip_address(i)
        print('{!r}'.format(addr))
        print('   IP version:', addr.version)
        print('   is private:', addr.is_private)
        print('  packed form:', binascii.hexlify(addr.packed))
        print('      integer:', int(addr))
        print()



def itterate_network(network):
    for n in network:
        net = ipaddress.ip_network(n)
        print('{!r}'.format(net))
        for i, ip in zip(range(3), net):
            print(ip)
        print()

if  args.ip:
    ip = [args.ip]
    ip_info(ip)
elif args.network:
    network = [args.network]
    network_info(network)
elif args.inet:
    network = [args.inet]
    itterate_network(network)
else:
    sys.exit("some error message")