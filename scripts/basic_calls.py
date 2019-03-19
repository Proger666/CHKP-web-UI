#!/usr/local/bin/python3

import requests
import json
import time


def api_call(management_data, command, json_payload):
    management_ip = management_data[0]
    management_port = management_data[1]
    sid = management_data[2]

    url = 'https://' + management_ip + ':' + management_port + '/web_api/v1.1/' + command
    requests.packages.urllib3.disable_warnings()
    if sid == '':
        request_headers = {'Content-Type': 'application/json'}
    else:
        request_headers = {'Content-Type': 'application/json', 'X-chkp-sid': sid}
    session = requests.Session()
    session.verify = False
    r = session.post(url, data=json.dumps(json_payload), headers=request_headers)

    return r.json()


def custom_command(management_data, command, **kwargs):
    result = api_call(management_data, command, kwargs)
    print('Custom commang result: ' + json.dumps(result))
    return result


def get_gateways(management_data):
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
    result = api_call(management_data, 'logout')
    print('Logout result: ' + json.dumps(result))
    return 0


def login(management_data, user, password):
    payload = {'user': user, 'password': password}
    response = api_call(management_data, 'login', payload)
    return response['sid']

