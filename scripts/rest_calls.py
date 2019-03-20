import basic_calls as bc
import chkp_parsers as pars
import json


def show_gateways(mgmt_json):
    management_data = [mgmt_json['mgmt_ip'], mgmt_json['mgmt_port'], mgmt_json['mgmt-sid']]
    return json.dumps(pars.rest_get_all_gateways(bc.get_all_gateways(management_data)))


def get_sid(mgmt_json, username, password):
    management_data = [mgmt_json['mgmt_ip'], mgmt_json['mgmt_port'], {}]
    return json.dumps(bc.login(management_data, username, password))


'''
def main():
    management_ip = '172.16.198.129'
    management_port = '443'
    sid = ''
    username = 'admin'
    secret = '123qweASD'
    management_data = [management_ip, management_port, sid]
    sid = get_sid_test(management_data, username, secret)
    print(sid)
    management_data[2] = sid[1:-1]

    gws = json.loads(show_gateways_test(management_data))
    bc.logout(management_data)
    print(gws)
    return 0


if __name__ == '__main__':
  main()
'''
