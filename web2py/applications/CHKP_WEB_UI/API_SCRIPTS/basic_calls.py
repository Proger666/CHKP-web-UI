#!/usr/local/bin/python3

import requests
import json
import time
import chkp_parsers as pars


class MGMTServer:
    def __init__(self, ip, username, password,port=443, ver=1.1, sid=''):
        '''Create only one MGMT Object '''
        self.val = None

        self.ip = ip,
        self.port = port,
        self.ver = ver
        self.sid = sid
        self.username = username
        self.password = password

    def __str__(self):
        return repr(self) + self.val

    instance = None

    def __new__(cls, **kwargs):  # __new__ always a classmethod
        if not MGMTServer.instance:
            MGMTServer.instance = MGMTServer.__OnlyOne(**kwargs)
        return MGMTServer.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, **kwargs):
        return setattr(self.instance, name, **kwargs)

def api_call(management_data, command, json_payload):
    url = 'https://' + management_data.ip + ':' + management_data.port + '/web_api/{}'.format(management_data.ver) + command
    requests.packages.urllib3.disable_warnings()
    if management_data.sid == '':
        request_headers = {'Content-Type': 'application/json'}
    else:
        request_headers = {'Content-Type': 'application/json', 'X-chkp-sid': management_data.sid}
    session = requests.Session()
    session.verify = False
    result = session.post(url, data=json.dumps(json_payload), headers=request_headers)
    r = result.json()
    r['status_code'] = str(result.status_code)
    return r


def custom_command(management_data, command, **kwargs):
    return api_call(management_data, command, kwargs)


def get_all_gateways(management_data):
    payload = {'details-level': 'full'}
    return api_call(management_data, 'show-gateways-and-servers', payload)


def create_host_object(management_data, name, host_ip, kwargs):
    payload = {'name': name, 'ip-address': host_ip, **kwargs}
    return json.dumps(api_call(management_data, 'add-host', payload))


def create_network_object(management_data, name, subnet, mask_length, **kwargs):
    payload = {'name': name, 'subnet': subnet, 'mask-length': mask_length, **kwargs}
    return json.dumps(api_call(management_data, 'add-network', payload))


def publish(management_data):
    result = api_call(management_data, 'publish', {})
    time.sleep(5)
    return json.dumps(result)


def discard(management_data, session_uid):
    payload = {'uid': session_uid}
    return json.dumps(api_call(management_data, 'discard', payload))


def logout(management_data):
    return json.dumps(api_call(management_data, 'logout', {}))


def login(management_obj):
    payload = {'user': management_obj.username, 'password': management_obj.password}
    return api_call(management_obj, 'login', payload)
