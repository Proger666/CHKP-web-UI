
import json


class SimpleGatewayObject:
    def __init__(self, gateway):
        self.uid = gateway['uid']
        self.name = gateway['name']
        self.type = gateway['type']
        self.policy = gateway['policy']
        self.os = gateway['operating-system']
        self.hardware = gateway['hardware']
        self.version = gateway['version']
        self.ipv4_address = gateway['ipv4-address']
        self.sec_blades = gateway['network-security-blades']
        self.mgmt_blades = gateway['management-blades']
        self.vpn_domain = gateway['vpn-encryption-domain']
        self.sic_status = gateway['sic-status']
        self.tags = gateway['tags']
        self.icon = gateway['icon']
        self.groups = gateway['groups']
        self.comments = gateway['comments']
        self.color = gateway['color']

    def __str__(self):
        return self.name


def rest_get_all_gateways(gateways):
    simple_gateways = []
    cluster_members = []
    clusters = []
    management = []
    for gw in gateways['objects']:
        if gw['type'] == 'simple-gateway':
            simple_gateways.append(gw)
        elif gw['type'] == 'CpmiGatewayCluster':
            clusters.append(gw)
        elif gw['type'] == 'CpmiClusterMember':
            cluster_members.append(gw)
        elif gw['type'] == 'CpmiHostCkp':
            management.append(gw)
    gw_dict = {'gateways': simple_gateways, 'clusters': clusters, 'cluster_members': cluster_members, 'mgmt': management}
    return gw_dict


def get_simple_gateways_list(gw):
    simple_gw_list = []
    for gw in gw['objects']:
        if gw['type'] == 'simple-gateway':
            simple_gw_list.append(SimpleGatewayObject(gw))
    return simple_gw_list


def return_error(error):
    return json.dumps({'error': error})


def check_if_data_exist(data, *args):
    if type(data) == str:
        data = json.loads(data)

    for arg in args:
        try:
            data[arg]
        except KeyError:
            print("Not enough arguments")
            return False
    return True
