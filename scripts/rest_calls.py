import basic_calls as bc
import chkp_parsers as pars
import json
import sys


def show_gateways(mgmt_json):  # Feed it with json contains mgmt_ip , mgmt_port, sid and see what will happen
    if not pars.check_if_data_exist(mgmt_json, 'mgmt_ip', 'mgmt_port',  'sid'):
        return pars.return_error('not enough arguments')

    result = bc.get_all_gateways(json.loads(mgmt_json))
    return pars.check_result(result, pars.rest_get_all_gateways)
    # As a result you will get json with gateways or json with 'error' and description


def get_sid(mgmt_json_no_sid):  # Feed it with json contains mgmt_ip , mgmt_port, user and password.
    if not pars.check_if_data_exist(mgmt_json_no_sid, 'mgmt_ip', 'mgmt_port', 'username', 'password'):
        return pars.return_error('not enough arguments')

    mgmt_json_no_sid = json.loads(mgmt_json_no_sid)
    mgmt_json_no_sid['sid'] = ''
    result = bc.login(mgmt_json_no_sid, mgmt_json_no_sid['username'], mgmt_json_no_sid['password'])
    return pars.check_result(result, json.dumps, get_sid='')
    # As a result you will get json with sid or json with 'error' and description


def main():
    management_ip = '172.16.198.129'
    management_port = '443'
    sid = ''
    username = 'admin'
    secret = '123qweASDa'
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
