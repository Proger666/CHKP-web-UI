# -*- coding: utf-8 -*-
### required - do no delete
from web2py.gluon import request


def get_gateways():
    '''Return gateway objects for give MGMT IP'''
    MGMT_IP = request.vars.mgmt_ip
    gws = []
    return gws
