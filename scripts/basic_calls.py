#!/usr/local/bin/python3

import requests
import json
import time
import chkp_parsers as pars


def api_call(management_data, command, json_payload):

    url = 'https://' + management_data['mgmt_ip'] + ':' + management_data['mgmt_port'] + '/web_api/v1.1/' + command
    requests.packages.urllib3.disable_warnings()
    if management_data['sid'] == '':
        request_headers = {'Content-Type': 'application/json'}
    else:
        request_headers = {'Content-Type': 'application/json', 'X-chkp-sid': management_data['sid']}
    session = requests.Session()
    session.verify = False
    result = session.post(url, data=json.dumps(json_payload), headers=request_headers)
    r = result.json()
    r['status_code'] = str(result.status_code)
    return r


def custom_command(management_data, command, **kwargs):
    result = api_call(management_data, command, kwargs)
    parsed_result = json.dumps(result)
    print('Custom commang result: ' + json.dumps(result))
    return result


def get_all_gateways(management_data):
    payload = {'details-level': 'full'}
    result = api_call(management_data, 'show-gateways-and-servers', payload)
    return result


def create_host_object(management_data, name, host_ip, kwargs):
    payload = {'name': name, 'ip-address': host_ip, **kwargs}
    result = api_call(management_data, 'add-host', payload)
    # time.sleep(2)
    print('Create host result: ' + json.dumps(result))
    return 0


def create_network_object(management_data, name, subnet, mask_length, **kwargs):
    payload = {'name': name, 'subnet': subnet, 'mask-length': mask_length, **kwargs}
    result = api_call(management_data, 'add-network', payload)
    # time.sleep(2)
    print('Create network result: ' + json.dumps(result))
    return 0


def publish(management_data):
    result = api_call(management_data, 'publish', {})
    time.sleep(5)
    print('Publish result: ' + json.dumps(result))
    return 0


def discard(management_data, session_uid):
    payload = {'uid': session_uid}
    result = api_call(management_data, 'discard', payload)
    print('Discards result: ' + json.dumps(result))
    return 0


def logout(management_data):
    result = api_call(management_data, 'logout', {})
    print('Logout result: ' + json.dumps(result))
    return 0


def login(management_data, user, password):
    payload = {'user': user, 'password': password}
    response = api_call(management_data, 'login', payload)
    if response['status_code'] == '200':
        return response['sid']
    else:
        return pars.return_error(' '.join(response))

