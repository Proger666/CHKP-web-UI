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


def get_sid(mgmt_json_no_sid): # Feed it with json contains
    if not pars.check_if_data_exist(mgmt_json_no_sid, 'mgmt_ip', 'mgmt_port',  'sid', 'username', 'password'):
        return pars.return_error('not enough arguments')

    mgmt_json_no_sid = json.loads(mgmt_json_no_sid)
    result = bc.login(mgmt_json_no_sid, mgmt_json_no_sid['username'], mgmt_json_no_sid['password'])

    if result['status_code'] == '200':
        return json.dumps({'sid': result['sid']})
    else:
        return pars.return_error(' '.join([thing for thing in result.values()]))


def main():
    management_ip = '172.16.198.129'
    management_port = '443'
    sid = ''
    username = 'admin'
    secret = '123qweASD'
    management_data = {'mgmt_ip': management_ip, 'mgmt_port': management_port, 'sid': ''}
    mgmt_json = json.dumps({'mgmt_ip': management_ip, 'mgmt_port': management_port, 'sid': sid, 'username': username,
                            'password': secret})

    login_result = json.loads(get_sid(mgmt_json))

    try:
        management_data['sid'] = login_result['sid']
    except KeyError:
        print(login_result)
        sys.exit(0)
    print("Logged in")

    print(show_gateways(json.dumps(management_data)))

    #gws = json.loads(show_gateways(management_data))
    #print(gws)

    print(bc.logout(management_data))

    return 0


if __name__ == '__main__':
  main()

