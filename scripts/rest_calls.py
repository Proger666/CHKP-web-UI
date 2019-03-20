import basic_calls as bc
import chkp_parsers as pars
import json
import sys


def show_gateways(mgmt_json):
    if not pars.check_if_data_exist(mgmt_json, 'mgmt_ip', 'mgmt_port',  'sid'):
        return pars.return_error('not enough arguments')

    mgmt_json = json.loads(mgmt_json)

    if mgmt_json['sid'] != '':
        return json.dumps(pars.rest_get_all_gateways(bc.get_all_gateways(mgmt_json)))
    else:
        return pars.return_error('no sid')


def get_sid(mgmt_json_no_sid):
    if not pars.check_if_data_exist(mgmt_json_no_sid, 'mgmt_ip', 'mgmt_port',  'sid', 'username', 'password'):
        return pars.return_error('not enough arguments')

    mgmt_json_no_sid = json.loads(mgmt_json_no_sid)
    if (mgmt_json_no_sid['username'] and mgmt_json_no_sid['password']) != '':
        username = mgmt_json_no_sid['username']
        secret = mgmt_json_no_sid['password']
    return json.dumps({'sid': bc.login(mgmt_json_no_sid, username, secret)})


def main():
    management_ip = '172.16.198.129'
    management_port = '443'
    sid = ''
    username = 'admin'
    secret = '123qweASD'
    management_data = {'mgmt_ip': management_ip, 'mgmt_port': management_port, 'sid': ''}
    mgmt_json = json.dumps({'mgmt_ip': management_ip, 'mgmt_port': management_port, 'sid': sid, 'username': username,
                            'password': secret})

    management_data['sid'] = json.loads(get_sid(mgmt_json))['sid']
    print("Logged in")
    print(show_gateways(mgmt_json))

    #gws = json.loads(show_gateways(management_data))
    #print(gws)

    bc.logout(management_data)

    return 0


if __name__ == '__main__':
  main()

