
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


def gateways_list(gw):
    simple_gw_list = []
    for gw in gw['objects']:
        if gw['type'] == 'simple-gateway':
            simple_gw_list.append(SimpleGatewayObject(gw))
    return simple_gw_list
