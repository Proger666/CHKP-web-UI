import basic_calls as bc
import chkp_parsers as pars
import json
import sys


def show_gateways(mgmt_json):
    return json.dumps(pars.rest_get_all_gateways(bc.get_all_gateways(mgmt_json)))


def get_sid(mgmt_json_no_sid):
    mgmt_json_no_sid = json.loads(mgmt_json_no_sid)
    try:
        if (mgmt_json_no_sid['username'] and mgmt_json_no_sid['password']) != '':
            username = mgmt_json_no_sid['username']
            secret = mgmt_json_no_sid['password']
            return json.dumps(bc.login(mgmt_json_no_sid, username, secret))[1:-1]
    except KeyError:
        print("Not enough arguments")
        sys.exit(0)

def main():
    management_ip = '172.16.198.129'
    management_port = '443'
    sid = ''
    username = 'admin'
    secret = '123qweASD'
    management_data = json.dumps({'mgmt_ip': management_ip, 'mgmt_port': management_port, 'sid': sid,
                                  'username': username})
    sid = get_sid(management_data)
    print(sid)
    management_data = json.loads(management_data)
    management_data['sid'] = sid
    del management_data['username']
    del management_data['password']

    gws = json.loads(show_gateways(management_data))
    print(gws)
    bc.logout(management_data)
    #print(gws)
    return 0


if __name__ == '__main__':
  main()

