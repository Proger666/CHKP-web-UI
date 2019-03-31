# -*- coding: utf-8 -*-
### required - do no delete
from rest_calls import *

# logging
log_user_str = ' for User: {}'.format(auth.user)


def mgmt_conn(mgmt_data):
    '''Connects to MGMT and stores SID as cookie string'''
    # check for defaults if not present - add
    if len(mgmt_data['ipAddr']) < 2 or len(mgmt_data['username']) < 1 or len(mgmt_data['password']) < 0:
        return api_error('Not enough info for login')
    DTO = {'mgmt_ip': mgmt_data['ipAddr'],
           'mgmt_port': mgmt_data.get('port', '443') if len(mgmt_data.get('port', '443'))> 0 else '443',
           'username': mgmt_data['username'],
           'password': mgmt_data['password'],
           'sid': '1'}
    logger.debug('Created DTO for mgmt connection {}'.format(DTO))
    data = json.dumps(DTO)
    result = None
    try:
        result = json.loads(get_sid(data))
        if 'error' in result:
            logger.error('Backend sent error in mgmt_conn {}'.format(result))
            return api_error('backend error: {}'.format(result['error']))
    except Exception as e:
        logger.error("Backend failed to server request with error: {}".format(str(e)))

    logger.error('Failed to connect to MGMT' + log_user_str)
    return api_error('Failed to make connection to Mgmt')


@request.restful()
def api():
    def POST(*args, **kwargs):

        # route request based on action field
        if request.vars.get('action', None) is not None:
            if request.vars['action'] == 'mgmt_conn':
                # connect to mgmt via API scripts
                # do we have data ?
                if request.vars.get('mgmt_data', None) is None:
                    logger.error('Failed to connect to mgmt - no mgmt data' + log_user_str)
                    return api_error('No mgmt data found')
                return mgmt_conn(request.vars.mgmt_data)
        logging.error('Failed to server request - no action choosen' + log_user_str)
        return api_error('Incorrect request')

    def GET(*args, **kwargs):
        return 'Not supported'

    return locals()
