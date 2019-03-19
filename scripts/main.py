#!/usr/local/bin/python3

import requests
import json
import sys
import time
import basic_calls


def main():
    management_ip = '172.16.198.129'
    management_port = '443'
    sid = ''
    username = 'admin'
    secret = '123qweASD'
    management_data = [management_ip, management_port, sid]
    sid = login(management_data, username, secret)
    management_data = [management_ip, management_port, sid]
    print('Management server data: ' + ' '.join(management_data))

    test = custom_command

    logout(management_data)
    sys.exit(0)


if __name__ == '__main__':
  main()
