def api_error(msg):
    return {'status': 'error', 'msg': msg}


def api_success(data):
    return {'status': 'OK', 'data': data}
