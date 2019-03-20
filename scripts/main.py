#!/usr/local/bin/python3


import sys
import basic_calls as bc
import chkp_parsers as pars


def main():
    management_ip = '172.16.198.129'
    management_port = '443'
    sid = ''
    username = 'admin'
    secret = '123qweASD'
    management_data = [management_ip, management_port, sid]
    sid = bc.login(management_data, username, secret)
    management_data = [management_ip, management_port, sid]
    print('Management server data: ' + ' '.join(management_data))

    bc.custom_command(management_data, 'show-gateways-and-servers', **{'details-level': 'full'})

    '''gw_list = pars.gateways_list(bc.get_all_gateways(management_data))
    for gw in gw_list:
        print(gw.uid)'''

    bc.logout(management_data)
    sys.exit(0)


if __name__ == '__main__':
  main()
