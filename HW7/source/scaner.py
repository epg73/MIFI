import argparse
import json
import os

import requests


def sent_http_request(target, method, headers=None, payload=None):
    headers_dict = dict()
    if headers:
        for header in headers:
            header_name = header.split(':')[0]
            header_value = header.split(':')[1:]
            headers_dict[header_name] = ':'.join(header_value)
    if method == "GET":
        response = requests.get(target, headers=headers_dict)
    elif method == "POST":
        response = requests.post(target, headers=headers_dict, data=payload)
    print(f"[#] Response status code: {response.status_code}\n")
    print(f"[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n")
    print(  f"[#] Response content:\n {response.text}")


def do_ping_sweep(ip, num_of_host):
    ip_parts = ip.split('.')
    network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
    scanned_ip = network_ip + str(int(ip_parts[3]) + num_of_host)
    response = os.popen(f'ping  -c 2 {scanned_ip} ')
    print(f'{scanned_ip}')
    res = response.readlines()
    print(f"[#] Result of scanning: {scanned_ip} [#]\n{res[2]}", end='\n\n')


parser = argparse.ArgumentParser(description='Network scanner')
parser.add_argument('task', choices=['scan', 'sendhttp'], help='Network scan or send HTTP request')
parser.add_argument('-i', '--ip', type=str, help='IP address')
parser.add_argument('-n', '--num_of_hosts', default=2, type=int, help='Number of hosts')
parser.add_argument('-w', '--web', type=str, help='WEB address')
parser.add_argument('-m', '--mode', default='GET', type=str, help='mode GET or PUT')
parser.add_argument('-hd', '--headers', default=None, nargs='*', type=str, help="headers")
parser.add_argument('-p', '--payload', default=None, nargs='+', help='payload data')

args = parser.parse_args()

print(args.task)

if args.task == 'scan':
    if not args.ip:
        print("no ip ")
        exit(-1)
    for host_num in range(args.num_of_hosts):
        do_ping_sweep(args.ip, host_num)

elif args.task == 'sendhttp':
    if not args.web:
        print('no site, use -w http://[site]')
        exit(-2)

    print("++++++++++++++++++++++++++++")
    response = sent_http_request(args.web, args.mode, args.headers, args.payload)
else:
    print(f'no valid arguments')
