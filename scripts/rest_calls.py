import basic_calls as bc
import chkp_parsers as pars

def show_gateways(mgmt_json):
    #management_data = [mgmt_json['mgmt_ip'], mgmt_json[mgmt]]
    return pars.rest_get_all_gateways(bc.get_all_gateways(mgmt_json))

def get_sid(mgmt_data, username, password):
    return bc.login(mgmt_data, username, password)

def main():
    management_ip = '172.16.198.129'
    management_port = '443'
    sid = ''
    username = 'admin'
    secret = '123qweASD'
    management_data = [management_ip, management_port, sid]
    sid = get_sid(management_data, username, secret)
    management_data[2] = sid

    gws = show_gateways(management_data)
    bc.logout(management_data)
    print(gws)
    return 0


if __name__ == '__main__':
  main()
