# -*- coding: utf-8 -*-
### required - do no delete
import applications.CHKP_WEB_UI.API_SCRIPTS.basic_calls as bc


def check_conn():
    '''Check if MGMT server is connected to WEB UI'''
    MGMT_IP = session.mgmt_sid
    try:
        if MGMT_IP is None:
            return False
        else:

            # Get last MGMT IP from DB
            MGMT_IP = db((db.t_mgmt_server.id > 0) & (db.t_mgmt_server.is_enabled == True)).select(db.t_mgmt.last_ip)
            if len(MGMT_IP.records) > 0:
                return False
            else:
                # Try to create or get previous
                MGMT_obj = bc.MGMTServer(request.vars.mgmt_ip, request.vars.mgmt_username, request.vars.mgmt_pwd)
                if bc.login(MGMT_obj):
                    return True
    except Exception as e:
        print("Opps we screwed:\n{]".format(str(request)))
    return False
